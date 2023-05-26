import requests
from lxml import etree

url = "https://beijing.zbj.com/search/service/?kw=saas&r=1"
resp = requests.get(url)
# print(resp.text)

# 解析
html = etree.HTML(resp.text)  # .HTML()作用为加载html源码

# 定位到第一家商铺，其他循环即可
# 拿到每一个服务商的div
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div')  # 由于相对路径里有""，所以外面要用''括起来，不能再用""

for div in divs:  # 每一个服务商信息
    price = div.xpath("./div/div[2]/div[1]/span/text()")  # [0]表示从列表里拿出来，strip()表示去掉
    if not price:
        print("empty")
    else:
        print(price)
    company_name = div.xpath("./div/a/div[2]/div[1]/div/text()")[0]
    if not company_name:
        print("empty")
    else:
        print(company_name)
    title = div.xpath("./div/div[2]/div[2]/a/text()")
    if not title:
        print("empty")
    else:
        print(title)
    # //*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/a