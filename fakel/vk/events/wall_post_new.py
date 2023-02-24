from flask import Response
from fakel import app
from fakel.telegram import bot
from fakel.vk.types import *
from aiogram.utils.exceptions import *


async def wall_post_new(data : dict) -> Response:
    """Обработка событий для добавления новой записи в группе вк"""
    chat = "@{}".format(app.config.get("TG_CHANNEL_NAME"))
    try: 
        text = extract_text(data) # FIXME: нельзя отправить только фото
        images = extract_image_urls(data)
        message = get_one_image(images) + text
        await bot.send_message(chat_id=chat, text=message, parse_mode="html")
    except KeyError as e:
        app.logger.warn("%s" % e)
        return Response("Failed")
    except ChatNotFound as e:
        app.logger.warn("%s\nchat: \"%s\"" % (e,chat))
        return Response("Failed")
    except MessageIsTooLong as e:
        # FIXME: Добавить обработку такой ситуации. Например, через Telegraph
        app.logger.warn("%s" % e)
        return Response("Failed")
    except BadRequest as e:
        app.logger.warn("%s\nmessage:\"%s\"" % (e,message))
        return Response("Failed")
    return Response("ok")

def extract_image_urls(data : dict) -> list:
    """Получение фото, стилизованных под html ссылки"""
    post = data.get("object")
    repost = post.get("copy_history")
    if repost is None:
        attachments = post.get("attachments")
    else:
        attachments = repost[0].get("attachments")
    
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

def get_one_image(images: list) -> str:
    """Вернуть первое фото"""
    return images[0] if len(images) else ""

def extract_text(data : dict) -> str:
    """Извлечь текст поста"""
    post = data.get("object")
    repost = post.get("copy_history")
    if repost is None:
        text = post.get("text")
    else:
        text = repost[0].get("text")
    return text
