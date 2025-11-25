#!/usr/bin/env python3
""" Module for async functions"""


import asyncio
import random


async def wait_random(max_delay: int = 10):
    """Waits for random delay and returns it"""
    delay = random.uniform(0, max_delay)
    return float(delay)
