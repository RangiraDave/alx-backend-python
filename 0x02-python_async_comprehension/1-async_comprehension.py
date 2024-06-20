#!/ussr/bin/env python3
"""
Async Comprehensions
"""

import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """
    Coroutine that will yield a random number between 0 and 10
    """
    return [random.uniform(0, 10) for _ in range(10)]
