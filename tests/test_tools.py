import asyncio
import time

import pytest as pytest

from tools import run_task


@pytest.fixture(scope='session')
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
def queue():
    return asyncio.Queue()


@pytest.mark.asyncio
async def test_run_task(queue):
    # We start a coroutine that runs inside the event loop
    await run_task(queue)


@pytest.mark.asyncio
async def test_check_task_work(queue):
    # In this coroutine test from the first test, the
    # proof is still running - we get the current time from the queue
    # It is at this moment that we can get side effects
    start_time = time.time()
    while True:
        if await queue.get() > start_time:
            break
