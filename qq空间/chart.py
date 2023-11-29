#  QQ空间解析/visualization.py
from pyecharts.charts.basic_charts.graph import Graph
links = []
nodes = []
with open("list.txt","r",encoding="utf-8") as f:
    tmp = eval(f.read())
    dic = {}
    for item in tmp:
        dic[item[0]] = dic.get(item[0],1) + item[2]
        dic[item[1]] = dic.get(item[1],1)
        links.append({"source":item[1],"target":item[0],"value":item[2]})
    for key in dic:
        nodes.append({"name":key,"symbolSize": (dic.get(key,1)+9)//10,"value":dic[key]})

graph = Graph()
graph.add("",nodes,links,
        categories=None, # 结点分类的类目，结点可以指定分类，也可以不指定。
        is_focusnode=False, # 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。默认为 True
        is_roam=True,
          )
graph.render(r"QQ点赞关系图.html")
