import re
import requests
import csv
for i in range(11):
    url = f"https://movie.douban.com/top250?start={25*i}&limit=250"
    headers = {
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44"
    }
    resp = requests.get(url=url, headers=headers)
    page_content = resp.text

    obj = re.compile(r'<span class="title">(?P<name>.*?)'
                 r'</span>.*?<div class="bd">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span>(?P<num>.*?)</span>', re.S)

    result = obj.finditer(page_content)

    f = open("data.csv", mode="a")
    csvwriter = csv.writer(f)
    for it in result:
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())

f.close()
resp.close()
