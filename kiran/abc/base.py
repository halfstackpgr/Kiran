import msgspec
from .enums import ChatType


class BaseUser(msgspec.Struct):
    """
    This object represents a Telegram user or bot.
    """

    id: int
    """
    Unique identifier for this user or bot.
    """
    is_bot: bool
    """
    `True`, if this user is a bot
    """
    first_name: str
    """The user's first name."""


class BaseChat(msgspec.Struct):
    """
    This object represents a chat.
    """

    id: int
    """
    Unique identifier for this chat.
    """

    type: ChatType
    """
    Type of chat, can be either 'private', 'group', 'supergroup' or 'channel'.
    """
