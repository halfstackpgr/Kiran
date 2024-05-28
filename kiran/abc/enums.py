import fastenum

class ChatType(fastenum.Enum):
    """
    Enum representing a chat type. 
    
    Attributes
    ----------
    PRIVATE : str
        Represents a private chat.
    GROUP : str
        Represents a group chat.
    SUPER_GROUP : str
        Represents a supergroup chat.
    CHANNEL : str
        Represents a channel chat.
    """
    PRIVATE = "private"
    GROUP = "group"
    SUPER_GROUP = "supergroup"
    CHANNEL = "channel"