from __future__ import annotations

import typing
import msgspec

from .media import PhotoSize


class User(msgspec.Struct):
    """
    This object represents a Telegram user or bot.
    """

    first_name: str
    """The user's first name."""
    id: typing.Optional[int] = None
    """
    Unique identifier for this user or bot.
    """
    is_bot: typing.Optional[bool] = False
    """
    `True`, if this user is a bot
    """
    last_name: typing.Optional[str] = None
    """
    User's or bot's last name
    """
    username: typing.Optional[str] = None
    """
    User's or bot's username
    """
    language_code: typing.Optional[str] = None
    """
    IETF language tag of the user's language
    """
    is_premium: typing.Optional[bool] = False
    """
    True, if this user is a Telegram Premium user
    """
    can_join_groups: typing.Optional[bool] = False
    """
    True, if the bot can be invited to groups
    """
    can_read_all_group_messages: typing.Optional[bool] = False
    """
    True, if the bot can read all messages in channels
    """
    supports_inline_queries: typing.Optional[bool] = False
    """
    True, if the bot supports inline queries
    """
    can_connect_to_business: typing.Optional[bool] = False
    """
    True, if the bot can be connected to a Telegram Business account to receive its messages.
    """


class SharedUser(msgspec.Struct):
    user_id: int
    """
    Unique identifier for this user or bot.
    """

    first_name: typing.Optional[str] = None
    """
    User's or bot's first name
    """
    last_name: typing.Optional[str] = None
    """
    User's or bot's last name
    """
    username: typing.Optional[str] = None
    """
    User's or bot's username
    """
    photo: typing.Optional[PhotoSize] = None
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
