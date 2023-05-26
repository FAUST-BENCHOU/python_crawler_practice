import re
import requests

domain = "https://www.dytt89.com"


resp = requests.get(domain, verify=False)
resp.encoding = 'utf-8'

print(resp.text)

obj1 = re.compile(r"2023必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名　(?P<name>.*?)<br />.*?<td'
                  r' style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<downlaod>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')

    result2 = obj2.finditer(resp.text)
    for itt in result2:
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href)

for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gbk'
    result3 = obj3.search(child_resp.text)
    print(child_resp.text)

    print(result3.group("name"))
    print(result3.group("downloading"))

resp.close()