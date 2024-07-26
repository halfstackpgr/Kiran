from __future__ import annotations

import datetime
import pathlib
import sys
import typing

import colorama

LoggingType = typing.Literal["info", "warning", "debug", "error"]
"""
Logging types that can be used in Kiran Logger.

Types
-----
info: 
    Basic information-only. Color Green would be used.
warning:
    Warning information. Color Red would be used.
debug: 
    Debug information. Color Light Black would be used to show debugging logs.
error:  
    Error information. Color yellow would be used to show error. No complete tracebacks would be shown.
"""

LoggingLevel = typing.Literal["basic", "standard", "debug", "no-error"]
"""
Levels of logging defined as per Kiran's package.

Levels
------
basic:
    Only basic logging will be displayed.
    Basic connections and errors would be displayed. No "debug" or "warning" will be displayed. [LoggingType](kiran.logger.LoggingType) would be supported.
debug: Only debug logging will be displayed.
    Each and everything happening in the bot would get displayed. Each connection and everything happening in the bot would get displayed. [LoggingType](kiran.logger.LoggingType) would be supported.
no-error: 
    Only non-error logging will be displayed.
    Meant to suppress the errors the bot might encounter.
"""


class LoggerSettings:
    """
    Logger settings, this has to be setup by the user for internal logging in Kiran.
    This would be able to log everything that are generated as `Exceptions` in Kiran.

    Parameters
    ----------
    level : typing.Union[typing.Literal["info", "warning", "debug", "error", "no-error"], LoggingType]
        Logging level, default is basic
    log_file : typing.Optional[typing.Union[str, pathlib.Path]]
        Logging file, default is None
    clean_logs : typing.Optional[bool]
        Weather to use clean logging, default is True. This would use the system level module to display logs.
    """

    def __init__(
        self,
        level: LoggingLevel,
        log_file: typing.Optional[typing.Union[str, pathlib.Path]] = None,
        clean_logs: typing.Optional[bool] = True,
        enable_colors: typing.Optional[bool] = True,
    ) -> None:
        self.level = level
        self.log_file = log_file
        self.clean_logs = clean_logs
        self.enable_colors = enable_colors

    def __repr__(self) -> str:
        return f"\nLevel: {self.level}\nLog File: {self.log_file}\nClean Logs: {self.clean_logs}\nEnable Colors: {self.enable_colors}"

    def __str__(self) -> str:
        return self.__repr__()


DefaultSettings = LoggerSettings("basic", None, True, True)


class KiranLogger:
    """
    A customized logger for Kiran Telegram Wrapper.

    Parameters
    ----------
    settings : LoggerSettings
        Logger settings, this has to be setup by the user for internal logging in Kiran.
    """

    def __init__(self, settings: LoggerSettings = DefaultSettings) -> None:
        self.log_settings = settings
        self.log_file = None
        self.file_session = None
        self.clean_logs = False
        self.enable_colors = False
        if self.log_settings:
            if self.log_settings.log_file is not None:
                if isinstance(self.log_settings.log_file, str):
                    self.log_file = pathlib.Path(self.log_settings.log_file)
                if isinstance(self.log_settings.log_file, pathlib.Path):
                    self.log_file = self.log_settings.log_file
                else:
                    raise ValueError(
                        "Invalid log file type. Must be str or an instance of pathlib.Path"
                    )
                with open(self.log_file, mode="a") as f:
                    self.file_session = f

            self.clean_logs = self.log_settings.clean_logs
            self.enable_colors = self.log_settings.enable_colors
        else:
            raise ValueError("No logger settings provided")
        self.log(f"Logger initialized with settings: {settings}", "debug")

    def __del__(self):
        if self.file_session:
            self.file_session.close()

    def __str__(self):
        return str(self.log_file) if self.log_file else ""

    def __repr__(self):
        return repr(self.log_file) if self.log_file else ""

    def _get_date(self) -> str:
        """
        Gets the current date and time.

        Returns
        -------
        str
            The current date and time.
        """
        return f"{colorama.Fore.CYAN}{datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')}{colorama.Fore.RESET}"

    def _add_color(self, message: str, log_type: LoggingType) -> str:
        """
        Adds color to the message.

        Parameters
        ----------
        message : str
            The message to be logged
        log_type : LoggingType
            The log type to be used

        Returns
        -------
        str
            The message with color added.
        """
        log_color = colorama.Fore.WHITE
        if log_type == "info":
            log_color = colorama.Fore.GREEN
        if log_type == "warning":
            log_color = colorama.Fore.RED
        if log_type == "debug":
            log_color = colorama.Fore.LIGHTBLACK_EX
        if log_type == "error":
            log_color = colorama.Fore.YELLOW
        if self.enable_colors:
            return f"Kiran: {self._get_date()} - {log_type.capitalize()} - {log_color}{message}{colorama.Fore.RESET}"
        else:
            return message

    def _save_logs(self, message: str) -> None:
        """
        Saves the log.

        Parameters
        ----------
        message : str
            The message to be logged
        """
        if self.file_session:
            self.file_session.write(f"{self._get_date()} - {message}\n")

    def _check_to_log(self, log_type: LoggingType) -> bool:
        """
        Check if the log type should be logged.

        Parameters
        ----------
        log_type : LoggingType
            The log type to check.

        Returns
        -------
        bool
            True if the log type should be logged, False otherwise.
        """
        map_of_logging = {
            "no-error": [],
            "basic": ["info", "warning"],
            "standard": ["info", "warning", "error"],
            "debug": ["info", "warning", "debug", "error"],
        }
        set_level = typing.cast(LoggingLevel, self.log_settings.level)
        pick_theme = map_of_logging.get(set_level)
        return log_type in pick_theme if pick_theme is not None else False

    def _clean_log(self, message: str, log_type: LoggingType) -> None:
        """
        Logging in a clean manner using base system module.

        Parameters
        ----------
        message : str
            The message to be logged
        log_type : LoggingType
            The log type to be used
        """
        if self.enable_colors:
            sys.stdout.write(f"{self._add_color(message, log_type)}\n")
        else:
            sys.stdout.write(f"{message}\n")

    def log(self, message: str, log_type: LoggingType) -> None:
        """
        A basic log function provided with the Kiran Logger. Can be used for internal logging as well as external logging too.

        Parameters
        ----------
        message : str
            The message to be logged
        log_type : LoggingType
            The log type to be used
        """
        if self._check_to_log(log_type):
            if self.clean_logs:
                self._clean_log(message, log_type)
            else:
                print(self._add_color(message, log_type))
        else:
            pass

    def clear_logs(self) -> None:
        """Clears the terminal."""
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()
