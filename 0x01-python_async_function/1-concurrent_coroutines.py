#!/usr/bin/env python3
""" Module 1-concurrent_coroutines"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """
    Spawn wait_random n times with the specified max_delay.
    Returns a list of the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
