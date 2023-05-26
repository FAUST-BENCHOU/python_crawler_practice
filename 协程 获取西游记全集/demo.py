import asyncio
import aiohttp
import aiofiles
import json

async def aiodownload(cid, b_id, title):
    data = {
        "book_id": b_id,
        "cid": b_id + '|' + cid,
        "need_bookinfo": 1
    }
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={json.dumps(data)}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()

            async with aiofiles.open(title, mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])

async def getCatalog(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            tasks = []
            for item in dic['data']['novel']['items']:
                title = item['title']
                cid = item['cid']
                tasks.append(aiodownload(cid, b_id, title))
            await asyncio.wait(tasks)

if __name__ == '__main__':
    b_id = "4306063500"
    url = f'https://dushu.baidu.com/api/pc/getCatalog?data={{"book_id":"{b_id}"}}'
    asyncio.run(getCatalog(url))
