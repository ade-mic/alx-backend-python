#!/usr/bin/env python3
"""
    Returns the first element of a sequence if it exists,
    otherwise returns None.

    Parameters:
    lst (Sequence[Any]): A sequence (such as a list or tuple)
    containing elements of any type.

    Returns:
    Union[Any, None]: The first element of the sequence,
    or None if the sequence is empty.

    Example:
    >>> safe_first_element([1, 2, 3])
    1

    >>> safe_first_element([])
    None

    >>> safe_first_element(["apple", "banana", "cherry"])
    'apple'
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
