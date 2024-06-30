import msgspec
import typing

from .messages import (
    MessageEntity,
    TextQuote,
)

from .users import User

from .misc import LinkPreviewOptions, MaskPosition

from .interactions import (
    Contact,
    Dice,
    Game,
    Poll,
    Venue,
    Location,
)
from .media import (
    Audio,
    Animation,
    PhotoSize,
    Document,
    Video,
    VideoNote,
    Voice,
)
from ..core.enums import ChatType, ParseMode
from .chats import ChatPhoto
from .files import File
from .misc import (
    BirthDate,
    BusinessLocation,
    BusinessOpeningHours,
)
from .reactions import ReactionTypeCustomEmoji, ReactionTypeEmoji
from ..core.enums import MessageOriginType, StickerType


class Sticker(msgspec.Struct):
    """
    Represents a telegram sticker.
    """

    file_id: str
    """
    Identifier for this file, which can be used to download or reuse the file
    """
    file_unique_id: str
    """
    Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    type: StickerType
    """
    Type of the sticker, currently one of `regular`, `mask`, `custom_emoji`. The type of the sticker is independent from its format, which is determined by the fields is_animated and is_video.
    """
    width: int
    """
    Sticker width
    """
    height: int
    """
    Sticker height
    """
    is_animated: bool
    """
    True, if the sticker is animated
    """
    is_video: bool
    """
    True, if the sticker is a video sticker
    """
    thumbnail: typing.Optional[PhotoSize]
    """
    Sticker thumbnail in the .WEBP or .JPG format
    """
    emoji: typing.Optional[str] = None
    """
    Emoji associated with the sticker
    """
    set_name: typing.Optional[str] = None
    """
    Name of the sticker set to which the sticker belongs
    """
    premium_animation: typing.Optional[File] = None
    """
    For premium regular stickers, premium animation for the sticker
    """
    mask_position: typing.Optional[MaskPosition] = None
    """
    For mask stickers, the position where the mask should be placed
    """
    custom_emoji_id: typing.Optional[str] = None
    """
    For custom emoji stickers, unique identifier of the custom emoji
    """
    needs_repainting: typing.Optional[bool] = False
    """
    True, if the sticker must be repainted to a text color
    """
    file_size: typing.Optional[int] = False
    """
    File size in bytes
    """


class BaseMessageOrigin(msgspec.Struct):
    """
    This object represents a message origin.
    """

    type: MessageOriginType
    """
    Origin type.
    """

    date: int
    """
    Date the message was sent originally in Unix time.
    """


class Chat(msgspec.Struct):
    """
    A instance representing a chat.
    """

    id: int
    """
    Unique identifier for this chat.
    """
    type: ChatType
    """
    Type of chat, can be either 'private', 'group', 'supergroup' or 'channel'.
    """
    title: typing.Optional[str] = None
    """
    Title, for supergroups, channels and group chats
    """
    username: typing.Optional[str] = None
    """
    Username, for private chats supergroups and channels if available
    """
    first_name: typing.Optional[str] = None
    """
    First name of the other party in a private chat
    """
    last_name: typing.Optional[str] = None
    """
    Last name of the other party in a private chat
    """
    is_forum: bool = False
    """
    True, if the supergroup is a forum has
    """


class Giveaway(msgspec.Struct):
    """
    This object represents a service message about the creation of a scheduled giveaway.
    Currently holds no information.
    """

    chats: typing.List[Chat]
    """
    The list of chats which the user must join to participate in the giveaway
    """
    winner_selection_date: int
    """
    The date when the giveaway ends. Unix time.
    """
    winner_count: int
    """
    Number of winners
    """
    only_new_members: typing.Optional[bool]
    """
    True, if only users who join the chats after the giveaway started should be eligible to win.
    """
    has_public_winners: bool
    """
    True, if the list of giveaway winners will be visible to everyone.
    """
    prize_description: typing.Optional[str] = None
    """
    Description of additional giveaway prize
    """
    country_codes: typing.Optional[typing.List[str]] = None
    """
    List of 2-letter ISO 3166-1 alpha-2 country codes. Currently, only one country can be specified.
    """
    premium_subscription_month_count: typing.Optional[int] = None
    """
    The number of months the Telegram Premium subscription won from the giveaway will be active for.
    """


class GiveawayWinners(msgspec.Struct):
    """
    Represents a message about the completion of a giveaway with public winners.
    """

    chat: Chat
    """
    The chat that created the giveaway.
    """
    giveaway_message_id: int
    """
    Identifier of the message with the giveaway in the chat.
    """
    winners_selection_date: int
    """
    The date when the giveaway winners were selected. Unix time.
    """
    winner_count: int
    """
    Number of winners
    """
    winners: typing.List[User]
    """
    List of up to 100 winners of the giveaway
    """
    additional_chat_count: typing.Optional[int]
    """
    Number of chats in which the giveaway was created
    """
    premium_subscription_month_count: typing.Optional[int]
    """
    The number of months the Telegram Premium subscription won from the giveaway will be active for.
    """
    unclaimed_prize_count: typing.Optional[int]
    """
    Number of undistributed prizes
    """
    only_new_members: typing.Optional[bool]
    """
    True, if only users who had joined the chats after the giveaway started were eligible to win.
    """
    was_refunded: typing.Optional[bool]
    """
    True, if the giveaway was refunded.
    """
    prize_description: typing.Optional[str] = None
    """
    Description of additional giveaway prize
    """


class MessageOriginChat(BaseMessageOrigin):
    """
    The message was originally sent on behalf of a chat to a group chat.
    """

    sender_chat: Chat
    """
    Chat that sent the message originally.
    """
    author_signature: typing.Optional[str] = None
    """
    For messages originally sent by an anonymous chat administrator, original message author signature.
    """


class MessageOriginChannel(BaseMessageOrigin):
    """
    The message was originally sent on behalf of a channel to a group chat.
    """

    chat: Chat
    """
    Channel that sent the message originally.
    """
    message_id: int
    """
    Unique message identifier inside the chat
    """
    author_signature: typing.Optional[str] = None
    """
    Signature of the original post author.
    """


class Story(msgspec.Struct):
    """
    Represents a telegram story
    """

    chat: Chat
    """
    Chat that posted the story
    """
    id: int
    """
    Unique identifier of the story
    """


class BusinessIntro(msgspec.Struct):
    """
    Contains information about the start page settings of a Telegram Business account.
    """

    title: typing.Optional[str] = None
    """
    Title text of the business intro
    """
    message: typing.Optional[str] = None
    """
    Message text of the business intro
    """
    sticker: typing.Optional[Sticker] = None
    """
    Sticker of the business intro
    """


class ChatFullInfo(Chat):
    """
    A instance representing a grouped information of a chat.
    """

    accent_color_id: typing.Optional[int] = None
    """
    Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview.
    """
    max_reaction_count: typing.Optional[int] = None
    """
    Maximum number of messages of the specified type in the chat
    """
    photo: typing.Optional[ChatPhoto] = None
    """
    Chat photo, if any.
    """
    active_usernames: typing.Optional[typing.List[str]] = None
    """
    If non-empty, the list of [all active chat usernames;](https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames) for private chats, supergroups and channels
    """
    birthdate: typing.Optional[BirthDate] = None
    """
    For private chats, the date of birth of the user.
    """
    business_intro: typing.Optional[BusinessIntro] = None
    """
    For private chats with business accounts, the intro of the business
    """
    business_location: typing.Optional[BusinessLocation] = None
    """
    For private chats with business accounts, the location of the business
    """
    business_opening_hours: typing.Optional[BusinessOpeningHours] = None
    """
    For private chats with business accounts, the opening hours of the business
    """
    personal_chat: typing.Optional[Chat] = None
    """
    For private chats, the personal channel of the user
    """
    available_reactions: typing.Optional[
        typing.List[typing.Union[ReactionTypeCustomEmoji, ReactionTypeEmoji]]
    ] = None
    """
    List of available reactions allowed in the chat. If omitted, then all [emoji reactions](https://core.telegram.org/bots/api#reactiontypeemoji) are allowed.
    """
    background_custom_emoji_id: typing.Optional[str] = None
    """
    Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background
    """
    profile_accent_color_id: typing.Optional[int] = None
    """
    Identifier of the accent color for the chat's profile background. See [profile accent colors](https://core.telegram.org/bots/api#profile-accent-colors) for more details.
    """
    profile_background_custom_emoji_id: typing.Optional[str] = None
    """
    Custom emoji identifier of the emoji chosen by the chat for its profile background.
    """
    emoji_status_custom_emoji_id: typing.Optional[str] = None
    """
    Custom emoji identifier of the emoji status of the chat or the other party in a private chat.
    """
    emoji_status_expiration_date: typing.Optional[int] = None
    """
    Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any.
    """
    bio: typing.Optional[str] = None
    """
    Bio of the other party in a private chat.
    """
    has_private_forwards: typing.Optional[bool] = False
    """
    True, if privacy settings of the other party in the private chat allows to use `tg://user?id=<user_id>` links only in chats with the user.
    """
    has_restricted_voice_and_video_messages: typing.Optional[bool] = False
    """
    True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat.
    """
    join_to_send_messages: typing.Optional[bool] = False
    """
    True, if users need to join the supergroup before they can send messages.
    """
    join_by_request: typing.Optional[bool] = False
    """
    True, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators.
    """
    description: typing.Optional[str] = None
    """
    Description, for groups, supergroups and channel chats.
    """
    invite_link: typing.Optional[str] = None
    """
    Primary invite link, for groups, supergroups and channel chats
    """
    pinned_message: typing.Optional["Message"] = None


class MessageAutoDeleteTimerChanged(msgspec.Struct):
    """
    This object represents a service message about a change in auto-delete timer settings.
    """

    message_auto_delete_time: int
    """
    New auto-delete time for messages in the chat
    """


class MessageOriginUser(BaseMessageOrigin):
    """
    The message was originally sent by a known user.
    """

    sender_user: User
    """
    User that sent the message originally.
    """


class MessageOriginHiddenUser(BaseMessageOrigin):
    """
    The message was originally sent by a hidden user.
    """

    sender_user_name: str
    """
    Name of the user that sent the message originally.
    """


class ExternalReplyInfo:
    """
    This object contains information about a message that is being replied to, which may come from another chat or forum topic.
    """

    origin: typing.Type[BaseMessageOrigin]
    """
    Origin of the message replied to by the given message.
    """
    chat: typing.Optional[Chat]
    """
    Chat the original message belongs to. Available only if the chat is a supergroup or a channel.
    """
    message_id: typing.Optional[int]
    """
    Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.
    """
    link_preview_options: typing.Optional[LinkPreviewOptions]


class InaccessibleMessage(msgspec.Struct, tag=True):
    """
    This object describes a message that was deleted or is otherwise inaccessible to the bot.
    """

    chat: Chat
    """
    Chat the message was belonged to.
    """
    message_id: int
    """
    Unique message identifier
    """
    date: int
    """
    Always 0. The field can be used to differentiate regular and inaccessible messages.
    """


class Message(msgspec.Struct, tag=True):
    """
    A telegram message.
    """

    message_id: int
    """
    Unique message identifier inside this chat
    """
    chat: Chat
    """
    Conversation the message belongs to.
    """
    message_thread_id: typing.Optional[int] = None
    """
    Unique identifier of a message thread to which the message belongs; for supergroups only
    """
    sender_chat: typing.Optional[Chat] = None
    """
    Sender of the message, sent on behalf of a chat. For example, the channel itself for channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    """
    sender_boost_count: typing.Optional[int] = None
    """
    If the sender of the message boosted the chat, the number of boosts added by the user.
    """
    sender_business_bot: typing.Optional[User] = None
    """
    The bot that actually sent the message on behalf of the business account. Available only for outgoing messages sent on behalf of the connected business account.
    """
    business_connection_id: typing.Optional[int] = None
    """
    Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.
    """
    forward_origin: typing.Optional[typing.Type[BaseMessageOrigin]] = None
    """
    Information about the original message for forwarded messages.
    """
    is_topic_message: typing.Optional[bool] = False
    """
    True, if the message is sent to a forum topic.
    """
    is_automatic_forward: typing.Optional[bool] = False
    """
    True, if the message is a channel post that was automatically forwarded to the connected discussion group.
    """
    reply_to_message: typing.Optional["Message"] = None
    """
    For replies in the same chat and message thread, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    """
    external_reply: typing.Optional[ExternalReplyInfo] = None
    """
    Information about the message that is being replied to, which may come from another chat or forum topic.
    """
    quote: typing.Optional[TextQuote] = None
    """
    For replies that quote part of the original message, the quoted part of the message.
    """
    reply_to_story: typing.Optional[Story] = None
    """
    For replies to a story, the original story.
    """
    via_bot: typing.Optional[User] = None
    """
    Bot through which the message was sent.
    """
    edit_date: typing.Optional[int] = None
    """
    Date the message was last edited in Unix time.
    """
    has_protected_content: typing.Optional[bool] = False
    """
    True, if the message can't be forwarded.
    """
    is_from_offline: typing.Optional[bool] = False
    """
    True, if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message.
    """
    media_group_id: typing.Optional[str] = None
    """
    The unique identifier of a media message group this message belongs to.
    """
    author_signature: typing.Optional[str] = None
    """
    Signature of the post author for messages in channels, or the custom title of an anonymous group administrator.
    """
    text: typing.Optional[str] = None
    """
    For text messages, the actual UTF-8 text of the message.
    """
    entities: typing.Optional[typing.List[MessageEntity]] = None
    """
    For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text.
    """
    link_preview_options: typing.Optional[LinkPreviewOptions] = None
    """
    Options used for link preview generation for the message, if it is a text message and link preview options were changed.
    """
    effect_id: typing.Optional[str] = None
    """
    Unique identifier of the message effect added to the message, if any.
    """
    animation: typing.Optional[Animation] = None
    """
    Original animation filename as defined by sender
    """
    audio: typing.Optional[Audio] = None
    """
    Original audio filename as defined by sender
    """
    document: typing.Optional[Document] = None
    """
    Message is a general file, information about the file.
    """
    photo: typing.Optional[typing.List[PhotoSize]] = None
    """
    Message is a photo, available sizes of the photo.
    """
    sticker: typing.Optional[Sticker] = None
    """
    Message is a sticker, information about the sticker.
    """
    story: typing.Optional[Story] = None
    """
    Message is a forwarded story.
    """
    video: typing.Optional[Video] = None
    """
    Message is a video, information about the video.
    """
    video_note: typing.Optional[VideoNote] = None
    """
    Message is a [video note](https://telegram.org/blog/video-messages-and-telescope), information about the video message
    """
    voice: typing.Optional[Voice] = None
    """
    Message is a voice message, information about the file
    """
    caption: typing.Optional[str] = None
    """
    Caption for the animation, audio, document, photo, video or voice
    """
    caption_entities: typing.Optional[typing.List[MessageEntity]] = None
    """
    For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
    """
    show_caption_above_media: typing.Optional[bool] = False
    """
    True, if the caption must be shown above the message media
    """
    has_media_spoiler: typing.Optional[bool] = False
    """
    True, if the message media is covered by a spoiler animation
    """
    contact: typing.Optional[Contact] = None
    """
    Message is a shared contact, information about the contact
    """
    dice: typing.Optional[Dice] = None
    """
    Message is a dice with random value
    """
    game: typing.Optional[Game] = None
    """
    Message is a game, information about the game. [More about games »](https://core.telegram.org/bots/api#games)
    """
    poll: typing.Optional[Poll] = None
    """
    Message is a native poll, information about the poll
    """
    venue: typing.Optional[Venue] = None
    """
    Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set.
    """
    location: typing.Optional[Location] = None
    """
    Message is a shared location, information about the location
    """
    new_chat_members: typing.Optional[typing.List[User]] = None
    """
    New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
    """
    left_chat_member: typing.Optional[User] = None
    """
    A member was removed from the group, information about them (this member may be the bot itself)
    """
    new_chat_title: typing.Optional[str] = None
    """
    A chat title was changed to this value
    """
    new_chat_photo: typing.Optional[typing.List[PhotoSize]] = None
    """
    A chat photo was change to this value
    """
    deleted_chat_photo: typing.Optional[bool] = False
    """
    Service message: the chat photo was deleted
    """
    group_chat_created: typing.Optional[bool] = False
    """
    Service message: the group has been created
    """
    supergroup_chat_created: typing.Optional[bool] = False
    """
    Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in `reply_to_message` if someone replies to a very first message in a directly created supergroup.
    """
    channel_chat_created: typing.Optional[bool] = False
    """
    Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in `reply_to_message` if someone replies to a very first message in a channel.
    """
    message_auto_delete_timer_changed: typing.Optional[
        MessageAutoDeleteTimerChanged
    ] = None
    """
    Service message: auto-delete timer settings changed in the chat.
    """
    migrate_from_chat_id: typing.Optional[int] = None
    """
    The supergroup has been migrated from a group with the specified identifier. 
    """
    pinned_message: typing.Optional[
        typing.Union["Message", InaccessibleMessage]
    ] = None

    from_user: typing.Optional[User] = msgspec.field(name="from", default=None)
    """
    Sender of the message; empty for messages sent to channels. For backward compatibility, the field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    """


class GiveawayCompleted(msgspec.Struct):
    """ """

    winner_count: int
    """
    Number of winners
    """
    unclaimed_prize_count: int
    """
    Number of unclaimed prizes
    """
    giveaway_message: typing.Optional[Message]
    """
    Message associated with the giveaway if not deleted.
    """


class ReplyParameters(msgspec.Struct):
    """
    Contains information about the message reply.
    """

    message_id: int
    """
    Identifier of the message to reply to.
    """
    chat_id: typing.Optional[int] = None
    """
    Identifier of the chat to send the message to (or username of the target channel in the format @channelusername).
    """
    allow_sending_without_reply: typing.Optional[bool] = None
    """
    Pass True, if the message should be sent even if the specified replied-to message is not found.
    """
    quote: typing.Optional[str] = None
    """
    Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including bold, italic, underline, strikethrough, spoiler, and custom_emoji entities. The message will fail to send if the quote isn't found in the original message.
    """
    quote_parse_mode: typing.Optional[ParseMode] = None
    """
    Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
    """
    quote_entities: typing.Optional[typing.List[MessageEntity]] = None
    """
    A JSON-serialized list of special entities that appear in the replied-to message, which can be specified instead of parse_mode.
    """
    quote_positon: typing.Optional[int] = None
    """
    Position of the quote in the original message in UTF-16 code units.
    """
