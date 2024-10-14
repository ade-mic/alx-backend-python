#!/usr/bin/env python3
"""
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay time in seconds.

    This coroutine waits for a random delay between 0 and
    max_delay seconds (inclusive) and then returns the delay time.
"""
import random
import asyncio



async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay time in seconds.

    This coroutine waits for a random delay between 0 and
    max_delay seconds (inclusive) and then returns the delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
