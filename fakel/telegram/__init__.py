from fakel import app
from aiogram import Bot, Dispatcher, executor, types

TOKEN = app.config.get("TG_BOT_TOKEN")
bot = Bot(token=TOKEN)

# from fakel.telegram.bot import ping



