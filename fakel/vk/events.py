from fakel.telegram import bot
from fakel import app
from flask import Response

# Подтверждение группы для vk callback
async def confirmation(data : dict) -> Response:
    try:
        if data["group_id"] != int(app.config.get("VK_GROUP_ID", "None")):
            app.logger.warning("Wrong group_id - \"%s\"" % data["group_id"])
            return Response("Failed id")
        if data["secret"] != app.config.get("APP_SECRET", "None"):
            app.logger.warning("Wrong secret - \"%s\"" % data["secret"])
            return Response("Failed secret")
    except KeyError as e:
        app.logger.warning("Key %s in not existed. Uncorrect request!" % e)
        return Response("Failed")
    except ValueError:
        app.logger.warning("Env variable is not defined")
        return Response("Failed")
    return Response(app.config.get("VK_CONFIRMATION", "None"))

async def wall_post_new(data : dict) -> Response:
    try:
        text = data["object"]["text"]
        chat = "@{}".format(app.config.get("TG_CHANNEL_NAME"))
        await bot.send_message(chat_id=chat, text=text)
    except KeyError as e:
        app.logger.warn("%s" % e)
        return Response("Failed")
    return Response("ok")
