import os
import pandas as pd
import matplotlib.pyplot as plt

# 读取 data 文件夹中的所有文件
data_folder = "data"
all_files = os.listdir(data_folder)

# 创建一个空的 DataFrame
df = pd.DataFrame(columns=["user", "time", "llcs", "haoyou", "likes", "content"])

# 从每个文件中读取数据并添加到 DataFrame 中
for file in all_files:
    with open(os.path.join(data_folder, file), "r", encoding="utf-8") as f:
        data = eval(f.read())
        df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)

# 将时间列转换为 datetime 类型
df["time"] = pd.to_datetime(df["time"])

# 设置时间为索引
df.set_index("time", inplace=True)

# 按小时进行分组，并计算每个小时的点赞总数
hourly_likes = df.resample("H").sum()["likes"]

# 找到获得最高 likes 的时间段
top_likes_time = hourly_likes.idxmax()

# 打印结果
print("时间段：", top_likes_time)
print("点赞总数：", hourly_likes[top_likes_time])

# 绘制折线图
plt.figure(figsize=(10, 6))
hourly_likes.plot(kind="line", marker="o", linestyle="-", color="b")
plt.title("Hourly Likes on QQ Zone Posts")
plt.xlabel("Hour")
plt.ylabel("Number of Likes")
plt.grid(True)
plt.show()
