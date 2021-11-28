from aiogram import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from parsers.parser import set_connection


async def sender(dp: Dispatcher):
    text = await set_connection()
    await dp.bot.send_message(chat_id=-1001708790143, text=text)


def setup(scheduler: AsyncIOScheduler, dp: Dispatcher):
    scheduler.add_job(func=sender, args=[dp], trigger='cron', hour=10)
    scheduler.add_job(func=sender, args=[dp], trigger='cron', hour=15)
    scheduler.add_job(func=sender, args=[dp], trigger='cron', hour=20)
    scheduler.start()
