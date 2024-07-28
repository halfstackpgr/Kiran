from __future__ import annotations

import typing

import msgspec

if typing.TYPE_CHECKING:
    from .interactions import Location


class ChatPhoto(msgspec.Struct):
    """A class representing the chat photo."""

    small_file_id: str
    """
    File identifier of small `(160x160)` chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    """
    small_file_unique_id: str
    """
    Unique file identifier of small `(160x160)` chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    big_file_id: str
    """
    File identifier of big `(640x640)` chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    """
    big_file_unique_id: str
    """
    Unique file identifier of big `(640x640)` chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """


class ChatLocation(msgspec.Struct):
    """This object represents a location to which a chat is connected."""

    location: typing.Optional[Location]
    """
    The location to which the supergroup is connected. Can't be a live location.
    """
    address: typing.Optional[str] = None
    """
    Location address; 1-64 characters, as defined by the chat owner
    """


class ChatAdministratorRights(msgspec.Struct):
    """Represents the rights of an administrator in a chat."""

    is_anonymous: bool
    """
    True, if the user's presence in the chat is hidden
    """
    can_manage_chat: bool
    """
    True, if the administrator can change chat title, photo and other settings
    """
    can_delete_messages: bool
    """
    True, if the administrator can delete messages of other users
    """
    can_manage_video_chat: bool
    """
    True, if the administrator can manage voice chat
    """
    can_restrict_members: bool
    """
    True, if the administrator can restrict, ban or unban chat members
    """
    can_promote_members: bool
    """
    True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that were directly or indirectly promoted by them
    """
    can_change_info: bool
    """
    True, if the administrator can change chat title, photo and other settings
    """
    can_invite_users: bool
    """
    True, if the administrator can invite new users to the chat
    """
    can_post_stories: bool
    """
    True, if the user is allowed to create, rename, close, and reopen forum topics
    """
    can_edit_stories: bool
    """
    True, if the administrator can edit messages of other users
    """
    can_delete_stories: bool
    """
    True, if the administrator can delete stories posted by other users
    """
    can_post_messages: bool
    """
    True, if the administrator can post messages from the chat
    """
    can_edit_messages: bool
    """
    True, if the administrator can edit messages of other users
    """
    can_pin_messages: bool
    """
    True, if the administrator can pin messages
    """
    can_manage_topics: bool
    """
    True, if the user is allowed to create, rename, close, and reopen forum topics
    """


class ChatPermissions(msgspec.Struct):
    """Describes actions that a non-administrator user is allowed to take in a chat."""

    can_send_messages: bool
    """
    True, if the user is allowed to send text messages, contacts, locations and venues
    """
    can_send_audios: bool
    """
    True, if the user is allowed to send audios
    """
    can_send_documents: bool
    """
    True, if the user is allowed to send documents
    """
    can_send_photos: bool
    """
    True, if the user is allowed to send photos
    """
    can_send_videos: bool
    """
    True, if the user is allowed to send videos
    """
    can_send_video_notes: bool
    """
    True, if the user is allowed to send video notes
    """
    can_send_voice_notes: bool
    """
    True, if the user is allowed to send voice notes
    """
    can_send_polls: bool
    """
    True, if the user is allowed to send polls
    """
    can_send_other_messages: bool
    """
    True, if the user is allowed to send animations, games, stickers and use inline bots
    """
    can_add_web_page_previews: bool
    """
    True, if the user is allowed to add web page previews to their messages
    """
    can_change_info: bool
    """
    True, if the user is allowed to change the chat title, photo and other settings
    """
    can_invite_users: bool
    """
    True, if the user is allowed to invite new users to the chat
    """
    can_pin_messages: bool
    """
    True, if the user is allowed to pin messages
    """
    can_manage_topics: bool
    """
    True, if the user is allowed to create, rename, close, and reopen forum topics
    """
