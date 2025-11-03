import asyncio
import httpx
import sys
import requests
from concurrent.futures import ThreadPoolExecutor

from utils.utils import calc_time, async_calc_time

FLASK_PORT = 8001
FASTAPI_PORT = 8002

@calc_time
def sync_bench(url: str, total=20, workers=10):
    def worker():
        r = requests.get(url)
        return r.status_code

    with ThreadPoolExecutor(max_workers=workers) as ex:
        results = list(ex.map(lambda _: worker(), range(total)))
    print(f"Completed {len(results)} requests")

@async_calc_time
async def async_bench(url: str, total=20, workers=10):
    sem = asyncio.Semaphore(workers)
    counter = 0
    async with httpx.AsyncClient(timeout=10.0) as client:
        async def worker():
            nonlocal counter
            async with sem:
                r = await client.get(url)
                if r.status_code == 200:
                    counter += 1
        tasks = [asyncio.create_task(worker()) for _ in range(total)]
        await asyncio.gather(*tasks)
        print(f"Completed {counter} requests")


if __name__ == '__main__':
    print(f"Is GIL enabled? {sys._is_gil_enabled()}")
    match sys.argv[1:]:
        case ["sync", "cpu"]:
            sync_bench(f"http://127.0.0.1:{FLASK_PORT}/cpu")
        case ["sync", "io"]:
            sync_bench(f"http://127.0.0.1:{FLASK_PORT}/io")
        case ["async", "cpu"]:
            asyncio.run(async_bench(f"http://127.0.0.1:{FASTAPI_PORT}/cpu"))
        case["async", "io"]:
            asyncio.run(async_bench(f"http://127.0.0.1:{FASTAPI_PORT}/io"))
        case _:
            print("_")
