#!/usr/bin/python3
"""
Adding a type annotation to the function,
given a parameter and return values.
"""

from typing import Union, Any, TypeVar, Mapping


T = TypeVar('T')
Res = Union[T, None]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Given a dictionary and a key, return the value of the key.
    If the key does not exist, return None.
    """
    if key in dct:
        return dct[key]
    else:
        return default
