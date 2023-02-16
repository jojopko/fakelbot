from fakel import app
from fakel.vk.types import UpdateTypes
from fakel.vk.events import *
from flask import request, Response


@app.route("/vk", methods=["POST"])
async def vk_callback_halder():
    """Ловит post запросы со строны vk.com и обрабатывает их"""
    vk_update : dict = request.get_json()
    try:
        if vk_update["type"] == UpdateTypes.CONFIRMATION:
            return await confirmation(vk_update)
        if vk_update["type"] == UpdateTypes.WALL_NEW_POST:
            return await wall_post_new(vk_update)
    except KeyError as e:
        app.logger.warning("Key %s in not existed. Uncorrect request!" % e)
    return Response()

