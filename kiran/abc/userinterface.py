from __future__ import annotations

import typing
import msgspec

from .chats import ChatAdministratorRights
from .misc import LoginUrl


class ForceReply(msgspec.Struct, tag=True):
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply').
    This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice [privacy mode](https://core.telegram.org/bots/features#privacy-mode). Not supported in channels and for messages
    sent on behalf of a Telegram Business account.
    """

    force_reply: bool = True
    """
    Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
    """
    input_field_placeholder: typing.Optional[str] = None
    """
    The placeholder to be shown in the input field when the reply is active; 1-64 characters.
    """
    selective: typing.Optional[bool] = False
    """
    Use this parameter if you want to force reply from specific users only. Targets:
    
    - Users that are `@mentioned` in the text of the Message object
    - If the bot's message is a reply to a message in the same chat and forum topic, sender of the original message.
    """


class ReplyKeyboardRemove(msgspec.Struct, tag=True):
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboard with
    the `ReplyKeyboardMarkup` or `ReplyKeyboardMarkup` object will be removed. Returns True on success.
    """

    remove_keyboard: bool = True
    """
    Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use `ForceReply`)
    """
    selective: typing.Optional[bool] = False
    """
    Use this parameter if you want to remove the keyboard for specific users only. Targets:
    
    - Users that are `@mentioned` in the text of the Message object
    - If the bot's message is a reply (has reply_to_message_id), sender of the original message.
    """


class KeyboardButtonRequestUsers(msgspec.Struct, tag=True):
    """
    Upon receiving a message with this object, Telegram clients will display a personal keyboard to the user. This keyboard will
    always contain only one button - an [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) that
    always results in exactly one text message. [See more](https://core.telegram.org/bots/api#keyboardbuttonrequestusers)
    """

    request_id = int
    """
    Identifier of the request
    """
    user_is_bot: typing.Optional[bool] = False
    """
    Pass True to request a bot, pass False to request a regular user
    """
    user_is_premium: typing.Optional[bool] = False
    """
    Pass True to request a Premium user
    """
    max_quantity: typing.Optional[int] = None
    """
    request_users: bool = True
    """
    request_name: bool = True
    """
    Request the user's first and last names.
    """
    request_username: typing.Optional[bool] = False
    """
    Request the users username.
    """
    request_photo: typing.Optional[bool] = False
    """
    Request the users profile pictures.
    """


class KeyboardButtonRequestChats(msgspec.Struct, tag=True):
    """
    Upon receiving a message with this object, Telegram clients will display a button requesting that the user
    add the bot to the attachment menu. [See more](https://core.telegram.org/bots/api#keyboardbuttonrequestchats)
    """

    request_id = int
    """
    Identifier of the request
    """
    chat_is_channel: typing.Optional[bool] = False
    """
    True to request a channel chat, pass False to request a group or a supergroup chat.
    """
    chat_is_forum: typing.Optional[bool] = False
    """
    True to request a forum supergroup, pass False to request a non-forum chat. If not specified, no additional restrictions are applied.
    """
    chat_has_username: typing.Optional[bool] = False
    """
    Pass True to request a supergroup or a channel with a username, pass False to request a chat without a username. If not specified, no additional restrictions are applied.
    """
    chat_is_created: typing.Optional[bool] = False
    """
    Pass True to request a chat owned by the user. Otherwise, no additional restrictions are applied.
    """
    user_administrator_rights: typing.Optional[ChatAdministratorRights] = None
    """
    The rights must be a superset of bot_administrator_rights. If not specified, no additional restrictions are applied.
    """
    bot_administrator_rights: typing.Optional[ChatAdministratorRights] = None
    """
    The rights must be a subset of user_administrator_rights. If not specified, no additional restrictions are applied.
    """
    bot_is_member: typing.Optional[bool] = False
    """
    Pass True to request a bot added to the attachment menu, pass False to request a bot not added to the attachment menu. If not specified, no additional restrictions are applied.
    """
    request_title: typing.Optional[bool] = False
    """
    Request the users title. Available in private chats only
    """
    request_username: typing.Optional[bool] = False
    """
    Request the users username. Available in private chats only
    """
    request_photo: typing.Optional[bool] = False
    """
    Request the users profile pictures. Available in private chats only
    """


class KeyboardButtonPollType(msgspec.Struct):
    """
    This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed. [See more](https://core.telegram.org/bots/api#keyboardbuttonpolltype)
    """

    type: typing.Optional[str] = None
    """
    Poll type, currently can be `regular` or `quiz`
    """


class WebAppInfo(msgspec.Struct, tag=True):
    """
    This object represents a service message about a Web App. [See more](https://core.telegram.org/bots/api#webappinfo)
    """

    url: typing.Optional[str] = None
    """
    An HTTPS URL of a Web App to be opened with additional data as specified in [Initializing Web Apps](https://core.telegram.org/bots/webapps#initializing-mini-apps)
    """


class KeyboardButton(msgspec.Struct, tag=True):
    """
    This object represents one button of the reply keyboard. [See more](https://core.telegram.org/bots/api#keyboardbutton)
    """

    text: str
    """
    Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
    """
    request_users: typing.Optional[KeyboardButtonRequestUsers] = None
    """
    If specified, pressing the button will open a list of suitable users. Identifiers of selected users will be sent to the bot in a `users_shared` service message. Available in private chats only.
    """
    request_chat: typing.Optional[KeyboardButtonRequestChats] = None
    """
    If specified, pressing the button will open a list of suitable chats. Tapping on a chat will send its identifier to the bot in a `chat_shared` service message. Available in private chats only.
    """
    request_contact: typing.Optional[bool] = False
    """
    If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only
    """
    request_location: typing.Optional[bool] = False
    """
    If True, the user's current location will be sent when the button is pressed. Available in private chats only
    """
    request_poll: typing.Optional[KeyboardButtonPollType] = None
    """
    If specified, the user will be asked to create or edit a poll and send it when the button is pressed. Available in private chats only
    """
    web_app: typing.Optional[WebAppInfo] = None
    """
    If specified, pressing the button will open a [`Web App`](https://core.telegram.org/bots/webapps) with the given URL. Available in private chats only
    """


class ReplyKeyboardMarkup(msgspec.Struct, tag=True):
    """
    This object represents a custom keyboard with reply options. [See more](https://core.telegram.org/bots/api#replykeyboardmarkup)
    """

    keyboard: typing.List[
        typing.List[typing.Union[KeyboardButton, typing.List[KeyboardButton]]]
    ]
    """
    Array of button rows, each represented by an Array of [KeyboardButton](https://core.telegram.org/bots/api#keyboardbutton) objects
    """
    resize_keyboard: typing.Optional[bool] = False
    """
    Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom
    [keyboard](https://core.telegram.org/bots#keyboards) will be used.
    """
    one_time_keyboard: typing.Optional[bool] = False
    """
    Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the
    chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
    """
    input_field_placeholder: typing.Optional[str] = None
    """
    The placeholder to be shown in the input field when the reply is active; 1-64 characters
    """
    selective: typing.Optional[bool] = False
    """
    Use this parameter if you want to show the keyboard to specific users only. Targets:
    
    - Users that are `@mentioned` in the text of the Message object
    - If the bot's message is a reply (has reply_to_message_id), sender of the original message.
    """


class InlineKeyboardButton(msgspec.Struct, tag=True):
    """
    This object represents one button of an inline keyboard. [See more](https://core.telegram.org/bots/api#inlinekeyboardbutton)
    """

    text: str
    """
    Label text on the button
    """
    url: typing.Optional[str] = None
    """
    HTTP or tg:// url to be opened when button is pressed
    """
    callback_data: typing.Optional[str] = None
    """
    Data to be sent in a callback query to the bot when the button is pressed, 1-64 bytes.
    """
    web_app: typing.Optional[WebAppInfo] = None
    """
    Description of the `Web App` to be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method [`answerWebAppQuery`](https://core.telegram.org/bots/api#answerwebappquery). Available only in private chats between a user and the bot.
    """
    login_url: typing.Optional[LoginUrl] = None
    """
    An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
    """
    switch_inline_query: typing.Optional[str] = None
    """
    If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. Not supported for messages sent on behalf of a Telegram Business account.
    """
    switch_inline_query_current_chat: typing.Optional[str] = None
    """
    If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent on behalf of a Telegram Business account.
    """
    pay: typing.Optional[bool] = None
    """
    Specify True, to send a [Pay](https://core.telegram.org/bots/api#payments) button. Substrings `⭐` and `XTR` in the buttons's text will be replaced with a Telegram Star icon.

    Note
    ----
    This type of button must always be the first button in the first row and can only be used in invoice messages.
    """


class InlineKeyboardMarkup(msgspec.Struct, tag=True):
    """
    Upon receiving a message with this object, Telegram clients will display an [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) with attached buttons. [See more](https://core.telegram.org/bots/api#inlinekeyboardmarkup)
    """

    inline_keyboard: typing.List[typing.List[InlineKeyboardButton]]
    """
    Array of button rows, each represented by an Array of [InlineKeyboardButton](https://core.telegram.org/bots/api#inlinekeyboardbutton) objects
    """
