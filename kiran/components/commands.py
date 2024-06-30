from __future__ import annotations

import enum
import msgspec
import typing
from ..abc.bots import BotCommandScope, BotCommandScopeDefault


class ParseMode(enum.Enum):
    """
    The Bot API supports basic formatting for messages. You can use bold, italic, underlined, strikethrough, spoiler text, block quotations as well as inline links and pre-formatted code in your bots' messages. Telegram clients will render them accordingly. You can specify text entities directly, or use markdown-style or HTML-style formatting.

    Note that Telegram clients will display an alert to the user before opening an inline link ('Open this link?' together with the full URL).

    Message entities can be nested, providing following restrictions are met:
    - If two entities have common characters, then one of them is fully contained inside another.
    - bold, italic, underline, strikethrough, and spoiler entities can contain and can be part of any other entities, except pre and code.
    - blockquote and expandable_blockquote entities can't be nested.
    - All other entities can't contain each other.

    Links `tg://user?id=<user_id>` can be used to mention a user by their identifier without using a username. Please note:

    These links will work only if they are used inside an inline link or in an inline keyboard button. For example, they will not work, when used in a message text.
    Unless the user is a member of the chat where they were mentioned, these mentions are only guaranteed to work if the user has contacted the bot in private in the past or has sent a callback query to the bot via an inline button and doesn't have Forwarded Messages privacy enabled for the bot.
    """

    MARKDOWN = "Markdown"
    """
    Note
    ----
    
    - Entities must not be nested, use parse mode MarkdownV2 instead.
    - There is no way to specify “underline”, “strikethrough”, “spoiler”, “blockquote”, “expandable_blockquote” and “custom_emoji” entities, use parse mode MarkdownV2 instead.
    - To escape characters `'_', '*', '`', '['` outside of an entity, prepend the characters '\' before them.
    - Escaping inside entities is not allowed, so entity must be closed first and reopened again: use _snake__case_ for italic snake_case and *2***2=4* for bold 2*2=4.
    """
    HTML = "HTML"
    """
    Note
    ----
    
    - Only the tags mentioned above are currently supported.
    - All <, > and & symbols that are not a part of a tag or an HTML entity must be replaced with the corresponding HTML entities (< with &lt;, > with &gt; and & with &amp;).
    - All numerical HTML entities are supported.
    - The API currently supports only the following named HTML entities: &lt;, &gt;, &amp; and &quot;.
    - Use nested pre and code tags, to define programming language for pre entity.
    - Programming language can't be specified for standalone code tags.
    - A valid emoji must be used as the content of the tg-emoji tag. The emoji will be shown instead of the custom emoji in places where a custom emoji cannot be displayed (e.g., system notifications) or if the message is forwarded by a non-premium user. It is recommended to use the emoji from the emoji field of the custom emoji sticker.
    - Custom emoji entities can only be used by bots that purchased additional usernames on Fragment.
    """
    MARKDOWN_V2 = "MarkdownV2"
    """
    Note
    ----
    
    - Any character with code between 1 and 126 inclusively can be escaped anywhere with a preceding '\' character, in which case it is treated as an ordinary character and not a part of the markup. This implies that '\' character usually must be escaped with a preceding '\' character.
    - Inside pre and code entities, all '`' and '\' characters must be escaped with a preceding '\' character.
    - Inside the (...) part of the inline link and custom emoji definition, all ')' and '\' must be escaped with a preceding '\' character.
    - In all other places characters `'_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!'` must be escaped with the preceding character '\'.
    - In case of ambiguity between italic and underline entities __ is always greadily treated from left to right as beginning or end of an underline entity, so instead of ___italic underline___ use ___italic underline_**__, adding an empty bold entity as a separator.
    - A valid emoji must be provided as an alternative value for the custom emoji. The emoji will be shown instead of the custom emoji in places where a custom emoji cannot be displayed (e.g., system notifications) or if the message is forwarded by a non-premium user. It is recommended to use the emoji from the emoji field of the custom emoji sticker.
    - Custom emoji entities can only be used by bots that purchased additional usernames on Fragment.
    """


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
