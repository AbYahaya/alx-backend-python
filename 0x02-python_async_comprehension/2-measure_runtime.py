#!/usr/bin/env python3
"""
This module defines a coroutine that measures the total runtime of
executing async_comprehension four times in parallel.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension 4x in parallel
    Returns:
        float: The total time taken to run async_comprehension 4x in parallel
    """
    start_time = time.perf_counter()
    
    # Run async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    
    end_time = time.perf_counter()
    return end_time - start_time
