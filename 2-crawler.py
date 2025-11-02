import sys
import urllib.request
from threading import Thread
import asyncio
import aiohttp


from utils import calc_time, async_calc_time

links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

def crawl(link, timeout=5):
    print(f"crawl started for {link}")
    with urllib.request.urlopen(link, timeout=timeout) as conn:
        data = conn.read()
    print(f"crawl ended for {link}")
    return data

@calc_time
def crawl_single_thread(func):
    for link in links:
        func(link)
    print(f"Single-threaded {len(links)} times", end=': ')

@calc_time
def crawl_multi_thread(func):
    threads = []
    for link in links:
        threads.append(Thread(target=func, args=(link,)))
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    print(f"Multi-threaded {len(links)} threads", end=': ')

async def crawl_async(link, timeout):
    print(f"crawl started for {link}")
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(link, timeout=timeout) as resp:
            data = await resp.read()
    print(f"crawl ended for {link}")
    return data

@async_calc_time
async def async_main(func):
    timeout = aiohttp.ClientTimeout(total=10)
    async with asyncio.TaskGroup() as group:
        for link in links:
            group.create_task(func(link, timeout))
    print(f"asyncio {len(links)} tasks", end=': ')


if __name__ == '__main__':
    print(f"Is GIL enabled? {sys._is_gil_enabled()}")
    match sys.argv[1:]:
        case ["single"]:
            crawl_single_thread(crawl)
        case ["multi"]:
            crawl_multi_thread(crawl)
        case ["async"]:
            asyncio.run(async_main(crawl_async))
        case _:
            crawl_single_thread(crawl)
            crawl_multi_thread(crawl)
            asyncio.run(async_main(crawl_async))

