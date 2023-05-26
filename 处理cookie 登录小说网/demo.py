# 登录 得到cookie
# 带着cookie 去请求到书架url 书架上的内容
import requests

session = requests.session()
data = {
    "loginName": "18536355523",
    "password": "123456zp"
}
# 1.登录
url = "https://passport.17k.com/ck/user/login"
resp = session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)

# 2.拿到书架上的数据
resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
# print(resp.text)
# print(resp.json())
# print(resp.json()["data"])
for a in resp.json()["data"]:
    print(a["bookName"])
# 使用Session对象发送请求可以使得在多个请求之间共享cookies，从而实现
# 登录状态的持续保持。在这个例子中，登录请求和书架请求都使用了同一个Session对象，因此可以成功获取到书架数据。