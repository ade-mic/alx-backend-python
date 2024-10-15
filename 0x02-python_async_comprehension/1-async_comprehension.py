#!/usr/bin/env python3
"""
Import async_generator from the previous task
a coroutine function async_comprehension no arguments.
The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers.
"""
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[Generator[float, None, None]]:
    """
    Collects 10 random numbers from the async_generator
    using an async comprehension.

    This coroutine asynchronously iterates over the `async_generator`
    to gather 10
    random numbers and returns them as a list.

    Returns:
        List[float]: A list containing 10 random floating-point
        numbers between 0 and 10.
    """

    return [i async for i in async_generator()]
