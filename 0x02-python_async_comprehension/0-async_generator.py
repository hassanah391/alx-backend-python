#!/usr/bin/env python3
""" Module 0-async_generator

This module contains an asynchronous generator function `async_generator`
that yields random floating-point numbers between 0 and 10. The function
sleeps for 1 second before yielding each number.
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronous generator that yields 10 random floats between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
