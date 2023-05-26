import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220927/vzbrpuxh040.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220927/v4n40lle0uj.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220927/00zammfmnia.jpg"
]

async def aiodownload(url):
    name = url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name,mode="wb") as f:
                f.write(await resp.content.read())

    print("over")

async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(aiodownload(url))
        tasks.append(task)

    await asyncio.wait(tasks)
    # 处理结果
    for task in tasks:
        result = task.result()
        # do something with result


if __name__ == '__main__':
    asyncio.run(main())