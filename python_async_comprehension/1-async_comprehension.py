#!/usr/bin/env python3
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension
    over async_generator, and then returns the list of these numbers.
    """
    return [i async for i in async_generator()]
