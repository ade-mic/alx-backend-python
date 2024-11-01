#!/usr/bin/env python3
"""
test for utils
"""
from utils import access_nested_map
import utils
from parameterized import parameterized
import unittest
from unittest.mock import Mock


class TestAccessNestedMap(unittest.TestCase):
    """test for  utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_nested_map(self, nested_map, path, expected):
        """test nested map function"""
        self.assertEqual(access_nested_map(nested_map=nested_map, path=path),
                         expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a", 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
         test that a KeyError is raised for
           the following inputs
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map=nested_map, path=path)


class TestGetJson(unittest.TestCase):
    """Get Json unittest using Mock"""
    utils.get_json = Mock()

    @parameterized.expand([
       ("http://example.com", {"payload": True}),
       ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test get_json from utils"""
        utils.get_json.return_value = test_payload
        self.assertTrue(utils.get_json(test_url))


if __name__ == '__main__':
    unittest.main()
