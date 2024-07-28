from __future__ import annotations

import msgspec


class ReactionTypeCustomEmoji(msgspec.Struct, tag_field="reaction_type"):
    """The reaction is based on a custom emoji."""

    custom_emoji_id: str
    """
    Custom emoji identifier
    """
    type: str = "custom_emoji"
    """
    The type of the emoji. Always "custom_emoji"
    """


class ReactionTypeEmoji(msgspec.Struct, tag_field="reaction_type"):
    """The reaction is based on an emoji."""

    type: str
    """
    The type of the emoji. Always "emoji"
    """

    emoji: str
    """
    Reaction emoji. Currently, it can be one of "👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"
    """
