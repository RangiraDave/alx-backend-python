#!/usr/bin/env python3
"""
Measure the runtime
"""

import asyncio
import random
import time
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that measures the total execution time for wait_n
    """
    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
