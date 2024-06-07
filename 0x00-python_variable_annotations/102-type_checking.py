#!/usr/bin/env python3
"""
Using mypy to validate the piece of code and
apply any necessary changes.
"""

from typing import Tuple, List, Mapping, Union, Any, TypeVar


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Given a tuple, return a list with the same elements,
    but with each element repeated by factor.
    """
    zoomed_in: List = []
    for item in lst:
        zoomed_in += [item] * factor
    return zoomed_in


arr = (12, 72, 91)
zoom2x = zoom_array(arr)
zoom3x = zoom_array(arr, 3)
