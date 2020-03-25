# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to android"""

import re
from requests import get
from bs4 import BeautifulSoup

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.covid.global$")
async def covid_global(request):
    """ covid-19 global """
    covid_global_dict = {
        "Global":
        "https://api.kawalcorona.com/"
    }
    releases = 'Covid-19 Global data:\n'
    for OBJECTID, release_url in covid_global_dict.items():
        data = get(release_url)()
        releases += f'{OBJECTID}: {data["Country_region"]["Last_Update"]["Lat"]["Long"]["Confirmed"]["Deaths"]["Recovered"]["Active"]}\n'
    await request.edit(releases)

    CMD_HELP.update({
    "covid": ".covid.global\nUsage : Give information about Corona Virus in your country"
})
