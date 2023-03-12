import pytest
import json
import copy
import enum
from flask.testing import FlaskClient
from data import *
from fakel import app


class ERROR_MESSAGES(enum.Enum):
    WRONG_RESPONSE_CODE = "Wrong response code. Should be 200."
    WRONG_RESPONSE_MESSAGE = "Wrong response message. Should be 'ok'."


@pytest.fixture
def application():
    app.config.update({
        "TESTING": True,
    })
    return app


@pytest.fixture
def client(application) -> FlaskClient:
    return application.test_client()


@pytest.fixture
def vk_text_requests(application) -> list[dict]:
    templates = []
    with open("tests/static/vk_callback_request_exaple.json", 'r') as f:
        TEMPLATE = json.load(f)
    template = TEMPLATE.copy()
    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = SMALL_TEXT
    template["object"]["attachments"] = []
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_1024
    template["object"]["attachments"] = []
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_2048
    template["object"]["attachments"] = []
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_4096
    template["object"]["attachments"] = []
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = VERY_LONG_TEXT
    template["object"]["attachments"] = []
    templates.append(copy.deepcopy(template))
    return templates
    

def test_api_new_post_only_text(client : FlaskClient, vk_text_requests):
    resp = client.post("/", json=vk_text_requests[0])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_CODE
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_requests[1])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_COD
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_requests[2])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_COD
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_requests[3])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_COD
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_requests[4])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_COD
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE


@pytest.fixture
def attachments_pack() -> list[dict]:
    attachments = []
    with open("tests/static/attachments/image1.json", "r") as f:
        attachments.append(json.load(f))
    with open("tests/static/attachments/image2.json", "r") as f:
        attachments.append(json.load(f))
    with open("tests/static/attachments/image3.json", "r") as f:
        attachments.append(json.load(f))
    with open("tests/static/attachments/video1.json", "r") as f:
        attachments.append(json.load(f))
    with open("tests/static/attachments/video2.json", "r") as f:
        attachments.append(json.load(f))
    with open("tests/static/attachments/doc1.json", "r") as f:
        attachments.append(json.load(f))
    return attachments


@pytest.fixture
def vk_text_with_attachments_requests(application, attachments_pack):
    templates = []
    with open("tests/static/vk_callback_request_exaple.json", 'r') as f:
        TEMPLATE = json.load(f)
    template = TEMPLATE.copy()
    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = SMALL_TEXT
    template["object"]["attachments"].append(attachments_pack[0])
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_1024
    template["object"]["attachments"].append(attachments_pack[0])
    template["object"]["attachments"].append(attachments_pack[1])
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_2048
    template["object"]["attachments"].append(attachments_pack[0])
    template["object"]["attachments"].append(attachments_pack[1])
    template["object"]["attachments"].append(attachments_pack[2])
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_4096
    template["object"]["attachments"].append(attachments_pack[3])
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_1024
    template["object"]["attachments"].append(attachments_pack[3])
    template["object"]["attachments"].append(attachments_pack[4])
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_1024
    template["object"]["attachments"].append(attachments_pack[1])
    template["object"]["attachments"].append(attachments_pack[3])
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_1024
    template["object"]["attachments"].append(attachments_pack[1])
    template["object"]["attachments"].append(attachments_pack[2])
    template["object"]["attachments"].append(attachments_pack[3])
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_2048
    template["object"]["attachments"].append(attachments_pack[5])
    templates.append(copy.deepcopy(template))

    template["group_id"] = application.config["VK_GROUP_ID"]
    template["secret"] = application.config["APP_SECRET"]
    template["object"]["text"] = LONG_TEXT_2048
    template["object"]["attachments"].append(attachments_pack[1])
    template["object"]["attachments"].append(attachments_pack[5])
    templates.append(copy.deepcopy(template))
    return templates


def test_api_new_post_with_attachments(client : FlaskClient, vk_text_with_attachments_requests):
    resp = client.post("/", json=vk_text_with_attachments_requests[0])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_CODE
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_with_attachments_requests[1])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_CODE
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_with_attachments_requests[2])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_CODE
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_with_attachments_requests[3])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_CODE
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_with_attachments_requests[4])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_CODE
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_with_attachments_requests[6])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_CODE
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_with_attachments_requests[7])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_CODE
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

    resp = client.post("/", json=vk_text_with_attachments_requests[8])
    assert resp.status_code == 200, ERROR_MESSAGES.WRONG_RESPONSE_CODE
    assert resp.text == "ok", ERROR_MESSAGES.WRONG_RESPONSE_MESSAGE

