import glob
filelist=glob.glob("data/*.txt")
dic={};
for file in filelist:
	with open(file,"r",encoding="utf-8") as f:
		d=eval(f.read())
		if (dic.get(d["user"])==None):
			dic[d["user"]]={}
		for haoyou in d["haoyou"]:
			if dic[d["user"]].get(haoyou)==None:
				dic[d["user"]][haoyou]=1
			else:
				dic[d["user"]][haoyou]=dic[d["user"]][haoyou]+1
l = []
for key in dic:
	if key == '':
		continue
	for key2 in dic[key]:
		if key2 == "":
			continue
		l.append([key,key2,dic[key][key2]])
		#key 收到 key2 dic[key][key2] 次点赞
with open("list.txt","w",encoding="utf-8") as f:
	f.write(str(l))
