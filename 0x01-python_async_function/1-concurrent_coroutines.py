#!/usr/bin/env python3
"""
    Module that import wait_random from the python file and
    write an async routine called wait_n
    that takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.

    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawned wait_random

    Args:
        n (int): number of times to spawned wait_randome
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        List:  list of all the delays (float values).

    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency.
    """
    list_n = [wait_random(max_delay) for i in range(n)]
    delays = [await delay for delay in asyncio.as_completed(list_n)]
    return delays
