#!/usr/bin/env python3
"""
Augmenting the code with the correct duck-typed annotations.
"""

from typing import Union, Any, Sequence, List, Tuple


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence."""
    if lst:
        return lst[0]
    else:
        return None
