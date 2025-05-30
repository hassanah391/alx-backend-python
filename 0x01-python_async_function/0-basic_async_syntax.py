#!/usr/bin/env python3
""" Module 0-basic_async_syntax"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
