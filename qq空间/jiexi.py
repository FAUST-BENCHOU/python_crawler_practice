from bs4 import BeautifulSoup as BS
import re

# 正则表达式进行匹配
def getText(match,text,group=1):
	tmp=re.search(match,text,re.S)
	if (tmp==None):
		return ""
	else:
		return tmp.group(group)

def get(html):
	soup=BS(html,"html.parser")
	shuoshuos=soup.find_all(name="li",attrs={"class":"f-single f-s-s"})
	for i in range(len(shuoshuos)):
		shuoshuo = shuoshuos[i]

		# 提取用户和时间
		user = shuoshuo.find("a", class_="f-name").get_text()
		time = getText(r"(\d\d:\d\d)", shuoshuo.find("span", class_="state").get_text())

		# 提取浏览次数 llcs
		llcs = 0
		llcs_match = shuoshuo.find("a", class_="state qz_feed_plugin")
		if llcs_match:
			llcs_text = llcs_match.get_text()
			llcs = int(getText(r"浏览(\d+)次", llcs_text))
			print(llcs)

		# 提取点赞用户和点赞次数
		like_info = shuoshuo.find("div", class_="f-like-list")
		haoyou = []
		likes=0
		if like_info:
			haoyou = [a.get_text() for a in like_info.find_all("a", class_="item q_namecard")]
			likes_match = like_info.find("span", class_="f-like-cnt")
			if likes_match:
				if likes_match:
					likes_text = likes_match.get_text()
					likes = int(re.search(r'\d+', likes_text).group())

		content_text=""
		# 提取说说内容
		content = shuoshuo.find("div", class_="f-single-content").find("div", class_="f-info")
		if content:
			content_text = content.get_text().strip()

		# 构造字典
		dic = {"user": user, "time": time, "llcs": llcs, "haoyou": haoyou, "likes": likes, "content": content_text}

		# 在data文件夹下面保存
		with open("data/{}_{}.txt".format(user, time.replace(":", "")), "w", encoding="utf-8") as f:
			f.write(str(dic))
