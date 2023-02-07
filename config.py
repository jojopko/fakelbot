from dotenv import get_key

DOTENV_FILE = ".env"

class Configure(object):
    SERVER_HOST = get_key(DOTENV_FILE, "SERVER_HOST")
    SERVER_PORT = get_key(DOTENV_FILE, "SERVER_PORT")
    APP_SECRET = get_key(DOTENV_FILE, "APP_SECRET")
    VK_CONFIRMATION = get_key(DOTENV_FILE, "VK_CONFIRMATION")
    VK_GROUP_ID = get_key(DOTENV_FILE, "VK_GROUP_ID")
    TG_CHANNEL_NAME = get_key(DOTENV_FILE, "TG_CHANNEL_NAME")
    TG_BOT_TOKEN = get_key(DOTENV_FILE, "TG_BOT_TOKEN")
