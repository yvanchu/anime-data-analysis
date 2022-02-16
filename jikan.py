import requests, json

## TODO: overcome the rate limit??
## maybe use timers?
baseurl = "https://api.jikan.moe/v4/seasons"

for year in range(2019, 2022):
    for season in ["winter", "spring", "summer", "fall"]:
        print(str(year) + " | " + season)
        url = baseurl + "/" + str(year) + "/" + season 
        r = requests.get(url).text
        res = json.loads(r)
        for page in range(1, res["pagination"]["last_visible_page"]):
            url = baseurl + "/" + str(year) + "/" + season + '/?page=' + str(page)
            r = requests.get(url).text
            res = json.loads(r)
            print(url)
            print(res)
            for anime in res["data"]:
                print(anime["title"])

