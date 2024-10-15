"""
    Executes async_comprehension four times in parallel and
    measures the total runtime.

    It uses asyncio.gather to run the async_comprehension
    coroutine concurrently
    and returns the time taken to execute all four tasks.

    Returns:
        float: The total runtime in seconds.
"""
import asyncio
import time
from typing import AsyncGenerator, List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel
    and measures the total runtime.

    It uses asyncio.gather to run the async_comprehension
    coroutine concurrently
    and returns the time taken to execute all four tasks.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()
    return end_time - start_time
