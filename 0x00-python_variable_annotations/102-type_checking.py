#!/usr/bin/python3
"""
Using mypy to validate the piece of code and
apply any necessary changes.
"""

from typing import Tuple, List, Mapping, Union, Any, TypeVar


T = TypeVar('T')
Res = Union[T, None]
Def = Union[T, None]


def zoom_array(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Given a dictionary and a key, return the value of the key.
    If the key does not exist, return None.
    """
    if key in dct:
        return dct[key]
    else:
        return default
