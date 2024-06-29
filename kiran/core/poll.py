from __future__ import annotations

import httpx
import typing
import datetime
import asyncio
from ..components.commands import CallableBotCommandDetails
from ..components.context import CommandContext
# import traceback

if typing.TYPE_CHECKING:
    from ..impl import KiranBot


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
        timeout: typing.Optional[int] = 100,
    ) -> None:
        self._session = client.session
        self.START_TIME = datetime.datetime.now()
        self.client = client
        self.timeout = timeout
        self.last_event_id: int = 0
        self.client.log(
            f"Polling has started for Telegram bot with timeout: {timeout}. Waiting for events.",
            "debug",
        )

    async def _make_polling_session(
        self,
    ) -> typing.Optional[httpx.Response]:
        while True:
            try:
                response = await self._session.get(
                    "getUpdates",
                    params={
                        "timeout": self.timeout,
                        "offset": self.last_event_id + 1,
                    },
                )
                self.client.log(f"Polling Response:\n{response.text}", "debug")
                return response
            except Exception as e:
                self.client.log(
                    f"Error while making request to Telegram:\n {str(e)}",
                    "error",
                )
                # self.client.log(traceback.format_exc(), "debug")
                await asyncio.sleep(5)

    async def _start_command_consumption(
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
    ) -> None: ...
    #TODO
    # Implement this by appending it to the list in the `self`.
    async def start_polling(self):
        while True:
            try:
                response = await self._make_polling_session()
                if response and response.status_code == 200:
                    updates = response.json()
                    if updates["result"]:
                        for update in updates["result"]:
                            self.last_event_id = update["update_id"]
                await asyncio.sleep(1)
            except Exception as e:
                self.client.log(
                    f"Error encountered while tracing updates: {str(e)}",
                    "error",
                )
                await asyncio.sleep(5)

    async def poll(self):
        await self.start_polling()
