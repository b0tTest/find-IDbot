
import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")


    API_ID = int(os.environ.get("API_ID", 12345))


    API_HASH = os.environ.get("API_HASH", "")


    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MyTestBotZ")


    BOT_USERNAME = os.environ.get("BOT_USERNAME", "findTgIDbot")
