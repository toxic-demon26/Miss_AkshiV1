import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/7c3c26e0ed938aec91209.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Holla I'm Luna!** \n\n"
  LUNA += "ð´ **I'm Working Properly** \n\n"
  LUNA += "ð´ **My Master : [zeinzo](https://t.me/tdrki_1)** \n\n"
  LUNA += f"ð´ **Telethon Version : {tlhver}** \n\n"
  LUNA += f"ð´ **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Thanks For Adding Me Here â¤ï¸**"
  BUTTON = [[Button.url("Êá´Êá´", "https://t.me/lunatapibot?start=help"), Button.url("sá´á´á´á´Êá´", "https://t.me/lunaXresso")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "â **bot restarted successfully**\n\nâ¢ Admin list has been **updated**"
  BUTTON = [[Button.url("ð¡ á´á´á´á´á´á´s", "https://t.me/zeinproject")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
