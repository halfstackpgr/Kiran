from __future__ import annotations

import fastenum
import datetime


class EventIntents(fastenum.Enum):
    """
    Enum representing the different types of updates that a bot can receive.

    Attributes
    ----------
    NEW_MESSAGE : str
        New incoming message of any kind - text, photo, sticker, etc.
    EDITED_MESSAGE : str
        New version of a message that is known to the bot and was edited.
    CHANNEL_POST
        New incoming channel post of any kind - text, photo, sticker, etc.
    CHANNEL_EDITED_POST
        New version of a channel post that is known to the bot and was edited.
    BUSINESS_CONNECTION
        The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot.
    BUSINESS_MESSAGE
        New message from a connected business account.
    EDITED_BUSINESS_MESSAGE
        New version of a message from a connected business account.
    DELETED_BUSINESS_MESSAGE
        Messages were deleted from a connected business account.
    MESSAGE_REACTION
        A reaction to a message was changed by a user.
    MESSAGE_REACTION_COUNT
        Reactions to a message with anonymous reactions were changed.
    INLINE_QUERY
        New incoming inline query.
    CHOSEN_INLINE_QUERY
        The result of an inline query that was chosen by a user and sent to their chat partner.
    CALLBACK_QUERY
        New incoming callback query.
    SHIPPING_QUERY
        New incoming shipping query. Only for invoices with flexible price.
    PRE_CHECKOUT_QUERY
        New incoming pre-checkout query. Contains full information about checkout.
    POLL
        New poll state. Bots receive only updates about manually stopped polls and polls, which are sent by the bot.
    POLL_ANSWER
        A user changed their answer in a non-anonymous poll.
    MY_CHAT_MEMBER
        The bot's chat member status was updated in a chat.
    CHAT_MEMBER
        A chat member's status was updated in a chat.
    CHAT_JOIN_REQUEST
        A request to join the chat has been sent.
    CHAT_BOOST
        A chat boost was added or changed.
    REMOVED_CHAT_BOOST
        A boost was removed from a chat.
    """

    NEW_MESSAGE = "message"
    EDITED_MESSAGE = "edited_message"
    CHANNEL_POST = "channel_post"
    CHANNEL_EDITED_POST = "edited_channel_post"
    BUSINESS_CONNECTION = "business_connection"
    BUSINESS_MESSAGE = "business_message"
    EDITED_BUSINESS_MESSAGE = "edited_business_message"
    DELETED_BUSINESS_MESSAGE = "deleted_business_messages"
    MESSAGE_REACTION = "message_reaction"
    MESSAGE_REACTION_COUNT = "message_reaction_count"
    INLINE_QUERY = "inline_query"
    CHOSEN_INLINE_QUERY = "chosen_inline_result"
    CALLBACK_QUERY = "callback_query"
    SHIPPING_QUERY = "shipping_query"
    PRE_CHECKOUT_QUERY = "pre_checkout_query"
    POLL = "poll"
    POLL_ANSWER = "poll_answer"
    MY_CHAT_MEMBER = "my_chat_member"
    CHAT_MEMBER = "chat_member"
    CHAT_JOIN_REQUEST = "chat_join_request"
    CHAT_BOOST = "chat_boost"
    REMOVED_CHAT_BOOST = "removed_chat_boost"


class KiranEvent:
    def __init__(
        self,
        event_id: int,
    ) -> None:
        self.event_id = event_id
        self.event_time = datetime.datetime.now()


class NewMessageEvent(KiranEvent):
    def __init__(self, event_id: int, message: ...) -> None:
        super().__init__(event_id)
