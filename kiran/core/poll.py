from __future__ import annotations

import asyncio
import datetime
import traceback
import typing

import msgspec

from ..abc.dependent import Message  # noqa: TCH001
from ..components.commands import CallableBotCommandDetails  # noqa: TCH001
from ..components.context import CommandContext
from ..core.enums import MessageEntityType

if typing.TYPE_CHECKING:
    from ..impl import KiranBot


class CalledResult(msgspec.Struct):
    update_id: int
    message: typing.Optional[Message] = None


class CallResponse(msgspec.Struct):
    ok: bool
    result: typing.List[CalledResult]


class PollingManager:
    """
    A module class that helps to poll the polling URL using a long polling interval method.
    Check for events and invokes them.

    Parameters
    ----------
    token : str
        The Telegram bot token.
    client : KiranBot
        The bot client.
    timeout : typing.Optional[int]
        The timeout for the polling. Defaults to 100.
    """

    def __init__(
        self,
        client: "KiranBot",
        timeout: int = 999,
    ) -> None:
        self.client = client
        self.client.log(
            "Polling Manager: Client has been initialized.", "debug"
        )
        self.response_binder = msgspec.json.Decoder(
            type=CallResponse, strict=False
        )
        self.client.log(
            "Polling Manager: Response Binder has been initialized.", "debug"
        )
        self.result_binder = msgspec.json.Decoder(
            type=CalledResult, strict=False
        )
        self.client.log(
            "Polling Manager: Result Binder has been initialized.", "debug"
        )
        self._session = client.session
        self.client.log(
            "Polling Manager: Client session has been initialized.", "debug"
        )
        self.START_TIME = datetime.datetime.now()
        self.client.log(
            "Polling Manager: Start time taken into account.", "debug"
        )
        self.timeout = timeout
        self.client.log(
            "Polling Manager: Timeout has been taken into account.", "debug"
        )
        self._slash_commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ] = {}
        self.client.log(
            "Polling Manager: Slash command storage initialized.", "debug"
        )
        self._prefix_commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ] = {}
        self.client.log(
            "Polling Manager: prefix command storage initialized.", "debug"
        )
        self._common_commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ] = {}
        self.client.log(
            "Polling Manager: Common command storage initialized.", "debug"
        )
        self.last_event_id: int = 0
        self.client.log(
            "Polling Manager: Last Event ID set to 0, offset taken into account.",
            "debug",
        )
        self.client.log(
            f"Polling has started for Telegram bot with timeout: {timeout}. Waiting for events.",
            "debug",
        )

    def _extract_command_name(self, s: str) -> str:
        cmd_name = s.split("/")[1]
        cmd_name = cmd_name.split(" ")[0]
        cmd_name = cmd_name.split("@")[0]
        return cmd_name

    async def _make_polling_session(
        self,
    ) -> typing.Optional[CallResponse]:
        try:
            response = await self._session.get(
                "getUpdates",
                params={
                    "timeout": self.timeout,
                    "offset": self.last_event_id + 1,
                },
                timeout=self.timeout,
            )
            if response.json()["result"] is not None:
                self.client.log(
                    f"Polling Response:\n{msgspec.json.format(response.text, indent=4)}",
                    "debug",
                )
            response_call = self.response_binder.decode(response.read())
            if response_call.ok is True:
                updates = response_call.result
                if updates:  # Check if updates is not empty
                    max_update_id = self.last_event_id
                    for update in updates:
                        if update.update_id > max_update_id:
                            max_update_id = update.update_id
                        if update.message is not None:
                            await self._invoke_command(update.message)
                    self.last_event_id = max_update_id  # Update last_event_id after processing all updates
            return response_call
        except Exception as e:
            self.client.log(
                message=f"Error while making request to Telegram:\n {e}",
                log_type="error",
            )
            self.client.log(traceback.format_exc(), "debug")
            print(traceback.format_exc())
            await asyncio.sleep(5)

    async def add_command_list(
        self,
        slash_commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ],
        prefix_commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ],
        common_commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ],
    ) -> None:
        self._slash_commands = slash_commands
        self._prefix_commands = prefix_commands
        self._common_commands = common_commands

    async def _invoke_command(self, obj_msg: Message) -> None:
        if obj_msg.entities is not None:
            command_pretext = obj_msg.entities[0]
            if command_pretext.type is MessageEntityType.BOT_COMMAND:
                assert obj_msg.text is not None
                net_cmds = self._slash_commands | self._common_commands
                cmd_name = self._extract_command_name(obj_msg.text)
                for cmd in net_cmds:
                    if cmd_name == cmd.name:
                        await net_cmds[cmd](
                            CommandContext(
                                name=cmd_name,
                                description=cmd.description,
                                prefix="/",
                                message_id=obj_msg.message_id,
                                chat_id=obj_msg.chat.id or 0,
                                invoking_message=obj_msg.text,
                                caller=self.client.caller,
                                client=self.client,
                                context_time=datetime.datetime.now(),
                            )
                        )
                        break

    async def start_polling(self):
        self.client.log(
            "Bot has started to receive events. Polling for dispatches started.",
            "info",
        )
        while True:
            try:
                response = await self._make_polling_session()
                if response is not None and response.ok is True:
                    updates = response.result
                    for update in updates:
                        if update.update_id > self.last_event_id:
                            self.last_event_id = update.update_id
                            if update.message is not None:
                                await self._invoke_command(update.message)
                await asyncio.sleep(1)
            except Exception as e:
                self.client.log(
                    f"Error encountered while tracing updates: {e}",
                    "error",
                )
                await asyncio.sleep(5)

    async def poll(self):
        await self.start_polling()
