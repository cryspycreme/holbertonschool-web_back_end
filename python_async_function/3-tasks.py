#!/usr/bin/env python3
""" Module for async functions"""

import time
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio task and returns it"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
