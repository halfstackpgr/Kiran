import typing
import datetime
import asyncio
import pathlib
import aiohttp

from .core.events import KiranEvent
from .core.cache import KiranCache
from .logger import LoggerSettings, KiranLogger, DefaultSettings
from .core.methods import TelegramMethodName

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
        logging_settings: typing.Optional[LoggerSettings] = None,
        proxy_settings: typing.Optional[LoadProxy] = None,
    ) -> None:
        self._callbacks: typing.Dict[str, typing.Callable[..., typing.Any]] = {}
        self._datetime_task: typing.Dict[
            datetime.datetime, typing.Callable[..., typing.Any]
        ] = {}
        self._subscribed_events: typing.List[KiranEvent] = []
        self._cache: KiranCache = KiranCache()
        self._token = token
        self._prefix = prefix
        self.proxy_settings = proxy_settings
        self.logger = KiranLogger(DefaultSettings)
        if logging_settings:
            self.logger = KiranLogger(logging_settings)
        self.logging_settings = logging_settings
        self.log = self.logger.log
        self.clean_logs = self.logger.clear_logs
        self.log(
            "Bot Client has been initialized. Would now try to pool the bot to receive events.",
            "debug",
        )
        self.event_loop = asyncio.get_event_loop()

    async def get_url_session(self, method: TelegramMethodName):
        """
        Get a url session to make request to a web-url.
        """
        async with aiohttp.ClientSession(
            base_url="https://api.telegram.org"
        ) as session:
            ls = await session.get(f"/bot{self._token}/{method}")
            print(await ls.read())

    def register(self): ...

    def listen(self): ...

    def shutdown(self) -> None:
        self.log("The shutdown event has been dispatched.", "debug")
        self.event_loop.close()
        self.log("The bot has been shutdown.", "debug")

    def load_plugins_from(
        self, path: typing.Union[str, pathlib.Path]
    ) -> None: ...

    def load_plugin(self, plugin: typing.Union[str, pathlib.Path]) -> None: ...

    def unload_plugin(
        self, plugin: typing.Union[str, pathlib.Path]
    ) -> None: ...

    def execute(self, code: str) -> None: ...

    def cache(self) -> KiranCache:
        return self._cache

    def call(self) -> None: ...
