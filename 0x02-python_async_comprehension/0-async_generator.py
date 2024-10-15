#!/usr/bin/env python3
"""
The async_generator coroutine function generates
a sequence of 10 random numbers between 0 and 10,
with a 1-second delay between each number.
It uses Python's random module to generate
the random numbers and asyncio.sleep to introduce
the asynchronous delay.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
        A coroutine that asynchronously generates 10 random numbers
        between 0 and 10.

        The function loops 10 times, and in each iteration:
            - Asynchronously waits for 1 second.
            - Yields a random floating-point number between 0 and 10.

        Returns:
            AsyncGenerator[float, None]: Yields random numbers
            one at a time, each after a 1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
