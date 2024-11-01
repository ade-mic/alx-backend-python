#!/usr/bin/env python3
"""
TestAccessNestedMap
Description
The TestAccessNestedMap class contains unit tests for
the utils.access_nested_map function.
It inherits from unittest.TestCase and
uses the parameterized.expand decorator to
test multiple input scenarios, including both
successful retrievals and expected exceptions.
"""
from utils import access_nested_map
from utils import get_json
from parameterized import parameterized
import unittest
from unittest.mock import Mock
from typing import Any, Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap
    Description
    The TestAccessNestedMap class contains unit tests for
    the utils.access_nested_map function.
    It inherits from unittest.TestCase and
    uses the parameterized.expand decorator to
    test multiple input scenarios, including both
    successful retrievals and expected exceptions.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_nested_map(self, nested_map: Dict[str, Any],
                        path: Tuple[str, ...], expected: Any) -> None:
        """
        Description: Tests that utils.access_nested_map returns
        the correct value for given inputs.
        Parameters:
                nested_map (Dict[str, Any]): The nested dictionary
                from which to retrieve the value.
                path (Tuple[str, …]): A sequence of keys that
                specifies the path to the desired value in the
                nested dictionary.
                expected (Any): The expected value to be
                  returned by the function.
        Returns: None
        """
        self.assertEqual(access_nested_map(nested_map=nested_map,
                                           path=path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict[str, Any],
                                         path: Tuple[str, ...]) -> None:
        """
        Test that a KeyError is raised for the following inputs
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map=nested_map, path=path)


class TestGetJson(unittest.TestCase):
    """Get Json unittest using Mock"""
    get_json = Mock()

    @parameterized.expand([
       ("http://example.com", {"payload": True}),
       ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test get_json from utils"""
        utils.get_json.return_value = test_payload
        self.assertTrue(get_json(test_url))


if __name__ == '__main__':
    unittest.main()
