#!/usr/bin/env python3
"""
This module defines an asynchronous comprehension that collects
10 random numbers from an asynchronous generator.
"""
from typing import List
# Using __import__ to import async_generator from 0-async_generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator using an
    asynchronous list comprehension and returns them.
    Returns:
        List[float]: A list of 10 random floats generated by async_generator.
    """
    return [i async for i in async_generator()]
