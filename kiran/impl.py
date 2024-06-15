import typing

from .logger import LoggerSettings, KiranLogger, DefaultSettings
from .core.commands import CommandOption
class KiranContext:
    def __init__(
        self, 
        command_name: str, 
        command_description: str,
        callback: typing.Callable[..., typing.Any],
        options: typing.Sequence[CommandOption]
        ) -> None:
        self.command_name = command_name
        self.command_description = command_description
        self.callback = callback
        self.options = options
        
        pass

    def __repr__(self) -> str:
        return f"{self.command_name}: {self.command_description}"


LoadProxy = typing.Union[typing.List[typing.Mapping[str, str]], typing.Mapping[str, str]]
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
    This class helps to initialize the bot class in order for the user to consturct the bot.
    You can register callbacks or functions using the decorator `register` method.
    You can start pooling the bot using `run()` method from the bot class.
    Runtime is all dependant on this class, you can access the logger using `logger` attribute.
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
        self._token = token
        self._prefix = prefix
        self.proxy_settings = proxy_settings
        self.logger = KiranLogger(DefaultSettings)
        if logging_settings:
            self.logger = KiranLogger(logging_settings)
        self.logging_settings = logging_settings
        self.log = self.logger.log
        self.clean_logs = self.logger.clear_logs
        self.log("Bot Client has been initialized. Would now try to pool the bot to receive events.", "debug")

    def register(self, callback: typing.Callable[..., typing.Any]) -> typing.Callable[..., typing.Any]:
        """
        Register a callback function.

        Parameters
        ----------
        callback : typing.Callable[..., typing.Any]
            Callback function to be registered.

        Returns
        -------
        typing.Callable[..., typing.Any]
            The registered callback function.
        """
        self._callbacks[callback.__name__] = callback
        return callback