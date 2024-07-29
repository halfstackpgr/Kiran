> [!WARNING]
> **WARNING**: This library is currently in **early development phase** and is **NOT** ready for production use. It is **HIGHLY DISCOURAGED** to use this library with your bot token. The developer **DOES NOT TAKE ANY RESPONSIBILITY** if anything goes wrong or your bot is compromised due to the use of this library. Please wait for a stable release before using it for any purpose.

![Kiran Banner ](https://github.com/user-attachments/assets/a989d175-e8ac-4cc7-b26b-d7c8000859b4)

<div>
  <h1 align="center">A Lightweight Framework</h1>
  <p>
    <b>Kiran</b> is a highly optimized framework designed to streamline the interaction with the Telegram Bot API by utilizing long polling. It prioritizes the following key aspects:
    <ul>
      <li>Faster processing and data validation for enhanced performance.</li>
      <li>Type safety to minimize unforeseen errors.</li>
      <li>An easy-to-understand syntax and well-documented library for beginners, making it accessible to a wide range of developers.</li>
      <li>Limited user involvement, with most failures handled internally by the framework itself.</li>
      <li>Fully customizable and configurable options.</li>
      <li>Minimal dependencies to ensure a lightweight and efficient framework.</li>
      <li>Focus on raw usage as per the official Telegram documentation.</li>
      <li>Strong focus on error handling and robustness.</li>
      <li>Comprehensive test coverage to ensure stability and reliability.</li>
      <li>Continuous improvement and updates to stay up-to-date with the Telegram Bot API.</li>
    </ul>
  </p>
</div>

<div>
  <h3>Why Kiran?</h3>
  <h4>What sets Kiran apart from other frameworks?</h4>
  Kiran stands out from other options available for wrapping up a Telegram bot by utilizing a fast-paced serialization library (msgspec) for efficient data validation and processing. It also boasts a lightweight and efficient framework to ensure a stable and efficient functioning of the bot.</br> Additionally, Kiran has its own highly customizable logging system, inspired by Python's base-level logger. The key selling points of Kiran are its speed, efficiency, and ease of use as visible in the banner.
  <p>
  <h4>Current Status of Kiran</h4>
  Kiran is currently in development and is not yet complete. It is an ongoing effort with the goal of providing a comprehensive framework for interacting with the Telegram Bot API. The framework is being actively built and improved, and it is constantly evolving to meet the needs of developers
  </p>
</div>

> [!NOTE]
>   The fact that Kiran is developed on the notion that nothing can be completed without having the scope to be better, underscores the commitment to continued growth and development. In the meantime, Kiran is a valuable resource for developers and will continue to be refined and expanded in the future.


### Example Usage:

```python
import kiran
import kiran.abc
import kiran.core
import kiran.core.enums
import kiran.logger

# Setting up a bot instance to use it in the bot.
bot = kiran.KiranBot(
    token="...",
    logging_settings=kiran.LoggerSettings("standard", enable_colors=True),
)

# The decorator 'command' defines a command, follwed by the decorator
# 'implements' which helps to implement the command in the bot as slash,
# prefix or general(both) commands.
@bot.command(
    name="reactme",
    description="Reacts to a message.",
)
@kiran.implements(kiran.CommandImplements.SLASH_COMMAND)
async def test_command(command: kiran.CommandContext) -> None:
    """
    A basic test command that sends a message and reacts to it.
    
    Parameters
    ----------
    command : kiran.CommandContext
        The context of the command.
    """
    msg = await command.call.send_message(
        chat_id=command.chat_id,
        text="Hello User\n```python\nprint('This is a test command.')\n```",
        parse_mode=kiran.core.enums.ParseMode.MARKDOWN_V2,
    )
    if msg is not None:
        await command.call.set_reaction(
            chat_id=msg.chat.id,
            message_id=msg.message_id,
            reaction=[kiran.abc.ReactionTypeEmoji(emoji="💊", type="emoji")],
        )

# Start the bot to make it connect with the telegram API.
bot.run()
```