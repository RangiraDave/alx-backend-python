#!/usr/bin/env python3

import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Function that measures the
    total execution time for wait_n(n, max_delay),
    and returns the average time.
    """

    start_time = time.time()
    wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n