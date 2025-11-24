#!/usr/bin/env python3
""" Module for type annotations"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multiply the multiplier by a multiplier """
    def scaling_func(x: float):
        """ Function scales the multiplier """
        return x * multiplier
    return scaling_func
