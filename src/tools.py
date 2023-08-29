import asyncio
import time


async def loop_func(queue: asyncio.Queue):
    while True:
        await queue.put(time.time())
        await asyncio.sleep(1)


async def run_task(queue: asyncio.Queue):
    loop = asyncio.get_running_loop()
    loop.create_task(loop_func(queue))
