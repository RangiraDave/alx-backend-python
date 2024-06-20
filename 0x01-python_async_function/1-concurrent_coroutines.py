#!/usr/bin/env python3

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that takes in two integer
    arguments (n: int and max_delay: int)
    named wait_n that spawns wait_random n times
    with the specified max_delay.
    """

    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    delays.sort()

    return delays
