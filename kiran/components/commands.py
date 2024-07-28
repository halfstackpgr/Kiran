from __future__ import annotations

import enum
import msgspec
import typing
from ..abc.bots import BotCommandScope, BotCommandScopeDefault


class LanguageCode(enum.Enum):
    """
    A two-letter ISO 639-1 language code. If empty, commands will be
    applied to all users from the given scope, for whose language
    there are no dedicated commands
    """

    AFAR = "aa"
    ABKHAZIAN = "ab"
    AFRIKAANS = "af"
    AMHARIC = "am"
    ARABIC = "ar"
    ASSAMESE = "as"
    AYMARA = "ay"
    AZERBAIJANI = "az"
    BASHKIR = "ba"
    BYELORUSSIAN = "be"
    BULGARIAN = "bg"
    BIHARI = "bh"
    BISLAMA = "bi"
    BENGALI = "bn"
    TIBETAN = "bo"
    BRETON = "br"
    CATALAN = "ca"
    CORSICAN = "co"
    CZECH = "cs"
    WELSH = "cy"
    DANISH = "da"
    GERMAN = "de"
    BHUTANI = "dz"
    GREEK = "el"
    ENGLISH = "en"
    ESPERANTO = "eo"
    SPANISH = "es"
    ESTONIAN = "et"
    BASQUE = "eu"
    PERSIAN = "fa"
    FINNISH = "fi"
    FIJIAN = "fj"
    FAEROESE = "fo"
    FRENCH = "fr"
    FRISIAN = "fy"
    IRISH = "ga"
    SCOTS_GAELIC = "gd"
    GALICIAN = "gl"
    GUARANI = "gn"
    GUJARATI = "gu"
    HAUSA = "ha"
    HINDI = "hi"
    CROATIAN = "hr"
    HUNGARIAN = "hu"
    ARMENIAN = "hy"
    INTERLINGUA = "ia"
    INTERLINGUE = "ie"
    INUPIAK = "ik"
    INDONESIAN = "in"
    ICELANDIC = "is"
    ITALIAN = "it"
    HEBREW = "iw"
    JAPANESE = "ja"
    YIDDISH = "ji"
    JAVANESE = "jw"
    GEORGIAN = "ka"
    KAZAKH = "kk"
    GREENLANDIC = "kl"
    CAMBODIAN = "km"
    KANNADA = "kn"
    KOREAN = "ko"
    KASHMIRI = "ks"
    KURDISH = "ku"
    KIRGHIZ = "ky"
    LATIN = "la"
    LINGALA = "ln"
    LAOTHIAN = "lo"
    LITHUANIAN = "lt"
    LATVIAN = "lv"
    MALAGASY = "mg"
    MAORI = "mi"
    MACEDONIAN = "mk"
    MALAYALAM = "ml"
    MONGOLIAN = "mn"
    MOLDAVIAN = "mo"
    MARATHI = "mr"
    MALAY = "ms"
    MALTESE = "mt"
    BURMESE = "my"
    NAURU = "na"
    NEPALI = "ne"
    DUTCH = "nl"
    NORWEGIAN = "no"
    OCCITAN = "oc"
    AFAN_OROMO = "om"
    ORIYA = "or"
    PUNJABI = "pa"
    POLISH = "pl"
    PASHTO = "ps"
    PORTUGUESE = "pt"
    QUECHUA = "qu"
    RHAETO_ROMANCE = "rm"
    KIRUNDI = "rn"
    ROMANIAN = "ro"
    RUSSIAN = "ru"
    KINYARWANDA = "rw"
    SANSKRIT = "sa"
    SINDHI = "sd"
    SANGRO = "sg"
    SERBO_CROATIAN = "sh"
    SINGHALESE = "si"
    SLOVAK = "sk"
    SLOVENIAN = "sl"
    SAMOAN = "sm"
    SHONA = "sn"
    SOMALI = "so"
    ALBANIAN = "sq"
    SERBIAN = "sr"
    SISWANT = "ss"
    SESOTHO = "st"
    SUDANESE = "su"
    SWEDISH = "sv"
    SWAHILI = "sw"
    TAMIL = "ta"
    TELUGU = "te"
    TAJIK = "tg"
    THAI = "th"
    TIGRINYA = "ti"
    TURKMEN = "tk"
    TAGALOG = "tl"
    SETSWANA = "tn"
    TONGA = "to"
    TURKISH = "tr"
    TSONGA = "ts"
    TATAR = "tt"
    TWI = "tw"
    UKRAINIAN = "uk"
    URDU = "ur"
    UZBEK = "uz"
    VIETNAMESE = "vi"
    VOLAPUK = "vo"
    WOLOF = "wo"
    XHOSA = "xh"
    YORUBA = "yo"
    CHINESE = "zh"
    ZULU = "zu"


class CallableBotCommandDetails(msgspec.Struct, frozen=True):
    """
    Used for storing data related to bot command.

    Parameters
    ----------
    name: str
        The name of the command.
    description: typing.Optional[str] = None
        The description of the command.
    scope: typing.Optional["BotCommandScope"]
        The scope of the command.
    language_code: typing.Optional[typing.Union[LanguageCode, str]]
        The language code of the command.
    """

    name: str
    description: str
    scope: typing.Optional["BotCommandScope"] = BotCommandScopeDefault()
    language_code: typing.Optional[typing.Union[LanguageCode, str]] = None


class CommandImplements(enum.Enum):
    """
    Used to specify the type of command.
    """

    SLASH_COMMAND = 0
    """
    The command will be registered as a slash command, which is the general way of registering commands with respect to official Telegram command methods.
    """
    PREFIX_COMMAND = 1
    """
    The command will be registered as a prefix command. This is a feature implemented in Kiran, making it an undocumented feature with respect to the official Telegram documentation.
    """
    GENERAL_COMMAND = 3
    """
    The command will be registered as both a slash command and a prefix command.
    """
