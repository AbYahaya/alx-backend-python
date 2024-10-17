#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine that waits for a random
delay between 0 and a specified max_delay, then returns the actual delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_del
    Args:
        max_delay (int): Maximum number of seconds to wait (inclusive)
    Returns:
        float: The actual delay (a float value between 0 and max_delay).
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)  # Pause execution for 'delay' seconds
    return delay  # Return the actual delay value
