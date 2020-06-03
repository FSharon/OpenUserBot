# Copyright (C) 2020 Frizzy
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.tiktok(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1) 
    chat = "@HK_tiktok_BOT"
    await event.edit("```Processing```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=801042975))
              await bot.send_message(chat, link)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @HK_tiktok_BOT and try again```")
              return
          if response.text.startswith("**Sorry I couldn't get TikTok video from**"):
             await event.edit("```I think this is not the right link```")
          else: 
             await event.delete()   
             await bot.send_message(event.chat_id, response.message)

CMD_HELP.update({
    "tiktok":
    ".tiktok <Link>"
    "\nUsage: Download TikTok video without watermark using @HK_tiktok_BOT"
}) 
