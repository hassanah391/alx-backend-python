#!/usr/bin/env python3
""" Module 3-tasks"""
import asyncio
from asyncio import Task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Create an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A task object wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
