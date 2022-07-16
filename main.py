import logging
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime


from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = 6435225
API_HASH = "4e984ea35f854762dcde906dce426c2d" 
LOG_GROUP = os.environ.get("LOG_GROUP", None)
ALIVE_IMG = os.environ.get("ALIVE_PIC", None)
STRING_SESSION1 = os.environ.get("STRING_SESSION1", None)

SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "1829237132").split()}
DB_URL = os.environ.get("DATABASE_URL", None)
MONGO_DBB = os.environ.get("MONGO_DB", None)

if ALIVE_IMG:
    ALIVE_PIC = ALIVE_IMG
else: 
    ALIVE_PIC = 'https://te.legra.ph/file/c1672f2d5ac436575fc3b.mp4'

if MONGO_DBB:
    MONGO_DB = MONGO_DBB
else: 
    MONGO_DB = "https://visionbypankaj:Rf2BMcooABO6lP6K@cluster0.dgwig.mongodb.net/?retryWrites=true&w=majority"

if LOG_GROUP:
    Owner = LOG_GROUP
else:
    Owner = 777000

if STRING_SESSION1:
    bot1 = Client(session_name= STRING_SESSION1, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot1 = None





scheduler = AsyncIOScheduler()
CMD_HELP = {}
START_TIME = datetime.now()

if bot1:
    bot1.start()
    bot1.join_chat("flamingsupport")
    bot1.join_chat("flamingchat")

idle()


print("YPUR FLAMING BOT HAS BEEN DEPLOYED")
print("Enjoy! Do visit @flamingsupport")

