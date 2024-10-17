#!/usr/bin/env python3
"""
This module defines an asynchronous generator that yields
a random float between 0 and 10 after each second.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that loops 10 times, each time waiting for
    1 second, then yielding a random number between 0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
