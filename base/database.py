from aiogram import Dispatcher
from aiogram.utils.executor import Executor
from gino import Gino

from data import config

db = Gino()


class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.Unicode(), unique=True)
    author = db.Column(db.Unicode())
    created_at = db.Column(db.DateTime(True), server_default=db.func.now())


async def on_startup(dispatcher: Dispatcher):
    await db.set_bind(config.POSTGRES_URI)


def setup(executor: Executor):
    executor.on_startup(on_startup)
