from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import utils

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6388856547:AAH_rUbZSUsgWjcgEdXpDLP_OnrurMU2yIs"

PASSWORD = "admin"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

# Initialize Bot instance with default bot properties which will be passed to all API calls
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {message.from_user.full_name}!. Send the password if you want to get notifications")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        if message.text == PASSWORD:
            utils.create_chat(message.chat.id)
            await message.answer("You have been added to notifications list")
            return
        await message.answer("Send the password if you want to get notifications")
    except TypeError:
        await message.answer("Try again")


async def start() -> None:
    await dp.start_polling(bot)
