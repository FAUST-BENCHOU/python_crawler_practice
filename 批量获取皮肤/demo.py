import requests
from lxml import etree
import os
from time import sleep
# 访问英雄主页
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'}

hero_list_url = "https://pvp.qq.com/web201605/js/herolist.json"
hero_list_resp = requests.get(hero_list_url, headers = headers)

for h in hero_list_resp.json():
    ename = h.get('ename')#编号
    cname = h.get('cname')#名字
    if not os.path.exists('cname'):
        os.makedirs(cname)


    hero_info_url = f'https://pvp.qq.com/web201605/herodetail/{ename}.shtml'
    hero_info_resp = requests.get(hero_info_url, headers = headers)
    hero_info_resp.encoding='gbk'

    e = etree.HTML(hero_info_resp.text)
    names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
    names = ([name[0:name.index('&')]for name in names.split('|')])


    for i,n in enumerate(names):
        url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i+1}.jpg'
        resp = requests.get(url, headers=headers)
        with open(f'{cname}/{n}.jpg','wb') as f:
            f.write(resp.content)
            sleep(1)





