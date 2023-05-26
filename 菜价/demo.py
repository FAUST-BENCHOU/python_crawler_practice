import requests
import csv


url = "http://www.xinfadi.com.cn/getPriceData.html"
param = {
    "count": "450155",
    "current": "1",
    "limit": "90",
}
resp = requests.get(url=url,params=param)
data = resp.json()

f = open("菜价.csv", mode="w")
csvwriter = csv.writer(f)
for item in data['list']:
    csvwriter.writerow([item['prodName'], item['place'], item['avgPrice']])

resp.close()
f.close()