
# COPYRIGHT (C) 2021 BY SUKHI AND MAMBA_STAR

"""
(((((((((((((((((((((((@MAMBA_STAR)))))))))))))))))))))))))))
(((((((((((((((((((((((@MAMBA_STAR)))))))))))))))))))))))))))
(((((((((((((((((((((((@MAMBA_STAR)))))))))))))))))))))))))))
(((((((((((((((((((((((@MAMBA_STAR)))))))))))))))))))))))))))
                 MADE BY MAMBA_STAR AND SUKHI

"""

from telethon import events, Button, custom
import re, os
from MAMBA.events import register
from MAMBA_X import xbot as tbot
from MAMBA_X import xbot as tgbot
PHOTO = "https://telegra.ph/file/ea68644f59bdaf57fd61e.jpg"
@register(pattern=("/alive"))
async def awake(event):
  hiddenmamba = event.sender.first_name
  SUKHPAL443 = "HELLO THIS IS HIDDENMAMBA OFFICIAL \n\n"
  SUKHPAL443 += "ALL SYSTEM WORKING PROPERLY\n\n"
  SUKHPAL443 += "HIDDENMAMBA OS : 3.8 LATEST\n\n"
  SUKHPAL443 += f"MY MASTER {HIDDENMAMBA} ☺️\n\n"
  SUKHPAL443 += "FULLY UPDATED\n\n"
  SUKHPAL443 += "TELETHON : 1.19.5 LATEST\n\n"
  SUKHPAL443 += "THANKS FOR ADD ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/MAMBA_STAR"), Button.url("DEVLOPER", "https://t.me/MAMBA_STAR")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="MAMBA_STAR")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=MAMBA_STAR,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MAMBA_STAR")))
async def callback_query_handler(event):
# inline by MAMBA_STAR and MAMBA_STAR🔥
  MAMBAMUSIC_ASSISTANT = [[Button.url("REPO-BLACK", "https://github.com/SUKHPAL443/BLACK_MAMBA"), Button.url("REPO-BLACK", "https://github.com/SUKHPAL443/BLACK_MAMBA")]]
  MAMBAMUSIC_ASSISTANT +=[[Button.url("DEPLOY-BLACK", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FSUKHPAL443%2FBLACK_MAMBA&template=https%3A%2F%2Fgithub.com%2FSUKHPAL443%2FBLACK_MAMBAP%2FLE"), Button.url("DEPLOY-BLACK", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FSUKHPAL443%2FBLACK_MAMBA&template=https%3A%2F%2Fgithub.com%2FSUKHPAL443%2FBLACK_MAMBA")]]
  MAMBAMUSIC_ASSISTANT +=[[Button.url("TUTORIAL", "https://youtube.com"), Button.url("STRING-SESSION", "https://repl.it/@jaggi444/MAMBA#main.py")]]
  MAMBAMUSIC_ASSISTANT +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  MAMBAMUSIC_ASSISTANT +=[[Button.url("SUPPORT CHANNEL", "https://t.me/MAMBA_NETWORK"), Button.url("SUPPORT GROUP", "https://t.me/MAMBA_X_SUPPORT")]]
  MAMBAMUSIC_ASSITANT +=[[custom.Button.inline("ALIVE", data="MAMBA")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=MAMBA)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MAMBAMUSIC_ASSISTANT")))
async def callback_query_handler(event):
  global PHOTO
  hiddenmamba = event.sender.first_name
# inline by SUKHI and MAMBA_STAR 🔥
  SUKHPAL443 = "HELLO THIS IS HIDDENMAMBA \n\n"
  SUKHPAL443 += "ALL SYSTEM WORKING PROPERLY\n\n"
  SUKHPAL443 += "HIDDENMAMBA OS : 3.8 LATEST\n\n"
  SUKHPAL443 += f"MY MASTER {MAMBA} ☺️\n\n"
  SUKHPAL443 += "FULLY UPDATED BOT\n\n"
  SUKHPAL443 += "TELETHON : 1.19.5 LATEST\n\n"
  SUKHPAL443 += "THANKS FOR ADD ME HERE"
  BUTTONS = [[Button.url("MASTER", "https://t.me/MAMBA_STAR"), Button.url("DEVLOPER", "https://t.me/MAMBA_STAR")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="MAMBA")]]
  await event.edit(text=MAMBA, buttons=BUTTONS)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF HIDDENMAMBA", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/SUKHPAL443/BLACK_MAMBA")]])
# SUKHI 🔥 MAMBA_STAR

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
