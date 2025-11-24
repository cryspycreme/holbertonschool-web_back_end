#!/usr/bin/env python3
""" Module for type annotations"""

from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns the index and length in a Tuple"""
    return [(i, len(i)) for i in lst]
