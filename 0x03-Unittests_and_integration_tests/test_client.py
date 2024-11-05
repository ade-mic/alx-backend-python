#!/usr/bin/env python3
"""A test suite for github org client
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient """
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json,):
        """Test GithubOrgClient.public_repos
          returns the correct list of repo names."""

        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = mock_repos_payload

        # Mock the _public_repos_url property
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            url = "https://api.github.com/orgs/test_org/repos"
            mock_public_repos_url.return_value = url

            # Call the public_repos method and verify the output
            client = GithubOrgClient("test_org")
            repos = client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Check that _public_repos_url and get_json were called once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_return):
        """unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo=repo,
                                             license_key=license_key)
        self.assertEqual(result, expected_return)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos':TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test Integration GithubOrgClient"""
    @classmethod
    def setUpClass(cls):
        """Set up class method to start patching requests.get"""
        cls.get_patcher = patch('requests.get',
                                side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patching requests.get"""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """Mock function for requests.get"""
        if url == "https://api.github.com/orgs/google":
            return MockResponse(TEST_PAYLOAD[0][0])
        elif url == "https://api.github.com/orgs/google/repos":
            return MockResponse(TEST_PAYLOAD[0][1])
        return MockResponse(None, 404)

    def test_public_repos(self):
        """Test public_repos method without license"""
        self.assertEqual(self.client.public_repos(), TEST_PAYLOAD[0][2])

    def test_public_repos_with_license(self):
        """Test public_repos method with license"""
        self.assertEqual(self.client.public_repos(license="apache-2.0"),
                         TEST_PAYLOAD[0][3])


class MockResponse:
    """
    Mock response class for requests.get
    """
    def __init__(self, json_data, status_code=200):
        """
        Initialize class
        """
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        """json"""
        return self.json_data


# Run the tests
if __name__ == "__main__":
    unittest.main()
