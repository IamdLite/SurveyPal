from aiogram import Bot, Dispatcher

from bot.middlewares.i18n import i18n
from data.config import load_config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

config = load_config()
bot = Bot(token=config.bot.token)

## To-Do set up postgrestql database
database = ""

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, run_tasks_by_default=True)
_=i18n.gettext