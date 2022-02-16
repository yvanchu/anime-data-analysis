import requests, json, sys

year = sys.argv[1]
season = sys.argv[2]

baseurl = "https://api.jikan.moe/v4/seasons"
page = 1
url = baseurl + "/" + str(year) + "/" + season + '/?page=' + str(page)
r = requests.get(url).text
res = json.loads(r)
hasNextPage = res["pagination"]["has_next_page"]

animeList = []
animeList += res['data']

while hasNextPage:
    page += 1
    url = baseurl + "/" + str(year) + "/" + season + '/?page=' + str(page)
    r = requests.get(url).text
    res = json.loads(r)
    hasNextPage = res["pagination"]["has_next_page"]
    animeList += res["data"]
    
print("mal_id" + "," + "title" + "," + "score" + "," + "scored_by" + "," + "rank" + ","
    + "popularity" + ","
    + "members" + ","
    + "favorites")

for anime in animeList:
    title = "\"" + anime["title"].replace("\"", "") + "\""
    print(str(anime["mal_id"]) + "," + title + "," + str(anime["score"]) + "," + str(anime["scored_by"]) + "," + str(anime["rank"]) + ","
    + str(anime["popularity"]) + ","
    + str(anime["members"]) + ","
    + str(anime["favorites"]))
