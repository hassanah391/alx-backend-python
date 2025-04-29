#!/usr/bin/env python3
""" Module 2-measure_runtime """

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of executing wait_n.

    Args:
        n (int): The number of coroutines to run concurrently.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average runtime per coroutine.
    """
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    elapsed = end - start
    return elapsed / n
