import logging
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from config import *

from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = API_ID
API_HASH = API_HASH 
LOG_CHAT = LOG_GROUP
SUDO_USERS = SUDO_USERS
DB_URL = DB_URL


if not STRING_SESSION1:
    logging.error("No String Session Found! Exiting!")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1)

if ALIVE_IMG:
    ALIVE_PIC = ALIVE_IMG
else: 
    ALIVE_PIC = 'https://te.legra.ph/file/c1672f2d5ac436575fc3b.mp4'

if MONGO_DB:
    MONGO_DB = MONGO_DB
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
    bot1.join_chat("flamingchat")

idle()

print("YPUR FLAMING BOT HAS BEEN DEPLOYED")
print("Enjoy! Do visit @flamingsupport")
