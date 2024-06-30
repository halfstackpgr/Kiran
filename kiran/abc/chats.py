from __future__ import annotations

import typing
import msgspec

if typing.TYPE_CHECKING:
    from .interactions import Location


class ChatPhoto(msgspec.Struct):
    """
    A class representing the chat photo.
    """

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
    """
    This object represents a location to which a chat is connected.
    """

    location: typing.Optional[Location]
    """
    The location to which the supergroup is connected. Can't be a live location.
    """
    address: typing.Optional[str] = None
    """
    Location address; 1-64 characters, as defined by the chat owner
    """
