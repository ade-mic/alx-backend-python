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
import utils
from parameterized import parameterized
import unittest
from utils import memoize
from unittest.mock import patch
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
    def test_access_nested_map(self, nested_map: Dict[str, Any],
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

    @parameterized.expand([
       ("http://example.com", {"payload": True}),
       ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get_json):
        """test get_json from utils"""
        mock_get_json.return_value = test_payload
        self.assertEqual(utils.get_json(test_url), test_payload)
        mock_get_json.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """test memoize decorator"""
    def test_memoize(self):
        """test memoie"""


        class TestClass:

            def a_method(self):
                return 42
            @memoize
            def a_property(self):
                return self.a_method()


        test_instance = TestClass()
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
