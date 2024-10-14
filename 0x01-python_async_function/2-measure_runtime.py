#!/usr/bin/env python3
"""
The module import wait_n
A  measure_time function with integers n and
max_delay as arguments that measures the total
execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures a total execution time for wait_n(n, max_delay)

    Args:
        n(int): number of time to spawn
        max_delay(int): waits for a random delay between 0 and max_delay

    Return:
        float: total_time / n

    """
    s = time.perf_counter()
    delays = asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - s
    return total_time / n
