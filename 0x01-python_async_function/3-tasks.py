#!/usr/bin/env python3

import asyncio
from typing import Any


wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> Any:
    """
    Function that takes in an integer
    argument (max_delay, with a default value of 10)
    named task_wait_random that waits for a random delay
    between 0 and max_delay
    (included and float value) seconds and eventually returns it.
    """

    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
