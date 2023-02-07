from dotenv import get_key
import os

DOTENV_FILE = ".env"

class Configure(object):
    SERVER_HOST = os.environ.get("SERVER_HOST") or \
        get_key(DOTENV_FILE, "SERVER_HOST")
    SERVER_PORT = os.environ.get("SERVER_PORT") or \
        get_key(DOTENV_FILE, "SERVER_PORT")
    APP_SECRET = os.environ.get("APP_SECRET") or \
        get_key(DOTENV_FILE, "APP_SECRET")
    VK_CONFIRMATION = os.environ.get("VK_CONFIRMATION") or \
        get_key(DOTENV_FILE, "VK_CONFIRMATION")
    VK_GROUP_ID = os.environ.get("VK_GROUP_ID") or \
        get_key(DOTENV_FILE, "VK_GROUP_ID")
    TG_CHANNEL_NAME = os.environ.get("TG_CHANNEL_NAME") or \
        get_key(DOTENV_FILE, "TG_CHANNEL_NAME")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN") or \
        get_key(DOTENV_FILE, "TG_BOT_TOKEN")
