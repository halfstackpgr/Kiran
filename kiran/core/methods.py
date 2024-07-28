from __future__ import annotations

import asyncio
import dataclasses
import enum
import typing

import httpx
import msgspec

from ..abc.bots import BotCommand
from ..abc.bots import BotCommandScope
from ..abc.bots import BotCommandScopeDefault
from ..abc.chats import ChatPermissions
from ..abc.dependent import Chat
from ..abc.dependent import ChatFullInfo
from ..abc.dependent import ChatInviteLink
from ..abc.dependent import ChatMemberAdministrator
from ..abc.dependent import ChatMemberBanned
from ..abc.dependent import ChatMemberLeft
from ..abc.dependent import ChatMemberMember
from ..abc.dependent import ChatMemberOwner
from ..abc.dependent import ChatMemberRestricted
from ..abc.dependent import Message
from ..abc.dependent import MessageEntity
from ..abc.dependent import ReplyParameters
from ..abc.dependent import User
from ..abc.files import File
from ..abc.users import UserProfilePhotos
from ..errors import KiranPollingError

if typing.TYPE_CHECKING:
    from ..abc.misc import LinkPreviewOptions
    from ..abc.reactions import ReactionTypeCustomEmoji
    from ..abc.reactions import ReactionTypeEmoji
    from ..abc.userinterface import ForceReply
    from ..abc.userinterface import InlineKeyboardMarkup
    from ..abc.userinterface import ReplyKeyboardMarkup
    from ..abc.userinterface import ReplyKeyboardRemove
    from ..components.commands import LanguageCode
    from ..core.enums import ParseMode
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
        self.client.log("Caller: JSON Encoder initialized.", "debug")

    def _get_bytes(self, resp: httpx.Response) -> bytes:
        return msgspec.json.encode(resp.json()["result"])

    def build_params(self, **kwargs: typing.Any):
        params: typing.Dict[str, typing.Any] = dict()  # noqa: C408
        for name, argument in kwargs.items():
            if argument is not None:
                try:
                    if not isinstance(argument, enum.Enum):
                        # TODO Find an alternative and fast solution for these processing.
                        # params.update(
                        #    {
                        #        params[name] : self.encoder.encode(argument).decode()
                        #    }
                        # )
                        # this is not doing the '" thing, but is not encoding the arguments properly.
                        # params[name] = self.encoder.encode(argument).decode() # this is doing the '" thing but is encoding.
                        # every arguments properly!
                        encoded_value = (
                            self.encoder.encode(argument)
                            .decode()
                            .strip('"')
                            .replace("\\n", "\n")
                        )
                        params[name] = encoded_value
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
                    f"Caller Response:\n{msgspec.json.format(response.text, indent=4)}",
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
        message_ids: typing.List[int],
        message_thread_id: typing.Optional[int] = None,
        remove_caption: typing.Optional[str] = None,
        disable_notification: typing.Optional[bool] = False,
        protect_content: typing.Optional[bool] = None,
    ) -> typing.Optional[typing.List[int]]:
        response = await self._make_request(
            method=TelegramMethodName.COPY_MESSAGES,
            params=self.build_params(
                chat_id=chat_id,
                from_chat_id=from_chat_id,
                message_ids=message_ids,
                message_thread_id=message_thread_id,
                remove_caption=remove_caption,
                disable_notification=disable_notification,
                protect_content=protect_content,
            ),
        )
        if response is not None:
            return response.json()["result"]["message_ids"]
        else:
            return None

    async def set_reaction(
        self,
        chat_id: typing.Optional[typing.Union[int, str]],
        message_id: typing.Optional[int] = None,
        reaction: typing.Optional[
            typing.List[
                typing.Union[ReactionTypeCustomEmoji, ReactionTypeEmoji]
            ]
        ] = None,
        is_big: typing.Optional[bool] = False,
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.SET_MESSAGE_REACTION,
            params=self.build_params(
                chat_id=chat_id,
                message_id=message_id,
                reaction=reaction,
                is_big=is_big,
            ),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def get_user_profile_photos(
        self,
        user_id: int,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Optional[UserProfilePhotos]:
        response = await self._make_request(
            method=TelegramMethodName.GET_USER_PROFILE_PHOTOS,
            params=self.build_params(
                user_id=user_id, offset=offset, limit=limit
            ),
        )
        if response is not None:
            profile_photos = msgspec.json.decode(
                self._get_bytes(response),
                type=UserProfilePhotos,
                strict=False,
            )
            return profile_photos

        else:
            return None

    async def get_file(self, file_id: str) -> typing.Optional[File]:
        response = await self._make_request(
            method=TelegramMethodName.GET_FILE,
            params=self.build_params(file_id=file_id),
        )
        if response is not None:
            file = msgspec.json.decode(
                self._get_bytes(response), type=File, strict=False
            )
            return file
        else:
            return None

    async def ban_chat_member(
        self,
        chat_id: typing.Union[str, int],
        user_id: int,
        until_date: typing.Optional[int],
        revoke_messages: typing.Optional[bool],
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.BAN_CHAT_MEMBER,
            params=self.build_params(
                chat_id=chat_id,
                user_id=user_id,
                until_date=until_date,
                revoke_messages=revoke_messages,
            ),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def unban_chat_member(
        self,
        chat_id: typing.Union[str, int],
        user_id: int,
        only_if_banned: typing.Optional[bool] = None,
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.UNBAN_CHAT_MEMBER,
            params=self.build_params(
                chat_id=chat_id, user_id=user_id, only_if_banned=only_if_banned
            ),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def restrict_chat_member(
        self,
        chat_id: typing.Union[str, int],
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: typing.Optional[bool] = None,
        until_date: typing.Optional[int] = None,
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.RESTRICT_CHAT_MEMBERS,
            params=self.build_params(
                chat_id=chat_id,
                user_id=user_id,
                permissions=permissions,
                use_independent_chat_permissions=use_independent_chat_permissions,
                until_date=until_date,
            ),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def promote_chat_member(
        self,
        chat_id: typing.Union[str, int],
        user_id: int,
        is_anonymous: typing.Optional[bool] = None,
        can_manage_chat: typing.Optional[bool] = None,
        can_delete_messages: typing.Optional[bool] = None,
        can_manage_video_chats: typing.Optional[bool] = None,
        can_restrict_members: typing.Optional[bool] = None,
        can_promote_members: typing.Optional[bool] = None,
        can_change_info: typing.Optional[bool] = None,
        can_invite_users: typing.Optional[bool] = None,
        can_post_stories: typing.Optional[bool] = None,
        can_edit_stories: typing.Optional[bool] = None,
        can_delete_stories: typing.Optional[bool] = None,
        can_post_messages: typing.Optional[bool] = None,
        can_edit_messages: typing.Optional[bool] = None,
        can_pin_messages: typing.Optional[bool] = None,
        can_manage_topics: typing.Optional[bool] = None,
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.PROMOTE_CHAT_MEMBER,
            params=self.build_params(
                chat_id=chat_id,
                user_id=user_id,
                is_anonymous=is_anonymous,
                can_manage_chat=can_manage_chat,
                can_delete_messages=can_delete_messages,
                can_manage_video_chats=can_manage_video_chats,
                can_restrict_members=can_restrict_members,
                can_promote_members=can_promote_members,
                can_change_info=can_change_info,
                can_invite_users=can_invite_users,
                can_post_stories=can_post_stories,
                can_edit_stories=can_edit_stories,
                can_delete_stories=can_delete_stories,
                can_post_messages=can_post_messages,
                can_edit_messages=can_edit_messages,
                can_pin_messages=can_pin_messages,
                can_manage_topics=can_manage_topics,
            ),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def set_chat_administrator_custom_title(
        self, chat_id: typing.Union[str, int], user_id: int, custom_title: str
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.SET_CHAT_ADMINISTRATOR_CUSTOM_TITLE,
            params=self.build_params(
                chat_id=chat_id, user_id=user_id, custom_title=custom_title
            ),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def ban_chat_sender_chat(
        self, chat_id: typing.Union[str, int], sender_chat_id: int
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.BAN_CHAT_SENDER_CHAT,
            params=self.build_params(
                chat_id=chat_id, sender_chat_id=sender_chat_id
            ),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def unban_chat_sender_chat(
        self, chat_id: typing.Union[str, int], sender_chat_id: int
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.UNBAN_CHAT_SENDER_CHAT,
            params=self.build_params(
                chat_id=chat_id, sender_chat_id=sender_chat_id
            ),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def set_chat_permissions(
        self,
        chat_id: typing.Union[str, int],
        permissions: ChatPermissions,
        use_independent_chat_permissions: typing.Optional[bool] = None,
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.SET_CHAT_PERMISSIONS,
            params=self.build_params(
                chat_id=chat_id,
                permissions=permissions,
                use_independent_chat_permissions=use_independent_chat_permissions,
            ),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def export_chat_invite_link(
        self, chat_id: typing.Union[str, int]
    ) -> typing.Optional[str]:
        response = await self._make_request(
            method=TelegramMethodName.EXPORT_CHAT_INVITE_LINK,
            params=self.build_params(chat_id=chat_id),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return None

    async def create_chat_invite_link(
        self,
        chat_id: typing.Union[str, int],
        name: typing.Optional[str] = None,
        expire_date: typing.Optional[int] = None,
        member_limit: typing.Optional[int] = None,
        creates_join_request: typing.Optional[bool] = None,
    ) -> typing.Optional[ChatInviteLink]:
        response = await self._make_request(
            method=TelegramMethodName.CREATE_CHAT_INVITE_LINK,
            params=self.build_params(
                chat_id=chat_id,
                name=name,
                expire_date=expire_date,
                member_limit=member_limit,
                creates_join_request=creates_join_request,
            ),
        )
        if response is not None:
            return msgspec.json.decode(
                self._get_bytes(response), type=ChatInviteLink, strict=False
            )
        else:
            return None

    async def edit_chat_invite_link(
        self,
        chat_id: typing.Union[str, int],
        invite_link: str,
        expire_date: typing.Optional[int] = None,
        member_limit: typing.Optional[int] = None,
        creates_join_request: typing.Optional[bool] = None,
    ) -> typing.Optional[ChatInviteLink]:
        response = await self._make_request(
            method=TelegramMethodName.EDIT_CHAT_INVITE_LINK,
            params=self.build_params(
                chat_id=chat_id,
                invite_link=invite_link,
                expire_date=expire_date,
                member_limit=member_limit,
                creates_join_request=creates_join_request,
            ),
        )
        if response is not None:
            return msgspec.json.decode(
                self._get_bytes(response), type=ChatInviteLink, strict=False
            )
        else:
            return None

    async def revoke_chat_invite_link(
        self, chat_id: typing.Union[str, int], invite_link: str
    ) -> typing.Optional[ChatInviteLink]:
        response = await self._make_request(
            method=TelegramMethodName.REVOKE_CHAT_INVITE_LINK,
            params=self.build_params(chat_id=chat_id, invite_link=invite_link),
        )
        if response is not None:
            return msgspec.json.decode(
                self._get_bytes(response), type=ChatInviteLink, strict=False
            )
        else:
            return None

    async def approve_chat_join_request(
        self, chat_id: typing.Union[str, int], user_id: int
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.APPROVE_CHAT_JOIN_REQUEST,
            params=self.build_params(chat_id=chat_id, user_id=user_id),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def decline_chat_join_request(
        self, chat_id: typing.Union[str, int], user_id: int
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.DECLINE_CHAT_JOIN_REQUEST,
            params=self.build_params(chat_id=chat_id, user_id=user_id),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def set_chat_photo(
        self, chat_id: typing.Union[str, int], photo: typing.BinaryIO
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.SET_CHAT_PHOTO,
            params=self.build_params(chat_id=chat_id, photo=photo),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def delete_chat_photo(self, chat_id: typing.Union[str, int]) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.DELETE_CHAT_PHOTO,
            params=self.build_params(chat_id=chat_id),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def set_chat_title(
        self, chat_id: typing.Union[str, int], title: str
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.SET_CHAT_TITLE,
            params=self.build_params(chat_id=chat_id, title=title),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def set_chat_description(
        self, chat_id: typing.Union[str, int], description: str
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.SET_CHAT_DESCRIPTION,
            params=self.build_params(chat_id=chat_id, description=description),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def pin_chat_message(
        self,
        chat_id: typing.Union[str, int],
        message_id: int,
        disable_notification: typing.Optional[bool] = None,
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.PIN_CHAT_MESSAGE,
            params=self.build_params(
                chat_id=chat_id,
                message_id=message_id,
                disable_notification=disable_notification,
            ),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def unpin_chat_message(
        self, chat_id: typing.Union[str, int], message_id: int
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.UNPIN_CHAT_MESSAGE,
            params=self.build_params(chat_id=chat_id, message_id=message_id),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def unpin_all_chat_messages(
        self, chat_id: typing.Union[str, int]
    ) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.UNPIN_ALL_CHAT_MESSAGES,
            params=self.build_params(chat_id=chat_id),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def leave_chat(self, chat_id: typing.Union[str, int]) -> bool:
        response = await self._make_request(
            method=TelegramMethodName.LEAVE_CHAT,
            params=self.build_params(chat_id=chat_id),
        )
        if response is not None:
            return response.json()["result"]
        else:
            return False

    async def get_chat(
        self, chat_id: typing.Union[str, int]
    ) -> typing.Optional[ChatFullInfo]:
        response = await self._make_request(
            method=TelegramMethodName.GET_CHAT,
            params=self.build_params(chat_id=chat_id),
        )
        if response is not None:
            return msgspec.json.decode(
                self._get_bytes(response), type=ChatFullInfo, strict=False
            )
        else:
            return None

    async def get_chat_administrators(
        self, chat_id: typing.Union[str, int]
    ) -> typing.Optional[
        typing.Sequence[
            typing.Union[
                ChatMemberRestricted,
                ChatMemberAdministrator,
                ChatMemberMember,
                ChatMemberLeft,
                ChatMemberBanned,
                ChatMemberOwner,
            ]
        ]
    ]:
        response = await self._make_request(
            method=TelegramMethodName.GET_CHAT_ADMINISTRATORS,
            params=self.build_params(chat_id=chat_id),
        )
        if response is not None:
            print(self._get_bytes(response))
            ps = msgspec.json.decode(
                self._get_bytes(response),
                type=typing.Sequence[
                    typing.Union[
                        ChatMemberRestricted,
                        ChatMemberAdministrator,
                        ChatMemberMember,
                        ChatMemberLeft,
                        ChatMemberBanned,
                        ChatMemberOwner,
                    ]
                ],
                strict=False,
            )
            return ps
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
