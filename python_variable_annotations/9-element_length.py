#!/usr/bin/env python3
""" Takes an iterable of sequences. """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
