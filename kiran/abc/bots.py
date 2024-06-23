import msgspec
import typing


class BotCommand(msgspec.Struct):
    """
    Represents a bot command.

    Parameters
    ----------
    command : str
        The command text. 1-32 characters.
    description : str
        The description of the command. 1-256 characters.
    """

    command: str
    description: str


class BotCommandScopeDefault(msgspec.Struct):
    """
    Represents a default bot command scope.

    Parameters
    ----------
    type : str
        Scope type, must be default
    """

    type: str = "default"


class BotCommandScopeAllPrivateChats(msgspec.Struct):
    """
    Represents an all private chats bot command scope.

    Parameters
    ----------
    type : str
        Scope type, must be all_private_chats
    """

    type: str = "all_private_chats"


class BotCommandScopeAllGroupChats(msgspec.Struct):
    """
    Represents an all group chats bot command scope.

    Parameters
    ----------
    type : str
        Scope type, must be all_group_chats
    """

    type: str = "all_group_chats"


class BotCommandScopeAllChatAdministrators(msgspec.Struct):
    """
    Represents an all chat administrators bot command scope.

    Parameters
    ----------
    type : str
        Scope type, must be all_chat_administrators
    """

    type: str = "all_chat_administrators"


class BotCommandScopeChat(msgspec.Struct):
    """
    Represents a chat bot command scope.

    Parameters
    ----------
    type : str
        Scope type, must be chat
    chat_id : int
        Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    """

    chat_id: int
    type: str = "chat"


class BotCommandScopeChatAdministrators(msgspec.Struct):
    """
    Represents a chat administrators bot command scope.

    Parameters
    ----------
    type : str
        Scope type, must be chat_administrators
    chat_id : int
        Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    """

    chat_id: int
    type: str = "chat_administrators"


class BotCommandScopeChatMember(msgspec.Struct):
    """
    Represents a chat member bot command scope.

    Parameters
    ----------
    type : str
        Scope type, must be chat_member
    chat_id : int
        Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    user_id : int
        Unique identifier of the target user
    """

    chat_id: int
    user_id: int
    type: str = "chat_member"


class BotName(msgspec.Struct):
    """
    Represents a bot name.

    Parameters
    ----------
    name : str
        The bot name. 1-255 characters.
    """

    name: str


class BotDescription(msgspec.Struct):
    """
    Represents a bot description.

    Parameters
    ----------
    description : str
        The bot description. 0-256 characters.
    """

    description: str


class BotShortDescription(msgspec.Struct):
    """
    Represents a bot short description.

    Parameters
    ----------
    short_description : str
        The bot short description. 0-64 characters.
    """

    short_description: str


BotCommandScope = typing.Union[
    BotCommandScopeDefault,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeChat,
    BotCommandScopeChatAdministrators,
    BotCommandScopeChatMember,
]
