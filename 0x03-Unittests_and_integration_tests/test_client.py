#!/usr/bin/env python3
"""A test suite for github org client
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""

        # Mocked return value from get_json, simulating API response
        mock_get_json.return_value = {"login": org_name}

        # Create an instance of GithubOrgClient with the given org_name
        client = GithubOrgClient(org_name)

        # Call the org property and check its return value
        result = client.org
        self.assertEqual(result, {"login": org_name})

        # Ensure get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")


# Run the tests
if __name__ == "__main__":
    unittest.main()
