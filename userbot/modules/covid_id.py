import json
import requests

from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.covidid$")
async def get_covidid(e):
    if not e.text.startswith("."):
        return ""

    if not e.pattern_match.group(1):
        await e.edit("Usage: Get covid-19 data in Indonesia")
        return
    else:
        e.pattern_match.group(1)
    
    url = f'https://api.kawalcorona.com/indonesia/provinsi.json'
    request = requests.get(url)
    result = json.loads(request.text)
    
    if request.status_code != 200:
        await e.edit(f"{result['status_description']}")
        return
        
        provinsi = result["provinsi"]
        positif = result["kasus_posi"]
        sembuh = result["kasus_semb"]
        meninggal = result["kasus_meni"]
        
        textkirim = (f"**Provinsi :** `{provinsi}`\n" +
                     f"**Positif :**  `{kasus_posi}`\n\n" +
                     f"**Sembuh :** `{kasus_semb}`\n" +
                     f"**Meninggal :** `{kasus_meni}`\n")
                                
        await e.edit(textkirim)
    
CMD_HELP.update({
        "covidid": ".covidid\
        \nUsage: Get covid-19 data in Indonesia\n"
    })
