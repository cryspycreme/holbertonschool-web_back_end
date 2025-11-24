#!/usr/bin/env python3
""" Module for type annotations"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Calculates the sum of int and floats """
    return sum(mxd_lst)
