import typing
import datetime


if typing.TYPE_CHECKING:
    from ..impl import KiranBot
    from ..core.methods import KiranCaller

class KiranContext:
    def __init__(
        self,
        caller: KiranCaller,
        client: KiranBot,
        callback: typing.Callable[..., typing.Any],
        context_time:  datetime.datetime
    ) -> None:
        self.call = caller
        self.client = client
        self.context_time = context_time
        self.callback = callback
        self.context_time = context_time
        pass
