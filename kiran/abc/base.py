import msgspec

class BaseUser(msgspec.Struct):
    """
    This object represents a Telegram user or bot.
    
    Attributes
    ----------
    id: int
        Unique identifier for this user or bot.
    is_bot: bool
        `True`, if this user is a bot
    first_name: str
        The user's first name.
    """
    id: int
    is_bot: bool
    first_name: str
    
