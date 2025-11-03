import urllib.request
import aiohttp

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

async def crawl_async(link, timeout):
    print(f"crawl started for {link}")
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(link, timeout=timeout) as resp:
            data = await resp.read()
    print(f"crawl ended for {link}")
    return data