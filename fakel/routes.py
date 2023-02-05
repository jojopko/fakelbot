from fakel import app
from fakel.vk.types import UpdateTypes
from fakel.vk import events as vk
from flask import request, Response


@app.route("/vk", methods=["POST"])
async def vk_callback_halder():
    vk_update : dict = request.get_json()
    try:
        if vk_update["type"] == UpdateTypes.CONFIRMATION:
            return vk.confirmation(vk_update)
        if vk_update["type"] == UpdateTypes.WALL_NEW_POST:
            return vk.wall_post_new(vk_update)
    except KeyError as e:
        app.logger.warning("Key %s in not existed. Uncorrect request!" % e)
    return Response()

