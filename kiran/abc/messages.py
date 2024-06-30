from __future__ import annotations

import msgspec
import typing


from .users import User
from ..core.enums import MessageEntityType


class MessageEntity(msgspec.Struct):
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.
    """

    type: MessageEntityType
    """
    The entity type
    """
    offset: int
    """
    Offset in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length) to the start of the entity
    """
    length: int
    """
    Length of the entity in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length)
    """
    url: typing.Optional[str] = None
    """
    Optional. For `text_link` only, URL that will be opened after user taps on the text
    """
    user: typing.Optional[User] = None
    """
    For “text_mention” only, the mentioned user
    """
    language: typing.Optional[str] = None
    """
    For “pre” only, the programming language of the entity
    """
    custom_emoji_id: typing.Optional[str] = None
    """
    For `custom_emoji` only, unique identifier of the custom emoji.
    """


class TextQuote(msgspec.Struct):
    text: str
    """
    Text of the quoted part of a message that is replied to by the given message.
    """
    entities: typing.Optional[typing.List[MessageEntity]]
    """ Special entities that appear in the quote. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are kept in quotes. """
    position: int
    """
    Approximate quote position in the original message in UTF-16 code units as specified by the sender
    """
    is_manual: bool
    """
    True, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server.
    """
