import typing

class CommandOption:
    """
    Command options for the command handler.
    
    You can define options, that might not be visibly available in the command handler in the telegram GUI.
    But would work internally. And would process the command.s
    """
    def __init__(self, name : str, value : typing.Any) -> None:
        self.name = name
        self.value = value
        pass

    def __repr__(self) -> str:
        return f"{self.name}: {self.value}"

    def __str__(self) -> str:
        return self.__repr__()

class KiranCommmand:
    def __init__(
        self,
        name : str,
        description : str,
        options : typing.List[CommandOption]
        ) -> None:
        pass