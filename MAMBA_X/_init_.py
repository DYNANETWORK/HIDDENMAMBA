from HIDDENMAMBA.events import register as MAMBA_STAR
from HIDDENMAMBA import telethn as bot
from HIDDENMAMBA import API_ID, API_HASH, TOKEN
from HIDDENMAMBA.events import *
from telethon import TelegramClient
from telethon.sessions import StringSession

import os
STRING_SESSION = os.environ.get("STRING_SESSION")
if STRING_SESSION:
  try:
    user = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
  except:
    pass
else:
     print ("please add StringSession var")

try:
     user.start()
except Exception as e:
     print(e)
try:      
  xbot = TelegramClient ("HIDDENMAMBA", API_ID, API_HASH).start(bot_token=TOKEN)
except:
  pass
if __name__ == "__main__":
   try:
      xbot.run_until_disconnected()
   except:
      pass
  #copyright by SUKHPAL443
