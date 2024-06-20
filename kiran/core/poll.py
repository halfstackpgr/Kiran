import aiohttp
import typing
import datetime
import asyncio

from ..errors import KiranPollingError

if typing.TYPE_CHECKING:
    from ..impl import KiranBot


class PollingManager:
    """
    A module class that helps to poll the polling URL using a long polling interval method.
    Check for events and invokes them.

    Parameters
    ----------
    token : str
        The Telegram bot token.
    client : KiranBot
        The bot client.
    timeout : typing.Optional[int]
        The timeout for the polling. Defaults to 100.
    """

    def __init__(
        self,
        token: str,
        client: "KiranBot",
        timeout: typing.Optional[int] = 100,
    ) -> None:
        self.START_TIME = datetime.datetime.now()
        self._token = token
        self.client = client
        self.timeout = timeout
        self.last_event_id: int = 0
        self.client.log(
            f"Polling has started for Telegram bot with timeout: {timeout}. Waiting for events.",
            "debug",
        )

    async def _make_request(self) -> typing.Optional[aiohttp.ClientResponse]:
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.get(
                    f"https://api.telegram.org/bot{self._token}/getUpdates",
                    params={
                        "timeout": self.timeout,
                        "offset": self.last_event_id + 1,
                    },
                )
                self.client.log(
                    f"Response of polling:\n{await response.text()}", "debug"
                )
                return response
        except aiohttp.ClientError as e:
            self.client.log(
                "Error trying to connect to the Telegram server.", "warning"
            )
            self.client.log(str(e), "debug")
            raise KiranPollingError(
                message="Error in trying to connect to the Telegram server.",
                client=self.client,
            )

    async def poll(self):
        while True:
            try:
                response = await self._make_request()
                if response and response.status == 200:
                    updates = await response.json()
                    if updates["result"]:
                        for update in updates["result"]:
                            print(update)
                            self.last_event_id = update["update_id"]
                await asyncio.sleep(
                    1
                )  # Small delay to prevent flooding the Telegram servers
            except Exception as e:
                self.client.log(f"Error in polling updates: {str(e)}", "error")
                await asyncio.sleep(5)  # Wait before retrying on error
