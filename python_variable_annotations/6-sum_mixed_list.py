#!/usr/bin/env python3
""" Calculate the sum of all numbers in a list of integers and floats. """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of all numbers in a list.
    """
    return sum(mxd_lst)
