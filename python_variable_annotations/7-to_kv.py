#!/usr/bin/env python3
"""
Function to_kv that takes a string and a number (int or float)
and returns a tuple with the string and the square of the number as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and a number v (which can be an int or a float),
    and returns a tuple where the first element is the string k,
    and the second element is the square of v as a float.

    Parameters:
    k (str): The key, a string.
    v (Union[int, float]): The value, which can be an integer or a float.

    Returns:
    Tuple[str, float]: A tuple with the string k and the square of v (float).
    """
    return (k, float(v ** 2))
