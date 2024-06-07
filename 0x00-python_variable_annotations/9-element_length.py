#!/usr/bin/python3
"""
Annotating the below function's parameters and return values
with the appropriate types.
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each containing an element and its length."""
    return [(idx, len(idx)) for idx in lst]
