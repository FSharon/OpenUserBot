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
    d_link = event.pattern_match.group(1)
    value = 3
    if ".com" not in d_link:
        await event.edit("`I need a link to download something pro.`**(._.)**")
    else:
        await event.edit("```Processing ...```")
    chat = "@HK_tiktok_BOT"
    async with bot.conversation(chat) as conv:
          try:
              msg_start = await conv.send_message("/start")
              r = await conv.get_response()
              msg = await conv.send_message(d_link)
              details = await conv.get_response()
              video = await conv.get_response(value)
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")
              return
          await bot.send_file(event.chat_id, video)
          await event.client.delete_messages(conv.chat_id,
                                             [msg_start.id, r.id, msg.id, details.id, video.id])
          await event.delete()

CMD_HELP.update({
    "tiktok":
    ".tiktok <Link>"
    "\nUsage: Download TikTok video without watermark using @HK_tiktok_BOT"
}) 
