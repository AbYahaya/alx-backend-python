#!/usr/bin/env python3
"""
This module provides functions to handle multiple asynchronous coroutines
concurrently, specifically running multiple coroutines that wait for random
delays and return results in a specific order.
"""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_del
    seconds and returns the delay.

    Args:
        max_delay (int): Maximum number of seconds to wait (inclusive)
    Returns:
        float: The actual delay (a float value between 0 and max_delay).
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute `wait_random` n times with the specified max_delay and return
    the list of all the delays in ascending order.

    Args:
    n (int): Number of times to execute the coroutine.
    max_delay (int): Maximum delay for each coroutine.
    Returns:
    List[float]: List of delays in ascending order.
    """

    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
