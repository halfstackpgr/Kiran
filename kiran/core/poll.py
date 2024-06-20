import aiohttp
import typing
import asyncio
import datetime
import msgspec

from ..errors import KiranPollingError

if typing.TYPE_CHECKING:
    from ..impl import KiranBot


class PollUpdates(msgspec.Struct):
    

class PollingManager:
    """
    A module class that helps to poll the polling URL using a long polling interval method.
    Check for events and invokes them.
    
    Parameters
    ----------
    client : KiranBot
        The bot client.
    timeout : typing.Optional[int]
        The timeout for the polling. Defaults to 5.
    """
    def __init__(self, token: str, client: "KiranBot", timeout: typing.Optional[int] = 5) -> None:
        
        self.START_TIME = datetime.datetime.now()
        self._token = token
        self.client = client
        self.timeout = timeout
        self.last_event_id : int = 0
        self.client.log("Polling has started for telegram bot with timeout: " + str(timeout) + ". Waiting for events.", "debug")
        pass

    async def _make_request(self)-> typing.Optional[aiohttp.ClientResponse]:
        try:
            async with aiohttp.ClientSession(base_url="https://api.telegram.org") as session:
                response = await session.get(f"bot{self._token}/getUpdates")
                
        except Exception as e:
            self.client.log("Error trying to connect to the telegram server.", "warning")
            self.client.log(str(e), "debug")
            raise KiranPollingError(session_response=session)