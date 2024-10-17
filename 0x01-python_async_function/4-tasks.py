#!/usr/bin/env python3
"""
This module provides a function to execute multiple asyncio tasks
that wait for a random delay and return the results in ascending order.
"""
import asyncio
from typing import List

# Import task_wait_random using __import__
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute `task_wait_random` n times with the specified max_delay and
    return the list of delays in ascending order.
    Args:
        n (int): Number of tasks to execute.
        max_delay (int): Maximum delay for each task.
    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Create n tasks
    delays = await asyncio.gather(*tasks)  # Wait for all tasks to complete
    return sorted(delays)  # Return delays in ascending order
