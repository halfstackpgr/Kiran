from __future__ import annotations

import typing
import aiohttp
import msgspec
import asyncio
import dataclasses

from ..errors import KiranPollingError
from ..abc.bots import BotCommand, BotCommandScope, BotCommandScopeDefault
from ..components.commands import LanguageCode

if typing.TYPE_CHECKING:
    from ..impl import KiranBot


@dataclasses.dataclass
class TelegramMethodName:
    """
    All methods in the Bot API are case-insensitive. We support GET and POST HTTP methods. Use either [URL query string](https://en.wikipedia.org/wiki/Query_string) or application/json or application/x-www-form-urlencoded or multipart/form-data for passing parameters in Bot API requests.
    On successful call, a JSON-object containing the result will be returned.
    """

    GET_ME: str = "getMe"
    LOG_OUT: str = "logOut"
    CLOSE: str = "close"
    SEND_MESSAGE: str = "sendMessage"
    FORWARD_MESSAGE: str = "forwardMessage"
    FORWARD_MESSAGES: str = "forwardMessages"
    COPY_MESSAGE: str = "copyMessage"
    COPY_MESSAGES: str = "copyMessages"
    SEND_PHOTO: str = "sendPhoto"
    SEND_AUDIO: str = "sendAudio"
    SEND_DOCUMENT: str = "sendDocument"
    SEND_VIDEO: str = "sendVideo"
    SEND_ANIMATION: str = "sendAnimation"
    SEND_VOICE: str = "sendVoice"
    SEND_VIDEO_NOTE: str = "sendVideoNote"
    SEND_MEDIA_GROUP: str = "sendMediaGroup"
    SEND_LOCATION: str = "sendLocation"
    SEND_VENUE: str = "sendVenue"
    SEND_CONTACT: str = "sendContact"
    SEND_POLL: str = "sendPoll"
    SEND_DICE: str = "sendDice"
    SEND_CHAT_ACTION: str = "sendChatAction"
    SET_MESSAGE_REACTION: str = "setMessageReaction"
    GET_USER_PROFILE_PHOTOS: str = "getUserProfilePhotos"
    GET_FILE: str = "getFile"
    BAN_CHAT_MEMBER: str = "banChatMember"
    UNBAN_CHAT_MEMBER: str = "unbanChatMember"
    RESTRICT_CHAT_MEMBERS: str = "restrictChatMembers"
    PROMOTE_CHAT_MEMBER: str = "promoteChatMember"
    SET_CHAT_ADMINISTRATOR_CUSTOM_TITLE: str = "setChatAdministratorCustomTitle"
    BAN_CHAT_SENDER_CHAT: str = "banChatSenderChat"
    UNBAN_CHAT_SENDER_CHAT: str = "unbanChatSenderChat"
    SET_CHAT_PERMISSIONS: str = "setChatPermissions"
    EXPORT_CHAT_INVITE_LINK: str = "exportChatInviteLink"
    CREATE_CHAT_INVITE_LINK: str = "createChatInviteLink"
    EDIT_CHAT_INVITE_LINK: str = "editChatInviteLink"
    REVOKE_CHAT_INVITE_LINK: str = "revokeChatInviteLink"
    APPROVE_CHAT_JOIN_REQUEST: str = "approveChatJoinRequest"
    DECLINE_CHAT_JOIN_REQUEST: str = "declineChatJoinRequest"
    SET_CHAT_PHOTO: str = "setChatPhoto"
    DELETE_CHAT_PHOTO: str = "deleteChatPhoto"
    SET_CHAT_TITLE: str = "setChatTitle"
    SET_CHAT_DESCRIPTION: str = "setChatDescription"
    PIN_CHAT_MESSAGE: str = "pinChatMessage"
    UNPIN_CHAT_MESSAGE: str = "unpinChatMessage"
    UNPIN_ALL_CHAT_MESSAGES: str = "unpinAllChatMessages"
    LEAVE_CHAT: str = "leaveChat"
    GET_CHAT: str = "getChat"
    GET_CHAT_ADMINISTRATORS: str = "getChatAdministrators"
    GET_CHAT_MEMBER_COUNT: str = "getChatMemberCount"
    GET_CHAT_MEMBER: str = "getChatMember"
    SET_CHAT_STICKER_SET: str = "setChatStickerSet"
    DELETE_CHAT_STICKER_SET: str = "deleteChatStickerSet"
    GET_FORUM_TOPIC_ICON_STICKER: str = "getForumTopicIconSticker"
    CREATE_FORUM_TOPIC: str = "createForumTopic"
    EDIT_FORUM_TOPIC: str = "editForumTopic"
    CLOSE_FORUM_TOPIC: str = "closeForumTopic"
    REOPEN_FORUM_TOPIC: str = "reopenForumTopic"
    DELETE_FORUM_TOPIC: str = "deleteForumTopic"
    UNPIN_ALL_FORUM_TOPIC_MESSAGES: str = "unpinAllForumTopicMessages"
    EDIT_GENERAL_FORUM_TOPIC: str = "editGeneralForumTopic"
    CLOSE_GENERAL_FORUM_TOPIC: str = "closeGeneralForumTopic"
    REOPEN_GENERAL_FORUM_TOPIC: str = "reopenGeneralForumTopic"
    HIDE_GENERAL_FORUM_TOPIC: str = "hideGeneralForumTopic"
    UNHIDE_GENERAL_FORUM_TOPIC: str = "unhideGeneralForumTopic"
    UNPIN_ALL_GENERAL_FORUM_TOPIC_MESSAGES: str = (
        "unpinAllGeneralForumTopicMessages"
    )
    ANSWER_CALLBACK_QUERY: str = "answerCallbackQuery"
    GET_USER_CHAT_BOOSTS: str = "getUserChatGBoosts"
    GET_BUSINESS_CONNECTION: str = "getBusinessConnection"
    SET_MY_COMMANDS: str = "setMyCommands"
    DELETE_MY_COMMANDS: str = "deleteMyCommands"
    GET_MY_COMMANDS: str = "getMyCommands"
    SET_MY_NAME: str = "setMyName"
    GET_MY_NAME: str = "getMyName"
    SET_MY_DESCRIPTION: str = "setMyDescription"
    GET_MY_DESCRIPTION: str = "getMyDescription"
    SET_MY_SHORT_DESCRIPTION: str = "setMyShortDescription"
    GET_MY_SHORT_DESCRIPTION: str = "getMyShortDescription"
    SET_CHAT_MENU_BUTTON: str = "setChatMenuButton"
    GET_CHAT_MENU_BUTTON: str = "getChatMenuButton"
    SET_MY_DEFAULT_ADMINISTRATOR_RIGHTS: str = "setMyDefaultAdministratorRights"
    GET_MY_DEFAULT_ADMINISTRATOR_RIGHTS: str = "getMyDefaultAdministratorRights"
    EDIT_MESSAGE_TEXT: str = "editMessageText"
    EDIT_MESSAGE_CAPTION: str = "editMessageCaption"
    EDIT_MESSAGE_MEDIA: str = "editMessageMedia"
    EDIT_MESSAGE_LIVE_LOCATION: str = "editMessageLiveLocation"
    STOP_MESSAGE_LIVE_LOCATION: str = "stopMessageLiveLocation"
    EDIT_MESSAGE_REPLY_MARKUP: str = "editMessageReplyMarkup"
    STOP_POLL: str = "stopPoll"
    DELETE_MESSAGE: str = "deleteMessage"
    DELETE_MESSAGES: str = "deleteMessages"

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.__match_args__}"


class KiranCaller:
    def __init__(self, bot: "KiranBot", token: str) -> None:
        self.client = bot
        self.token = token

    async def _make_request(
        self,
        method: typing.Union[str, TelegramMethodName],
        params: typing.Dict[str, typing.Any],
    ) -> typing.Optional[aiohttp.ClientResponse]:
        try:
            url = f"https://api.telegram.org/bot{self.token}/{method}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    self.client.log(
                        f"Caller Response:\n{await response.text()}", "debug"
                    )
                return response
        except asyncio.TimeoutError as e:
            str(e)
            self.client.log(
                "Timeout error occurred while making the request.", "warning"
            )
            raise KiranPollingError(
                message="Timeout error occurred while making the request.",
                client=self.client,
            )
        except aiohttp.ClientError as e:
            self.client.log(
                "Error trying to connect to the Telegram server.", "warning"
            )
            self.client.log(str(e), "debug")
            raise KiranPollingError(
                message="Error in trying to call the Telegram server.",
                client=self.client,
            )

    async def set_commands(
        self,
        bot_commands: typing.Union[typing.List[BotCommand], BotCommand],
        command_scope: typing.Optional[
            BotCommandScope
        ] = BotCommandScopeDefault(),
        language_code_iso: typing.Optional[
            typing.Union[str, typing.Type[LanguageCode]]
        ] = None,
    ) -> None:
        encoder = msgspec.json.Encoder()
        list_of_commands = encoder.encode(bot_commands).decode("utf-8")
        print(list_of_commands)
        scope_encoded = encoder.encode(command_scope).decode("utf-8")
        language_code_encoded = (
            encoder.encode(language_code_iso).decode("utf-8")
            if language_code_iso
            else None
        )

        params = {
            "commands": list_of_commands,
            "scope": scope_encoded,
        }
        if language_code_encoded is not None:
            params["language_code"] = language_code_encoded

        resp = await self._make_request(
            method=TelegramMethodName.SET_MY_COMMANDS,
            params=params,
        )
        self.client.log((await resp.content.read()).decode(), "debug")  # type: ignore
