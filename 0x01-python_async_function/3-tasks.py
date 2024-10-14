#!/usr/bin/env python3
"""
This module provides a function to create and return an asyncio Task
that waits for a random delay.
"""
import asyncio
from 0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task that runs the wait_random coroutine.
    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.
    Returns:
        asyncio.Task: An asyncio task that runs wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
