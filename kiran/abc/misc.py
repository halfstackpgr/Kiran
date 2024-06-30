from __future__ import annotations

import typing
import msgspec

from .interactions import Location
from ..core.enums import MaskPositionPoint


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


class LinkPreviewOptions(msgspec.Struct):
    """
    Describes the options used for link preview generation.

    ---
    Reference: [telegram.LinkPreviewOptions](https://core.telegram.org/bots/api#linkpreviewoptions)
    """

    is_disabled: typing.Optional[bool]
    """
    True, if the link preview is disabled
    """
    url: typing.Optional[str] = None
    """
    URL to use for the link preview. If empty, then the first URL found in the message text will be used.
    """
    prefer_small_media: typing.Optional[bool] = False
    """
    True, if the media in the link preview is supposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview.
    """
    prefer_large_media: typing.Optional[bool] = False
    """
    True, if the media in the link preview is supposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview.
    """
    show_above_text: typing.Optional[bool] = False
    """
    True, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text.
    """
