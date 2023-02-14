from flask import Response
from fakel import app
from fakel.telegram import bot
from fakel.vk.types import *
from aiogram.utils.exceptions import *


async def wall_post_new(data : dict) -> Response:
    """Обработка событий для добавления новой записи в группе вк"""
    chat = "@{}".format(app.config.get("TG_CHANNEL_NAME"))
    try: 
        text = data["object"]["text"] # FIXME: нельзя отправить только фото
        images = extract_image_urls(data["object"]["attachments"])
        message = get_one_image(images) + text
        await bot.send_message(chat_id=chat, text=message, parse_mode="html")
    except KeyError as e:
        app.logger.warn("%s" % e)
        return Response("Failed")
    except IndexError as e:
        app.logger.warn("%s" % e)
    except ChatNotFound as e:
        app.logger.warn("%s" % e)
        return Response("Failed")
    except MessageIsTooLong as e:
        # FIXME: Добавить обработку такой ситуации. Например, через Telegraph
        app.logger.warn("%s" % e)
        return Response("Failed")
    except BadRequest as e:
        app.logger.warn("%s" % e)
    return Response("ok")

def get_one_image(images: list) -> str:
    if len(images):
        return images[0]
    else:
        return ""

def extract_image_urls(attachments : list) -> list:
    """Получение фото, стилизованных под html ссылки"""
    try:
        img_html = []
        image_urls = get_urls(get_images(attachments))
        for i in image_urls:
            img_html.append(f"<a href=\"{i}\">   </a>")
    except IndexError as e:
        app.logger.warn("%s" % e)
    return img_html

def get_images(attachments : list) -> list:
    """Получение объектов фото"""
    try:
        image_objs = [e for e in attachments if e["type"] == "photo"]
    except KeyError as e:
        app.logger.warn("%s" % e)
    finally:
        return image_objs

def get_urls(images : list) -> list:
    """Выделение ссылок на фото в макс. расширении"""
    try:
        urls = []
        for e in images:
            sizes = e["photo"]["sizes"]
            maxsize = sizes[0]
            for s in sizes:
                if PHOTO_SIZES.get(s["type"], -1) > PHOTO_SIZES.get(maxsize["type"], -1):
                    maxsize = s
            urls.append(maxsize["url"])
    except KeyError as e:
        app.logger.warn("%s" % e)
    finally:
        return urls

def extract_text(data : dict):
    pass

