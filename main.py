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
    bot1 = Client(session_string= STRING_SESSION1, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot1 = None





scheduler = AsyncIOScheduler()
CMD_HELP = {}
START_TIME = datetime.now()

if bot1:
    bot1.start()
    bot1.join_chat("flamingsupport")
    bot1.join_chat("flamingchat")
if bot2:
    bot2.start()
    bot2.join_chat("flamingsupport")
    bot2.join_chat("flamingchat")
if bot3:
    bot3.start()
    bot3.join_chat("flamingsupport")
    bot3.join_chat("flamingchat")
if bot4:
    bot4.start()
    bot4.join_chat("flamingsupport")
    bot4.join_chat("flamingchat")
if bot5:
    bot5.start()
    bot5.join_chat("flamingsupport")
    bot5.join_chat("flamingchat")
if bot6:
    bot6.start()
    bot6.join_chat("flamingsupport")
    bot6.join_chat("flamingchat")
if bot7:
    bot7.start()
    bot7.join_chat("flamingsupport")
    bot7.join_chat("flamingchat")
if bot8:
    bot8.start()
    bot8.join_chat("flamingsupport")
    bot8.join_chat("flamingchat")
if bot9:
    bot9.start()
    bot9.join_chat("flamingsupport")
    bot9.join_chat("flamingchat")
if bot:
    bot.start()
    bot.join_chat("flamingsupport")
    bot.join_chat("flamingchat")
if bot11:
    bot11.start()
    bot11.join_chat("flamingsupport")
    bot11.join_chat("flamingchat")
if bot12:
    bot12.start()
    bot12.join_chat("flamingsupport")
    bot12.join_chat("flamingchat")
if bot13:
    bot13.start()
    bot13.join_chat("flamingsupport")
    bot13.join_chat("flamingchat")
if bot14:
    bot14.start()
    bot14.join_chat("flamingsupport")
    bot14.join_chat("flamingchat")
if bot15:
    bot15.start()
    bot15.join_chat("flamingsupport")
    bot15.join_chat("flamingchat")
if bot16:
    bot16.start()
    bot16.join_chat("flamingsupport")
    bot16.join_chat("flamingchat")
if bot17:
    bot17.start()
    bot17.join_chat("flamingsupport")
    bot7.join_chat("flamingchat")
if bot18:
    bot18.start()
    bot18.join_chat("flamingsupport")
    bot18.join_chat("flamingchat")
if bot19:
    bot19.start()
    bot19.join_chat("flamingsupport")
    bot19.join_chat("flamingchat")
if bot20:
    bot20.start()
    bot20.join_chat("flamingsupport")
    bot20.join_chat("flamingchat")
if bot21:
    bot21.start()
    bot21.join_chat("flamingsupport")
    bot21.join_chat("flamingchat")
if bot22:
    bot22.start()
    bot22.join_chat("flamingsupport")
    bot22.join_chat("flamingchat")
if bot23:
    bot23.start()
    bot23.join_chat("flamingsupport")
    bot23.join_chat("flamingchat")
if bot24:
    bot24.start()
    bot24.join_chat("flamingsupport")
    bot24.join_chat("flamingchat")
if bot25:
    bot25.start()
    bot25.join_chat("flamingsupport")
    bot25.join_chat("flamingchat")
if bot26:
    bot26.start()
    bot26.join_chat("flamingsupport")
    bot26.join_chat("flamingchat")
if bot27:
    bot27.start()
    bot27.join_chat("flamingsupport")
    bot27.join_chat("flamingchat")
if bot28:
    bot28.start()
    bot28.join_chat("flamingsupport")
    bot28.join_chat("flamingchat")
if bot29:
    bot29.start()
    bot29.join_chat("flamingsupport")
    bot29.join_chat("flamingchat")
if bot30:
    bot30.start()
    bot30.join_chat("flamingsupport")
    bot30.join_chat("flamingchat")
if bot31:
    bot31.start()
    bot31.join_chat("flamingsupport")
    bot31.join_chat("flamingchat")
if bot32:
    bot32.start()
    bot32.join_chat("flamingsupport")
    bot32.join_chat("flamingchat")
if bot33:
    bot33.start()
    bot33.join_chat("flamingsupport")
    bot33.join_chat("flamingchat")
if bot34:
    bot34.start()
    bot34.join_chat("flamingsupport")
    bot34.join_chat("flamingchat")
if bot35:
    bot35.start()
    bot35.join_chat("flamingsupport")
    bot35.join_chat("flamingchat")
if bot36:
    bot36.start()
    bot36.join_chat("flamingsupport")
    bot36.join_chat("flamingchat")
if bot37:
    bot37.start()
    bot37.join_chat("flamingsupport")
    bot37.join_chat("flamingchat")
if bot38:
    bot38.start()
    bot38.join_chat("flamingsupport")
    bot38.join_chat("flamingchat")
if bot39:
    bot39.start()
    bot39.join_chat("flamingsupport")
    bot39.join_chat("flamingchat")
if bot40:
    bot40.start()
    bot40.join_chat("flamingsupport")
    bot40.join_chat("flamingchat")
if bot41:
    bot41.start()
    bot41.join_chat("flamingsupport")
    bot41.join_chat("flamingchat")
if bot42:
    bot42.start()
    bot42.join_chat("flamingsupport")
    bot42.join_chat("flamingchat")
if bot43:
    bot43.start()
    bot43.join_chat("flamingsupport")
    bot43.join_chat("flamingchat")
if bot44:
    bot44.start()
    bot44.join_chat("flamingsupport")
    bot44.join_chat("flamingchat")
if bot45:
    bot45.start()
    bot45.join_chat("flamingsupport")
    bot45.join_chat("flamingchat")
if bot46:
    bot46.start()
    bot46.join_chat("flamingsupport")
    bot46.join_chat("flamingchat")
if bot47:
    bot47.start()
    bot47.join_chat("flamingsupport")
    bot47.join_chat("flamingchat")
if bot48:
    bot48.start()
    bot48.join_chat("flamingsupport")
    bot48.join_chat("flamingchat")
if bot49:
    bot49.start()
    bot49.join_chat("flamingsupport")
    bot49.join_chat("flamingchat")
if bot50:
    bot50.start()
    bot50.join_chat("flamingsupport")
    bot50.join_chat("flamingchat")

print("YPUR FLAMING BOT HAS BEEN DEPLOYED")
print("Enjoy! Do visit @flamingsupport")

idle()
