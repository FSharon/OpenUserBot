import json
import requests

from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.covidid$")
async def get_covidid(e):
    await e.edit(
    
    url = f'https://api.kawalcorona.com/indonesia/provinsi.json'
    request = requests.get(url)
    result = json.loads(request.text)
    
CMD_HELP.update({
        "covidid": ".covidid\
        \nUsage: Get covid-19 data in Indonesia\n"
    })
