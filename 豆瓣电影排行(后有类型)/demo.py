import requests
import json

url = "https://movie.douban.com/j/chart/top_list"
para = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}
for i in range(8):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44"}

    resp = requests.get(url=url, params=para, headers=headers)

    for item in resp.json():
        print(item['title'])

    para["start"] = str((i + 1) * 20)
    json.dumps(para)

resp.close()
