from __future__ import annotations

import typing
import datetime
import asyncio

from .errors import CommandImplementationError
from .core.poll import PollingManager
from .logger import LoggerSettings, KiranLogger, DefaultSettings
from .core.cache import KiranCache
from .components.context import CommandContext
from .abc.bots import BotCommandScope, BotCommandScopeDefault
from .components.commands import CallableBotCommandDetails, LanguageCode
from .components.commands import CommandImplements

CommandFunction = typing.Callable[[CommandContext], typing.Awaitable[None]]
ImplementationMethod = typing.Union[int, CommandImplements]

if typing.TYPE_CHECKING:
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
        if polling_manager is None:
            polling_manager = PollingManager(token, self, 100)
        self._commands: typing.Dict[
            CallableBotCommandDetails,
            typing.Callable[["CommandContext"], typing.Awaitable[None]],
        ] = {}
        self._slash_commands: typing.Dict[
            str, typing.Callable[["CommandContext"], typing.Awaitable[None]]
        ] = {}
        self._prefix_commands: typing.Dict[
            str, typing.Callable[["CommandContext"], typing.Awaitable[None]]
        ] = {}
        self._common_commands: typing.Dict[
            str, typing.Callable[["CommandContext"], typing.Awaitable[None]]
        ] = {}
        self.polling_manager = polling_manager
        self._datetime_task: typing.Dict[
            datetime.datetime, typing.Callable[..., typing.Any]
        ] = {}
        self._cache: KiranCache = KiranCache()
        self._token = token
        self._prefix = prefix
        self.log(
            "Bot Client has been initialized. Would now try to pool the bot to receive events.",
            "debug",
        )
        self.event_loop = asyncio.get_event_loop()

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
                self._commands[
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

    async def _poll(self) -> ...:
        await self.polling_manager.poll()

    async def _main_frame(self) -> None:
        await self.event_loop.run_until_complete(await self._poll())
        self.log("Polling has been started.", "info")
        for command in self._commands:
            self.log(f"Command {command.name} has been registered.", "debug")
        self.log("All commands have been registered.", "debug")

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

    async def dispatch(self, event: "KiranEvent") -> None:
        for handler in self._subscribed_events.get(type(event), []):
            await handler(event)

    def shutdown(self) -> None:
        self.log("The shutdown event has been dispatched.", "debug")
        self.event_loop.close()
        self.log("The bot has been shutdown.", "debug")

    def run(self) -> None:
        asyncio.run(main=self._main_frame())


def implements(
    method: ImplementationMethod,
) -> typing.Callable[[CommandFunction], CommandFunction]:
    def decorator(func: CommandFunction) -> CommandFunction:
        setattr(func, "__implements__", method)
        return func

    return decorator
