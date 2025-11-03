import sys
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
import asyncio
import aiohttp

from utils.cpu import count_x
from utils.io import crawl_async, links

app = FastAPI()

@app.get("/cpu")
async def cpu():
    count_x()
    return JSONResponse({"message": "Hello, world!"})

@app.get("/io")
async def io():
    timeout = aiohttp.ClientTimeout(total=10)
    async with asyncio.TaskGroup() as group:
        for link in links:
            group.create_task(crawl_async(link, timeout))
    return PlainTextResponse("Hello, finished crawling")