import fastenum


class ChatType(fastenum.Enum):
    """
    Enum representing a chat type.
    """

    PRIVATE = "private"
    """Represents a private chat."""
    GROUP = "group"
    """Represents a group chat."""
    SUPER_GROUP = "supergroup"
    """Represents a supergroup chat."""
    CHANNEL = "channel"
    """Represents a channel chat."""


class StickerType(fastenum.Enum):
    """
    Enum representing a sticker type.
    """

    REGULAR = "regular"
    """Represents a standard sticker."""
    MASK = "mask"
    """Represents a mask sticker."""
    CUSTOM_EMOJI = "custom_emoji"
    """Represents a custom emoji sticker."""


class MaskPositionPoint(fastenum.Enum):
    """
    Enum representing a mask position point.
    """

    FOREHEAD = "forehead"
    """Represents a mask position point on the forehead."""
    EYES = "eyes"
    """Represents a mask position point on the eyes."""
    MOUTH = "mouth"
    """Represents a mask position point on the mouth."""
    CHIN = "chin"
    """Represents a mask position point on the chin."""
