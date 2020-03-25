@register(outgoing=True, pattern="^.covid.global$")
async def covid_global(request):
    """ covid-19 global """
    covid_global_dict = {
        "Global":
        "https://api.kawalcorona.com/"
    }
    releases = 'Covid-19 Global data:\n'
    for OBJECTID, release_url in covid_global_dict.items():
        data = get(release_url).json()
        releases += f'{OBJECTID}: ["Country_region"]["Last_Update"]["Lat"]["Long"]["Confirmed"]["Deaths"]["Recovered"]["Active"]\n'
    await request.edit(releases)
