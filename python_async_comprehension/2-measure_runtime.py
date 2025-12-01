#!/usr/bin/env python3
""" Module for async comprehension functions"""


import asyncio
import random
import time
from typing import Generator, List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure elapsed time"""
    start_time = time.time()
    # coroutine_objects = [
    #     async_comprehension(),
    #     async_comprehension(),
    #     async_comprehension(),
    #     async_comprehension(),
    # ]
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time
