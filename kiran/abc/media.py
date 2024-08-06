from __future__ import annotations

import typing

import msgspec


class PhotoSize(msgspec.Struct):
    """A class representing the photo size."""

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    width: int
    """
    Photo width
    """
    height: int
    """
    Photo height
    """
    file_size: typing.Optional[int] = None
    """
    File size in bytes.
    """


class Animation(msgspec.Struct):
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound)."""

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    width: int
    """
    Video width as defined by sender
    """
    height: int
    """
    Video height as defined by sender
    """
    duration: int
    """
    Duration of the video in seconds as defined by sender
    """
    thumbnail: typing.Optional[PhotoSize]
    """
    Animation thumbnail as defined by sender.
    """
    file_name: typing.Optional[str] = None
    """
    Original animation filename as defined by sender
    """
    mime_type: typing.Optional[str] = None
    """
    MIME type of the file as defined by sender
    """
    file_size: typing.Optional[int] = None
    """
    File size in bytes.
    """


class Audio(msgspec.Struct):
    """This object represents an audio file to be treated as music by the Telegram clients."""

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    duration: int
    """
    Duration of the audio in seconds as defined by sender
    """
    performer: typing.Optional[str] = None
    """
    Performer of the audio as defined by sender or by audio tags
    """
    title: typing.Optional[str] = None
    """
    Title of the audio as defined by sender or by audio tags
    """
    file_name: typing.Optional[str] = None
    """
    Original filename as defined by sender
    """
    mime_type: typing.Optional[str] = None
    """
    MIME type of the file as defined by sender
    """
    file_size: typing.Optional[int] = None
    """
    File size in bytes
    """
    thumbnail: typing.Optional[PhotoSize] = None
    """
    Thumbnail of the album cover to which the music file belongs
    """


class Document(msgspec.Struct):
    """A general file (as opposed to photos, voice messages and audio files)."""

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    thumbnail: typing.Optional[PhotoSize] = None
    """
    Document thumbnail as defined by sender
    """
    file_name: typing.Optional[str] = None
    """
    Original filename as defined by sender
    """
    mime_type: typing.Optional[str] = None
    """
    MIME type of the file as defined by sender
    """
    file_size: typing.Optional[int] = None
    """
    File size in bytes
    """


class Video(msgspec.Struct):
    """This object represents a video file."""

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    width: int
    """
    Video width as defined by sender
    """
    height: int
    """
    Video height as defined by sender
    """
    duration: int
    """
    Duration of the video in seconds as defined by sender
    """
    thumbnail: typing.Optional[PhotoSize]
    """
    Video thumbnail
    """
    file_name: typing.Optional[str] = None
    """
    Original filename as defined by sender
    """
    mime_type: typing.Optional[str] = None
    """
    MIME type of the file as defined by sender
    """
    file_size: typing.Optional[int] = None
    """
    File size in bytes
    """


class VideoNote(msgspec.Struct):
    """This object represents a [video message](https://telegram.org/blog/video-messages-and-telescope) (available in Telegram apps as of [v.4.0](https://telegram.org/blog/video-messages-and-telescope))."""

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    length: int
    """
    Video width and height (diameter of the video message) as defined by sender
    """
    duration: int
    """
    Duration of the video in seconds as defined by sender
    """
    thumbnail: typing.Optional[PhotoSize]
    """
    Video thumbnail
    """
    file_size: typing.Optional[int] = None
    """
    File size in bytes
    """


class Voice(msgspec.Struct):
    """This object represents a voice note."""

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    duration: int
    """
    Duration of the audio in seconds as defined by sender
    """
    mime_type: typing.Optional[str] = None
    """
    MIME type of the file as defined by sender
    """
    file_size: typing.Optional[int] = None
    """
    File size in bytes
    """
