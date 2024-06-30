from __future__ import annotations

import typing
import msgspec


class File(msgspec.Struct):
    """
    This object represents a file ready to be downloaded. The file can be downloaded via the link `https://api.telegram.org/file/bot<token>/<file_path>`. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling [getFile](https://core.telegram.org/bots/api#getfile).
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    file_size: typing.Optional[int]
    """
    File size in bytes.
    """
    file_path: typing.Optional[str] = None
    """
    File path. Use `https://api.telegram.org/file/bot<token>/<file_path>` to get the file.
    """
