#!/usr/bin/env python3
"""
task_wait_random that takes an integer max_delay
and returns a asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine.
    Args:
        max_delay(int): maximum delay
    Returns:
        asyncio.Task: A task that will run the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
