#!/usr/bin/env python3
"""Pagination Module"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Returns a typle containing start and end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Simple Pagination function"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indexes = index_range(page, page_size)
        data = []
        with open('Popular_Baby_Names.csv') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                data.append(row)
        return data[indexes[0]: indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary of hypermedia key-value pairs"""
        start_index, end_index = index_range(page, page_size)

        next_page = None
        if (len(self.dataset()) > end_index):
            next_page = page + 1
            if next_page > int(len(self.dataset())/page_size):
                next_page = None

        prev_page = None
        if (page > 1):
            prev_page = page - 1

        total_pages = int(len(self.dataset())/10)
        if (page_size > 0):
            total_pages = int(len(self.dataset())/page_size)

        hyper_dict = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }

        return hyper_dict
