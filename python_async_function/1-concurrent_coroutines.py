#!/usr/bin/env python3
""" Execute multiple coroutines at the same time with async """
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Function that returns the list """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delay = [await task for task in asyncio.as_completed(tasks)]
    return delay
