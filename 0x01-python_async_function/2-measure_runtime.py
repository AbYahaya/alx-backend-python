#!/usr/bin/env python3
"""
This module provides a function to measure the average runtime of
executing multiple asynchronous coroutines.
"""
import time
import asyncio
from 1_concurrent_coroutines import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return the
    average time per coroutine.
    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.
    Returns:
        float: The average runtime per coroutine.
    """
    start_time = time.time()  # Record start time
    await wait_n(n, max_delay)  # Run the async function
    total_time = time.time() - start_time  # Calculate total execution time
    return total_time / n  # Return average time per coroutine
