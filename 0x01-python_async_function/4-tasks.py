#!/usr/bin/env python3
""" Module 4-tasks"""
import asyncio
from asyncio import Task
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple asyncio tasks concurrently and return their results.

    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of delays (float values)
        in the order of task completion.
    """
    # Create a list of n coroutine objects (not awaited yet)
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Initialize a list to hold the completed delay values
    delays = []

    # Iterate over tasks as they complete
    for completed in asyncio.as_completed(tasks):
        delay = await completed  # Wait for completed task to return its delay
        delays.append(delay)     # Add the result to the list

    return delays  # Return the list of delays
