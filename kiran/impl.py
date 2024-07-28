from __future__ import annotations

import asyncio
import inspect
import typing

import httpx

from ._about import __banner__
from .abc.bots import BotCommand
from .abc.bots import BotCommandScope
from .abc.bots import BotCommandScopeDefault
from .components.commands import CallableBotCommandDetails
from .components.commands import CommandImplements
from .components.commands import LanguageCode
from .components.context import CommandContext
from .core.cache import KiranCache
from .core.methods import KiranCaller
from .core.poll import PollingManager
from .errors import CommandImplementationError
from .logger import DefaultSettings
from .logger import KiranLogger
from .logger import LoggerSettings

CommandFunction = typing.Callable[[CommandContext], typing.Awaitable[None]]
ImplementationMethod = typing.Union[int, CommandImplements]

if typing.TYPE_CHECKING:
    import datetime

    from .core.events import KiranEvent


LoadProxy = typing.Union[
    typing.List[typing.Mapping[str, str]], typing.Mapping[str, str]
]
"""
LoadProxy is a type that specifies the proxy for the bot. It can be used in two ways:
The proxy settings can be accessed using the configuration module in Kiran.

Parameters
----------
proxy_type : str
    The type of the proxy. It can be "http", "socks4", "socks5".
proxy_address : str
    The address of the proxy.
username : str
    The username for the proxy, if any.
password : str
    The password for the proxy, if any.
"""


class KiranBot:
    """
    Kiran Bot.
    This class helps to initialize the bot class in order for the user to construct the bot.
    You can register callbacks or functions using the decorator `register` method.
    You can start pooling the bot using `run()` method from the bot class.
    Runtime is all dependent on this class, you can access the logger using `logger` attribute.
    Or you can setup your own logger using the internal logger.

    Parameters
    ----------
    token: str
        Your bot token.

    prefix: typing.Optional[typing.Union[str, typing.List[str]]] = "/"
        The prefix for the bot to respond to.

    logging_settings: typing.Optional[LoggerSettings] = None
        The logger settings for the bot.
    """

    def __init__(
        self,
        token: str,
        prefix: typing.Optional[typing.Union[str, typing.List[str]]] = "/",
        logging_settings: typing.Optional["LoggerSettings"] = None,
        proxy_settings: typing.Optional[LoadProxy] = None,
        polling_manager: typing.Optional["PollingManager"] = None,
    ) -> None:
        print(__banner__)
        self.proxy_settings = proxy_settings
        self.logger = KiranLogger(DefaultSettings)
        if logging_settings:
            self.logger = KiranLogger(logging_settings)
        self.logging_settings = logging_settings
        self.log = self.logger.log
        self.clean_logs = self.logger.clear_logs
        self._subscribed_events: typing.Dict[
            typing.Type["KiranEvent"],
            typing.List[
                typing.Callable[["KiranEvent"], typing.Awaitable[None]]
            ],
        ] = {}
        self.log("Event subscription storage initialized.", "debug")
        self.session = httpx.AsyncClient(
            base_url=f"https://api.telegram.org/bot{token}", timeout=999
        )
        self.log("Httpx session initialized.", "debug")
        if polling_manager is None:
            polling_manager = PollingManager(client=self, timeout=999)
            self.log(
                "Polling manager has been created. Was not defined by the developer.",
                "debug",
            )
        self._commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ] = {}
        self.log("All command subscription storage initialized.", "debug")
        self._slash_commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ] = {}
        self.log("Slash command subscription storage initialized.", "debug")
        self._prefix_commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ] = {}
        self.log("Prefix command subscription storage initialized.", "debug")
        self._common_commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ] = {}
        self.log("Common command subscription storage initialized.", "debug")
        self.polling_manager = polling_manager
        self.log("Polling manager has been initialized.", "debug")
        self._datetime_task: typing.Dict[
            datetime.datetime, typing.Callable[..., typing.Any]
        ] = {}
        self.log(
            "Task storage based on datetime execution initialized.", "debug"
        )
        self._cache: KiranCache = KiranCache()
        self.log("Cache has been initialized.", "debug")
        self._token = token
        self.log("Token has been taken into account.", "debug")
        self._prefix = prefix
        self.log("Prefix has been taken into account.", "debug")
        self.caller = KiranCaller(bot=self)
        self.log("Caller has been initialised for call jobs.", "debug")
        self.event_loop = asyncio.new_event_loop()
        self.log("Event loop has been defined.", "debug")
        self.log(
            "Bot Client has been initialized. Would now try to pool the bot to receive events.",
            "debug",
        )

    def command(
        self,
        name: str,
        description: str,
        scopes: typing.Optional[BotCommandScope] = BotCommandScopeDefault(),
        language_code: typing.Optional[typing.Union[LanguageCode, str]] = None,
    ) -> typing.Callable[
        [typing.Callable[["CommandContext"], typing.Awaitable[None]]],
        typing.Callable[["CommandContext"], typing.Awaitable[None]],
    ]:
        def decorator(
            func: typing.Callable[[CommandContext], typing.Awaitable[None]],
        ) -> typing.Callable[[CommandContext], typing.Awaitable[None]]:
            if hasattr(func, "__implements__"):
                if func.__implements__ == CommandImplements.GENERAL_COMMAND:  # type: ignore
                    self.log(
                        f"Command: {name} has been registered as a common command.",
                        "debug",
                    )
                    self._common_commands[
                        CallableBotCommandDetails(
                            name=name,
                            description=description,
                            scope=scopes,
                            language_code=language_code,
                        )
                    ] = func
                if func.__implements__ == CommandImplements.SLASH_COMMAND:  # type: ignore
                    self.log(
                        f"Command: {name} has been registered as a slash command.",
                        "debug",
                    )
                    self._slash_commands[
                        CallableBotCommandDetails(
                            name=name,
                            description=description,
                            scope=scopes,
                            language_code=language_code,
                        )
                    ] = func
                if func.__implements__ == CommandImplements.PREFIX_COMMAND:  # type: ignore
                    self.log(
                        f"Command: {name} has been registered as a prefix command.",
                        "debug",
                    )
                    self._prefix_commands[
                        CallableBotCommandDetails(
                            name=name,
                            description=description,
                            scope=scopes,
                            language_code=language_code,
                        )
                    ] = func
            else:
                raise CommandImplementationError(
                    message=f"Implementation method not specified. Command: {name}",
                    client=self,
                )
            return func

        return decorator

    async def _poll(self):
        await self.polling_manager.poll()

    async def _register_slash_commands(self) -> None:
        sorted_commands: typing.Dict[
            typing.Union[str, LanguageCode],
            typing.Dict[
                BotCommandScope, typing.List[CallableBotCommandDetails]
            ],
        ] = {}
        for command in self._slash_commands | self._common_commands:
            language_code = command.language_code or "default"
            command_scope = command.scope or BotCommandScopeDefault()

            if language_code not in sorted_commands:
                sorted_commands[language_code] = {}

            if command_scope not in sorted_commands[language_code]:
                sorted_commands[language_code][command_scope] = []

            sorted_commands[language_code][command_scope].append(command)

        for language_code, scopes in sorted_commands.items():
            for scope, commands in scopes.items():
                bot_commands = [
                    BotCommand(
                        command=cmd.name,
                        description=cmd.description,
                    )
                    for cmd in commands
                ]
                if language_code == "default":
                    await self.caller.set_commands(
                        bot_commands=bot_commands,
                        command_scope=scope,
                        language_code_iso=None,
                    )
                else:
                    await self.caller.set_commands(
                        bot_commands=bot_commands,
                        command_scope=scope,
                        language_code_iso=language_code,
                    )
        self.log(
            f"Populated {len(self._slash_commands)} slash commands to the bot.",
            "info",
        )
        self.log(
            f"Populated {len(self._prefix_commands)} prefix commands to the bot.",
            "info",
        )
        self.log(
            f"Populated {len(self._common_commands)} common commands to the bot.",
            "info",
        )
        await self.polling_manager.add_command_list(
            slash_commands=self._slash_commands,
            prefix_commands=self._prefix_commands,
            common_commands=self._common_commands,
        )

    async def _main_frame(self) -> None:
        try:
            self.log(
                "Light spark has been made! Registering the commands.", "info"
            )
            await self.event_loop.create_task(self._register_slash_commands())
            self.log("All commands are successfully engaged.", "info")
            await self._poll()
        except KeyboardInterrupt:
            self.log("The bot has been interrupted.", "debug")
            self.shutdown()

    def listen(
        self, event_type: typing.Type["KiranEvent"]
    ) -> typing.Callable[
        [typing.Callable[["KiranEvent"], typing.Awaitable[None]]],
        typing.Callable[["KiranEvent"], typing.Awaitable[None]],
    ]:
        def decorator(
            func: typing.Callable[[KiranEvent], typing.Awaitable[None]],
        ) -> typing.Callable[[KiranEvent], typing.Awaitable[None]]:
            if event_type not in self._subscribed_events:
                self._subscribed_events[event_type] = []
            self._subscribed_events[event_type].append(func)
            return func

        return decorator

    def task(self, task_type: typing.Literal["datetime", "loop"], time: typing.Union[datetime.datetime, int]):
        ...
        
    async def dispatch(self, event: "KiranEvent") -> None:
        for handler in self._subscribed_events.get(type(event), []):
            await handler(event)

    def shutdown(self) -> None:
        self.log("The shutdown event has been dispatched.", "debug")
        self.event_loop.stop()
        self.log("The event loop has been stopped.", "debug")
        self.log("The bot has been shutdown.", "info")

    def run(self) -> None:
        try:
            self.log("Trying to make a spark with the server.", "info")
            self.event_loop.create_task(self._main_frame())
            self.event_loop.run_forever()
        except KeyboardInterrupt:
            self.log("The bot has been interrupted.", "info")
            self.shutdown()
        except Exception as e:
            self.log(
                f"Error encountered while trying to run the event loop: {e}",
                "error",
            )
            self.log(f"Element Suspected: {inspect.findsource(e)}", "error")  # type: ignore
            self.shutdown()


def implements(
    method: ImplementationMethod,
) -> typing.Callable[[CommandFunction], CommandFunction]:
    def decorator(func: CommandFunction) -> CommandFunction:
        setattr(func, "__implements__", method)
        return func

    return decorator


