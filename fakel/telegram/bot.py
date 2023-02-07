import asyncio
from fakel import app
from fakel.telegram import bot
import aiogram

# NOTE я не знаю на сколько это нужно...
# async def ping():
#     while True:
#         app.logger.info("Trying send message to telegram channel")
#         try:
#             aiogram.bot.Bot.se
#             chat_id = "@{}".format(app.config.get("TG_CHANNEL_NAME"))
#             message = await bot.send_message(chat_id=chat_id, text=".")
#             if await message.delete():
#                 app.logger.info("Bot is fully active")
#                 return
#             else:
#                 asyncio.sleep(5)
#         except Exception as e:
#             print(e)
#             return
            
    


