from __future__ import annotations

import typing
import httpx
import msgspec
import asyncio
import enum
import dataclasses


from ..errors import KiranPollingError
from ..abc.bots import BotCommand, BotCommandScope, BotCommandScopeDefault
from ..abc.misc import LinkPreviewOptions
from ..abc.userinterface import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
)
from ..abc.dependant import User, Chat, Message, MessageEntity, ReplyParameters
from ..components.commands import LanguageCode
from ..core.enums import ParseMode

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


class KiranCaller:
    def __init__(self, bot: "KiranBot") -> None:
        self.client = bot
        self.encoder = msgspec.json.Encoder()

    def _get_bytes(self, resp: httpx.Response) -> bytes:
        return msgspec.json.encode(resp.json()["result"])

    def build_params(self, **kwargs: typing.Any):
        params: typing.Dict[str, typing.Any] = dict()
        for name, argument in kwargs.items():
            if argument is not None:
                try:
                    if not isinstance(argument, enum.Enum):
                        params[name] = self.encoder.encode(argument).decode()
                except Exception:
                    if isinstance(argument, enum.Enum):
                        params[name] = argument.value
                    else:
                        params[name] = argument
                finally:
                    if isinstance(argument, enum.Enum):
                        params[name] = argument.value

        self.client.log("Params:\n" + str(params), "debug")
        return params

    async def _make_request(
        self,
        method: typing.Union[str, TelegramMethodName],
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        retry_count: int = 3,
        retry_delay: int = 1,
    ) -> typing.Optional[httpx.Response]:
        for attempt in range(retry_count):
            try:
                response = await self.client.session.get(method, params=params)  # type: ignore
                self.client.log(
                    f"Caller Response:\n{response.text}",
                    "debug",
                )
                if response.json()["ok"] is True:
                    return response
                else:
                    return None
            except (asyncio.TimeoutError, httpx.TimeoutException):
                if attempt < retry_count - 1:
                    self.client.log(
                        f"Error while making request to Telegram (attempt {attempt+1}/{retry_count}). Retrying in {retry_delay} seconds.",
                        "warning",
                    )
                    await asyncio.sleep(retry_delay)
                else:
                    self.client.log(
                        f"Error while making request to Telegram (attempt {attempt+1}/{retry_count}). Giving up.",
                        "error",
                    )
                    raise KiranPollingError(
                        message="Error while making request to Telegram.",
                        client=self.client,
                    )

    async def get_me(self) -> typing.Optional[User]:
        response = await self._make_request(method=TelegramMethodName.GET_ME)
        if response is not None:
            user = msgspec.json.decode(
                self._get_bytes(response),
                type=User,
                strict=False,
            )
            return user
        else:
            return None

    async def log_out(self) -> None:
        response = await self._make_request(method=TelegramMethodName.LOG_OUT)
        if response is not None:
            self.client.log(
                f"Log Out Response:\n{response.text}",
                "debug",
            )

    async def close(self) -> None:
        response = await self._make_request(method=TelegramMethodName.CLOSE)
        if response is not None:
            self.client.log(
                f"Close Response:\n{response.text}",
                "debug",
            )

    async def send_message(
        self,
        chat_id: typing.Union[int, str, Chat],
        text: str,
        business_connection_id: typing.Optional[str] = None,
        message_thread_id: typing.Optional[int] = None,
        parse_mode: typing.Optional[ParseMode] = None,
        entities: typing.Optional[typing.List[MessageEntity]] = None,
        link_preview_options: typing.Optional[LinkPreviewOptions] = None,
        disable_notification: typing.Optional[bool] = None,
        protect_content: typing.Optional[bool] = None,
        message_effect_id: typing.Optional[str] = None,
        reply_parameters: typing.Optional[ReplyParameters] = None,
        reply_markup: typing.Optional[
            typing.Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> typing.Optional[Message]:
        if isinstance(chat_id, Chat):
            chat_id = chat_id.id
        response = await self._make_request(
            method=TelegramMethodName.SEND_MESSAGE,
            params=self.build_params(
                chat_id=chat_id,
                text=text,
                business_connection_id=business_connection_id,
                message_thread_id=message_thread_id,
                parse_mode=parse_mode,
                entities=entities,
                link_preview_options=link_preview_options,
                disable_notification=disable_notification,
                protect_content=protect_content,
                message_effect_id=message_effect_id,
                reply_parameters=reply_parameters,
                reply_markup=reply_markup,
            ),
        )

        if response is not None:
            message = msgspec.json.decode(
                self._get_bytes(response),
                type=Message,
                strict=False,
            )
            return message
        else:
            return None

    async def forward_message(
        self,
        chat_id: typing.Union[int, str, Chat],
        from_chat_id: typing.Union[int, str, Chat],
        message_id: int,
        message_thread_id: typing.Optional[int] = None,
        disable_notification: typing.Optional[bool] = False,
        protect_content: typing.Optional[bool] = None,
    ) -> typing.Optional[Message]:
        if isinstance(chat_id, Chat):
            chat_id = chat_id.id
        response = await self._make_request(
            method=TelegramMethodName.FORWARD_MESSAGE,
            params=self.build_params(
                chat_id=chat_id,
                from_chat_id=from_chat_id,
                message_id=message_id,
                message_thread_id=message_thread_id,
                disable_notification=disable_notification,
                protect_content=protect_content,
            ),
        )

        if response is not None:
            message = msgspec.json.decode(
                self._get_bytes(response),
                type=Message,
                strict=False,
            )
            return message
        else:
            return None

    async def forward_messages(
        self,
        chat_id: typing.Union[int, str, Chat],
        from_chat_id: typing.Union[int, str, Chat],
        message_id: typing.List[int],
        message_thread_id: typing.Optional[int] = None,
        disable_notification: typing.Optional[bool] = False,
        protect_content: typing.Optional[bool] = None,
    ) -> typing.Optional[Message]:
        if isinstance(chat_id, Chat):
            chat_id = chat_id.id

        response = await self._make_request(
            method=TelegramMethodName.FORWARD_MESSAGE,
            params=self.build_params(
                chat_id=chat_id,
                from_chat_id=from_chat_id,
                message_id=message_id,
                message_thread_id=message_thread_id,
                disable_notification=disable_notification,
                protect_content=protect_content,
            ),
        )

        if response is not None:
            message = msgspec.json.decode(
                self._get_bytes(response),
                type=Message,
                strict=False,
            )
            return message
        else:
            return None

    async def copy_message(
        self,
        chat_id: typing.Union[int, str, Chat],
        from_chat_id: typing.Union[int, str, Chat],
        message_id: int,
        message_thread_id: typing.Optional[int] = None,
        caption: typing.Optional[str] = None,
        parse_mode: typing.Optional[ParseMode] = None,
        caption_entities: typing.Optional[typing.List[MessageEntity]] = None,
        disable_notification: typing.Optional[bool] = False,
        show_caption_above_media: typing.Optional[bool] = None,
        protect_content: typing.Optional[bool] = None,
        reply_parameters: typing.Optional[ReplyParameters] = None,
        reply_markup: typing.Optional[
            typing.Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> typing.Optional[int]:
        response = await self._make_request(
            method=TelegramMethodName.COPY_MESSAGE,
            params=self.build_params(
                chat_id=chat_id,
                from_chat_id=from_chat_id,
                message_id=message_id,
                message_thread_id=message_thread_id,
                caption=caption,
                parse_mode=parse_mode,
                caption_entities=caption_entities,
                disable_notification=disable_notification,
                protect_content=protect_content,
                show_caption_above_media=show_caption_above_media,
                reply_parameters=reply_parameters,
                reply_markup=reply_markup,
            ),
        )
        if response is not None:
            return int(response.json()["result"]["message_id"])
        else:
            return None

    async def copy_messages(
        self,
        chat_id: typing.Union[int, str, Chat],
        from_chat_id: typing.Union[int, str, Chat],
        message_id: typing.List[int],
        message_thread_id: typing.Optional[int] = None,
        caption: typing.Optional[str] = None,
        parse_mode: typing.Optional[ParseMode] = None,
        caption_entities: typing.Optional[typing.List[MessageEntity]] = None,
        disable_notification: typing.Optional[bool] = False,
        protect_content: typing.Optional[bool] = None,
    ) -> typing.Optional[typing.List[int]]:
        response = await self._make_request(
            method=TelegramMethodName.COPY_MESSAGES,
            params=self.build_params(
                chat_id=chat_id,
                from_chat_id=from_chat_id,
                message_id=message_id,
                message_thread_id=message_thread_id,
                caption=caption,
                parse_mode=parse_mode,
                caption_entities=caption_entities,
                disable_notification=disable_notification,
                protect_content=protect_content,
            ),
        )
        if response is not None:
            message_ids = msgspec.json.decode(
                self._get_bytes(response),
                type=typing.List[int],
                strict=False,
            )
            return message_ids
        else:
            return None

    async def set_commands(
        self,
        bot_commands: typing.Union[typing.List[BotCommand], BotCommand],
        command_scope: typing.Optional[
            BotCommandScope
        ] = BotCommandScopeDefault(),
        language_code_iso: typing.Optional[
            typing.Union[str, LanguageCode]
        ] = None,
    ) -> None:
        await self._make_request(
            method=TelegramMethodName.SET_MY_COMMANDS,
            params=self.build_params(
                commands=bot_commands,
                scope=command_scope,
                language_code=language_code_iso,
            ),
        )
