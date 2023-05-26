import requests
from lxml import etree
url = 'https://nba.hupu.com/stats/players'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
resp = requests.get(url, headers=headers)
e = etree.HTML(resp.text)

names = e.xpath('//table[@class="players_table"]//tr//td[2]//a//text()')
teams = e.xpath('//table[@class="players_table"]//tr//td[3]//a//text()')
with open('nba.txt','w',encoding='utf-8') as f:
    for name,team in zip(names,teams) :
        f.write(f'姓名：{name} 球队：{team}\n')