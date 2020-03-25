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


@register(outgoing=True, pattern="^.covidid(?: |$)(.*)")
async def covid_id(request):
    """ covid-19 indonesia """
    covid_id_dict = {
        "Indonesia":
        "https://api.kawalcorona.com/indonesia/"
    }
    releases = 'Data Covid-19 Indonesia:\n'
    for name, release_url in covid_id_dict.items():
        data = get(release_url).json()
        releases += f'{name}: {data["positif"]["sembuh"]["meninggal"]}\n'
    await request.edit(releases)

    CMD_HELP.update({
    "corona": ".covidid\nUsage : Give information about Corona Virus in Indonesia"
})
