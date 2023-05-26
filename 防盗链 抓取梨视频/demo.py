import requests

url = "https://www.pearvideo.com/video_1734427"
contID = url.split("_")[1]
# https://video.pearvideo.com/mp4/adshort/20210707/cont-1734427-15713455_adpkg-ad_hd.mp4
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62",
           "Referer": "https://www.pearvideo.com/video_1734427"
           }

resp = requests.get(videoStatusUrl,headers=headers)
dic = resp.json()

srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime,f"cont-{contID}")

with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)
resp.close()