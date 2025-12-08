#!/usr/bin/env python3
"""Pagination Module"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a typle containing start and end index"""
    offset = (page - 1) * page_size
    limit = offset + page_size
    return (offset, limit)
