#!/usr/bin/env python3
""" Module for async functions"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of delays"""
    results = []
    # return list of delays
    for i in range(n):
        num = await asyncio.create_task(wait_random(max_delay))
        results.append(num)
    sorted_results = sorted(results)
    return sorted_results

    # # sort the delays
    # delays = []
    # for result in asyncio.as_completed(results):
    #     delay = await result
    #     delays.append(delay)
    # return delays
