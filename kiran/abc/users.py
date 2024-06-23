import typing
import msgspec

from .media import PhotoSize


class User(msgspec.Struct):
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

    last_name: typing.Optional[str]
    """
    User's or bot's last name
    """
    username: typing.Optional[str]
    """
    User's or bot's username
    """
    language_code: typing.Optional[str]
    """
    IETF language tag of the user's language
    """
    is_premium: bool
    """
    True, if this user is a Telegram Premium user
    """

    can_join_groups: bool
    """
    True, if the bot can be invited to groups
    """
    can_join_groups: bool
    """
    True, if privacy mode is disabled for the bot
    """
    can_read_all_group_messages: bool
    """
    True, if the bot can read all messages in channels
    """
    supports_inline_queries: bool
    """
    True, if the bot supports inline queries
    """
    can_connect_to_business: bool
    """
    True, if the bot can be connected to a Telegram Business account to receive its messages.
    """


class SharedUser(msgspec.Struct):
    user_id: int
    """
    Unique identifier for this user or bot.
    """

    first_name: typing.Optional[str]
    """
    User's or bot's first name
    """
    last_name: typing.Optional[str]
    """
    User's or bot's last name
    """
    username: typing.Optional[str]
    """
    User's or bot's username
    """
    photo: typing.Optional[PhotoSize]
    """
    User's or bot's profile photo
    """


class UsersShared(msgspec.Struct):
    """
    Contains information about the users whose identifiers were shared.
    """

    request_id: int
    """
    Identifier of the request
    """
    users: typing.List[SharedUser]
    """
    Information about users shared with the bot.
    """
