# Copyright (C) 2020 Frizzy.
# All rights reserved.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.tiktok(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    song = event.pattern_match.group(1)
    chat = "@HK_tiktok_BOT"
    await event.edit("```Getting your TikTok video```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`Downloading...Please wait`")
          try:
              msg = await conv.send_message
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await event.reply("```Please unblock @HK_tiktok_BOT and try again```")
              return
          await event.edit("`Sending your TikTok video...`")
          await asyncio.sleep(3)
          await bot.send_file(event.chat_id, respond)
    await event.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await event.delete()

CMD_HELP.update({
    "tiktok":
    ".tiktok <Link>"
    "\nUsage: Download TikTok video without watermark with @HK_tiktok_BOT"
}) 
