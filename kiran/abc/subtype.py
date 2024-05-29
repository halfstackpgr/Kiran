import msgspec
import typing
from .enums import StickerType, MaskPositionPoint


class Location(msgspec.Struct):
    latitude: float
    """
    Latitude as defined by sender.
    """
    longitude: float
    """
    Longitude as defined by sender.
    """
    horizontal_accuracy: typing.Optional[float]
    """
    The radius of uncertainty for the location, measured in meters; 0-1500.
    """
    live_period: typing.Optional[int]
    """
    Period in seconds for which the location can be updated, should be between 60 and 86400.
    """
    heading: typing.Optional[int]
    """
    Direction in which user is moving, in degrees; must be between 1 and 360 if specified.
    """
    proximity_alert_radius: typing.Optional[int]
    """
    The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
    """

class MaskPosition(msgspec.Struct):
    """
    Describes the position on faces where a mask should be placed by default.
    """

    point: MaskPositionPoint
    """
    The part of the face relative to which the mask should be placed. One of `forehead`, `eyes`, `mouth`, or `chin`.
    """
    x_shift: float
    """
    Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
    """
    y_shift: float
    """
    Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
    """
    scale: float
    """
    Mask scaling coefficient. For example, 2.0 means double size.
    """


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
    file_path: typing.Optional[str]
    """
    File path. Use `https://api.telegram.org/file/bot<token>/<file_path>` to get the file.
    """


class PhotoSize(msgspec.Struct):
    """
    A class representing the photo size.
    """

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
    file_size: typing.Optional[int]
    """
    File size in bytes.
    """


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


class BirthDate(msgspec.Struct):
    """
    Describes the birthdate of a user.
    """

    day: int
    """
    Day of birth, from 1 to 31.
    """
    month: int
    """
    Month of birth, from 1 to 12.
    """
    year: int
    """
    Year of birth, from 1 to 9999.
    """


class Sticker(msgspec.Struct):
    """
    Represents a telegram sticker.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    type: StickerType
    """
    Type of the sticker, currently one of `regular`, `mask`, `custom_emoji`. The type of the sticker is independent from its format, which is determined by the fields is_animated and is_video.
    """
    width: int
    """
    Sticker width
    """
    height: int
    """
    Sticker height
    """
    is_animated: bool
    """
    True, if the sticker is animated
    """
    is_video: bool
    """
    True, if the sticker is a video sticker
    """
    thumbnail: typing.Optional[PhotoSize]
    """
    Sticker thumbnail in the .WEBP or .JPG format
    """
    emoji: typing.Optional[str]
    """
    Emoji associated with the sticker
    """
    set_name: typing.Optional[str]
    """
    Name of the sticker set to which the sticker belongs
    """
    premium_animation: typing.Optional[File]
    """
    For premium regular stickers, premium animation for the sticker
    """
    mask_position: typing.Optional[MaskPosition]
    """
    For mask stickers, the position where the mask should be placed
    """
    custom_emoji_id: typing.Optional[str]
    """
    For custom emoji stickers, unique identifier of the custom emoji
    """
    needs_repainting: typing.Optional[bool]
    """
    True, if the sticker must be repainted to a text color
    """
    file_size: typing.Optional[int]
    """
    File size in bytes
    """


class BusinessIntro(msgspec.Struct):
    """
    Contains information about the start page settings of a Telegram Business account.
    """

    title: typing.Optional[str]
    """
    Title text of the business intro
    """
    message: typing.Optional[str]
    """
    Message text of the business intro
    """
    sticker: typing.Optional[Sticker]
    """
    Sticker of the business intro
    """

class BusinessLocation(msgspec.Struct):
    """
    Contains information about the location of a Telegram Business account.
    """
    address: str
    """
    Address of the business.
    """
    location: typing.Optional[Location]
    """
    Location of the business.
    """
    

class BusinessOpeningHoursInterval(msgspec.Struct):
    """
    Describes an interval of time during which a business is open.
    """
    opening_minute: int
    """
    The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 * 24 * 60
    """
    closing_minute: int
    """
    The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 * 24 * 60
    """
class BusinessOpeningHours(msgspec.Struct):
    """
    Contains information about the opening hours of a Telegram Business account.
    """
    time_zone_name: typing.List[str]
    """
    Unique name of the time zone for which the opening hours are defined
    """
    opening_hours: typing.Optional[typing.List[BusinessOpeningHoursInterval]]
    
class ReactionTypeEmoji(msgspec.Struct):
    """
    The reaction is based on an emoji.
    """
    type: str
    """
    The type of the emoji. Always "emoji"
    """
    emoji: str
    """
    Reaction emoji. Currently, it can be one of "👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"
    """

class ReactionTypeCustomEmoji(msgspec.Struct):
    """
    The reaction is based on a custom emoji.
    """
    type: str
    """
    The type of the emoji. Always "custom_emoji"
    """
    custom_emoji_id: str
    """
    Custom emoji identifier
    """
