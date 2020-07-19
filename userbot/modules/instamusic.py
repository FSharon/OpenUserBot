# port to OUB by fr7zzy

import subprocess
from userbot import bot, CMD_HELP
import glob
import os
from userbot.events import register
try:
    import subprocess
except BaseException:
    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)


@register(outgoing=True, pattern="^.song(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.edit("`Ok finding the song`")
    bruh(str(cmd))
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("`Sending song`")
    await bot.send_file(
        event.chat_id,
        loa,
        force_document=True,
        allow_cache=False,
        caption=cmd,
        reply_to=reply_to_id
    )
    await message.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3", shell=True)


CMD_HELP.update({
    "song": ".song\nUsage : Send mp3"
})
