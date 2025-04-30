#!/usr/bin/env python3
"""Module 2-measure_runtime

This module contains the `measure_runtime` coroutine function, which
measures the total runtime of executing the `async_comprehension` function
four times concurrently using `asyncio.gather`.
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of running async_comprehension
    4 times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
