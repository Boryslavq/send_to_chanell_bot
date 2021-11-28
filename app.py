from aiogram import Dispatcher, Bot
from aiogram.types import ParseMode
from aiogram.utils import executor

from base import database
from base.database import db
from data.config import token
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sender import send_message


async def on_startup(dispatcher: Dispatcher):
    await database.on_startup(dp)
    await db.gino.create_all()

    send_message.setup(scheduler, dp)


if __name__ == "__main__":
    scheduler = AsyncIOScheduler()

    bot = Bot(token=token, parse_mode=ParseMode.HTML, validate_token=True)
    dp = Dispatcher(bot)
    executor.start_polling(dp, on_startup=on_startup)
