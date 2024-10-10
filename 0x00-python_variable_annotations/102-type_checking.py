#!/usr/bin/env python3
"""
    Function that takes a list of integers and a factor, and returns a new list
    where each element in the original list is repeated 'factor' times.

    Args:
        lst (List[int]): The list of integers to be zoomed.
        factor (int, optional): The factor by which to zoom
        the list. Defaults to 2.

    Returns:
        List[int]: The zoomed list.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Function that takes a list of integers and a factor, and returns a new list
    where each element in the original list is repeated 'factor' times.

    Args:
        lst (List[int]): The list of integers to be zoomed.
        factor (int, optional): The factor by which to zoom the list.
        Defaults to 2.

    Returns:
        List[int]: The zoomed list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(tuple(array))
zoom_3x = zoom_array(tuple(array), 3)
