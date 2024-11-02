#!/usr/bin/env python3
"""A test suite for github org client
"""
import unittest
from unittest.mock import patch, PropertyMock
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

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_public_repos_url(self, org_name, mock_get_json):
        """Test GithubOrgClient._public_repos_url
        returns the correct URL.
        """
        # Define the expected repos_url based on the org_name
        mock_org_repo_url = f"https://api.github.com/orgs/{org_name}/repos"

        # Set the return value of the get_json mock
        mock_get_json.return_value = {"repos_url": mock_org_repo_url}

        client = GithubOrgClient(org_name)
        # Patch the org property within the context of this test
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_get_json.return_value = {"repos_url": mock_org_repo_url}
        # Assert that _public_repos_url returns
        # the correct repos_url from the payload
        self.assertEqual(client._public_repos_url, mock_org_repo_url)

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('utils.get_json')
    def test_public_repos(self, org_name, mock_get_json):
        """Test GithubOrgClient.public_repos
        returns the correct repo names."""

        # Define the expected repos_url based on the org_name
        mock_org_repo_url = f"https://api.github.com/orgs/{org_name}/repos"

        # Define a mock payload for repos
        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
        ]

        # Set the return value of the get_json mock
        mock_get_json.return_value = mock_repos_payload

        client = GithubOrgClient(org_name)

        # Patch the _public_repos_url property within the context of this test
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            # Set the return value of the mocked _public_repos_url property
            mock_public_repos_url.return_value = mock_org_repo_url

            # Call public_repos and check if it returns the correct repo names
            repos = client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2"])

            # Ensure _public_repos_url and get_json are called correctly
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_org_repo_url)


# Run the tests
if __name__ == "__main__":
    unittest.main(verbosity=2)
