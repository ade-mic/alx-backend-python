#!/usr/bin/env python3
"""
Given the parameters and the return values, add type
annotations to the function

Hint: look into TypeVar
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Annotated function that safely gets a value from a dictionary.

    Args:
        dct (Mapping[Any, T]): The dictionary to get the value from.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary if the key is found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
