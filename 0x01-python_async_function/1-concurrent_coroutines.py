#!/usr/bin/env python3
""" Module 1-concurrent_coroutines """

import asyncio
from typing import List  # Required for asynchronous programming features

# Dynamically import the `wait_random` coroutine from another file
# This function sleeps for a random amount of time and returns the delay
wait_random = __import__('0-basic_async_syntax').wait_random


# Define an asynchronous function `wait_n`
async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    Returns a list of the delays in ascending order based on completion time.

    Args:
        n (int): number of coroutines to run concurrently
        max_delay (int): maximum delay for each wait_random call

    Returns:
        List[float]: list of delays in the order they completed (ascending)
    """
    # Create a list of n coroutine objects (not awaited yet)
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Initialize a list to hold the completed delay values
    delays = []

    # Iterate over tasks as they complete
    for completed in asyncio.as_completed(tasks):
        delay = await completed  # Wait for completed task to return its delay
        delays.append(delay)     # Add the result to the list

    return delays  # Return the list of delays
