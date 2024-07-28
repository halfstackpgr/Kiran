from __future__ import annotations

import enum


class ChatType(enum.Enum):
    """Enum representing a chat type."""

    PRIVATE = "private"
    """Represents a private chat."""
    GROUP = "group"
    """Represents a group chat."""
    SUPER_GROUP = "supergroup"
    """Represents a supergroup chat."""
    CHANNEL = "channel"
    """Represents a channel chat."""


class StickerType(enum.Enum):
    """Enum representing a sticker type."""

    REGULAR = "regular"
    """Represents a standard sticker."""
    MASK = "mask"
    """Represents a mask sticker."""
    CUSTOM_EMOJI = "custom_emoji"
    """Represents a custom emoji sticker."""


class MaskPositionPoint(enum.Enum):
    """Enum representing a mask position point."""

    FOREHEAD = "forehead"
    """Represents a mask position point on the forehead."""
    EYES = "eyes"
    """Represents a mask position point on the eyes."""
    MOUTH = "mouth"
    """Represents a mask position point on the mouth."""
    CHIN = "chin"
    """Represents a mask position point on the chin."""


class MessageOriginType(enum.Enum):
    """Enum representing a message origin type."""

    USER = "user"
    """Represents a message origin type of a user."""
    HIDDEN_USER = "hidden_user"
    """Represents a message origin type of a hidden user."""
    CHAT = "chat"
    """Represents a message origin type of a chat."""
    CHANNEL = "channel"
    """Represents a message origin type of a channel."""


class MessageEntityType(enum.Enum):
    """Type of the message entity."""

    MENTION = "mention"
    """A mention: `@username`."""
    HASHTAG = "hashtag"
    """A hashtag: `#hashtag`."""
    CASHTAG = "cashtag"
    """A cashtag: `$USD`."""
    BOT_COMMAND = "bot_command"
    """A bot command: `/start@jobs_bot`."""
    URL = "url"
    """A URL: `https://telegram.org`."""
    EMAIL = "email"
    """An email address: `do-not-reply@telegram.org`."""
    PHONE_NUMBER = "phone_number"
    """A phone number: `+1-212-555-0123`."""
    BOLD = "bold"
    """Bold Text"""
    ITALIC = "italic"
    """Italic Text"""
    UNDERLINE = "underline"
    """Underline Text"""
    STRIKETHROUGH = "strikethrough"
    """Strikethrough Text"""
    SPOILER = "spoiler"
    """Spoiler Text"""
    BLOCK_QUOTE = "blockquote"
    """Blockquote Text"""
    EXPANDABLE_BLOCK_QUOTE = "expandable_blockquote"
    """Expandable Blockquote Text"""
    CODE = "code"
    """Code Text"""
    PRE = "pre"
    """Pre Text"""
    TEXT_LINK = "text_link"
    """Text Link"""
    TEXT_MENTION = "text_mention"
    """Text Mention"""
    CUSTOM_EMOJI = "custom_emoji"
    """Custom Emoji"""


class PollType(enum.Enum):
    """Enum representing a poll type."""

    QUIZ = "quiz"
    """Represents a quiz poll."""
    POLL = "poll"
    """Represents a regular poll."""


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
