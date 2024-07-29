"""Information about the package."""

from __future__ import annotations

import sys
import typing

from colorama import Fore

__author__: typing.Final = "halfstackpgr"
__email__: typing.Final = "halfstackpgr@gmail.com"
__version__: typing.Final = "0.0.1"
__telegram_api__: typing.Final = "Bot API 7.7"
__github_url__: typing.Final = "https://github.com/halfstackpgr/kiran"
__pypi_url__: typing.Final = "https://pypi.org/project/kiran"
__short_description__: typing.Final = (
    "A raged framework for wrapping up your telegram bot."
)

__banner__: typing.Final = f"""
    {Fore.LIGHTRED_EX}oooo    oooo o8o{Fore.RESET}                                    {Fore.CYAN}Author:{Fore.RESET} {__author__}
    {Fore.LIGHTRED_EX}`888   .8P'  `"'{Fore.RESET}                                    {Fore.CYAN}Email:{Fore.RESET} {__email__}
    {Fore.WHITE}888  d8'    oooo  oooo d8b  .oooo.   ooo. .oo.{Fore.RESET}      {Fore.CYAN}Python Version:{Fore.RESET} {sys.version[:6]}
    {Fore.BLUE}88888[      `888  `8888P   `P  )88b  `888P"Y88b{Fore.RESET}     {Fore.CYAN}Wrapper Version:{Fore.RESET} {__version__}
    {Fore.WHITE}888`88b.     888   888      .oP"888   888   888{Fore.RESET}     {Fore.CYAN}Telegram API:{Fore.RESET} {__telegram_api__}
    {Fore.LIGHTGREEN_EX}888  `88b.   888   888     d8(  888   888   888{Fore.RESET}     {Fore.CYAN}Github URL:{Fore.RESET} halfstackpgr/kiran
    {Fore.LIGHTGREEN_EX}o888o  o888o o888o d888b   `Y8888o   o888o o888o{Fore.RESET}    {Fore.MAGENTA}⭐ The Repo if you find it helpful.{Fore.RESET}

                    {__short_description__}
"""
