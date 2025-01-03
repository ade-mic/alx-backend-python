#!/usr/bin/env python3
"""
A type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function
that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier.

    Args:
        multiplier (float): The float to use as the multiplier.

    Returns:
        Callable[[float], float]: A function that multiplies a float by
        the multiplier.
    """
    return lambda x: x * multiplier
