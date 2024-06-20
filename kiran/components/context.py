import typing
import datetime

from kiran.core.methods import KiranCaller
from kiran.impl import KiranBot


if typing.TYPE_CHECKING:
    from ..impl import KiranBot
    from ..core.methods import KiranCaller


class KiranContext:
    def __init__(
        self,
        caller: KiranCaller,
        client: KiranBot,
        callback: typing.Callable[..., typing.Any],
        context_time: datetime.datetime,
    ) -> None:
        self.call = caller
        self.client = client
        self.callback = callback
        self.context_time = context_time
        pass


class CommandContext(KiranContext):
    def __init__(
        self,
        name: str,
        description: str,
        prefix: str,
        message_id: int,
        chat_id: int,
        invoking_message: str,
        caller: KiranCaller,
        client: KiranBot,
        callback: typing.Callable[..., typing.Any],
        context_time: datetime.datetime,
    ) -> None:
        self._name = name
        self._description = description
        self._prefix = prefix
        self._description = description
        self._message_id = message_id
        self._chat_id = chat_id
        self._invoking_message = invoking_message
        super().__init__(caller, client, callback, context_time)

    @property
    def name(self) -> str:
        """
        Name of the command provided at the time of registration.

        Returns
        -------
        name: str
            Name of the command.
        """
        return self._name

    @property
    def description(self) -> str:
        """
        Description of the command provided at the time of registration.

        Returns
        -------
        description: str
            Description of the command.
        """
        return self._description

    @property
    def prefix(self) -> str:
        """
        Prefix used to invoke the command.

        Returns
        -------
        prefix: str
            Prefix used to invoke the command.
        """
        return self._prefix

    @property
    def message_id(self) -> int:
        """
        Message ID of the message that invoked the command.

        Returns
        -------
        message_id: int
            Message ID of the message that invoked the command.
        """
        return self._message_id

    @property
    def chat_id(self) -> int:
        """
        Chat ID of the chat that invoked the command.

        Returns
        -------
        chat_id: int
            Chat ID of the chat that invoked the command.
        """
        return self._chat_id

    @property
    def invoking_message(self) -> str:
        """
        Message that invoked the command.

        Returns
        -------
        invoking_message: str
            Message that invoked the command.
        """
        return self._invoking_message
