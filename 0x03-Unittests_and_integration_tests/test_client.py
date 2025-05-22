#!/usr/bin/env python3
"""Module test_client"""
from client import GithubOrgClient
from unittest import TestCase
from unittest.mock import PropertyMock, patch
from parameterized import parameterized


class TestGithubOrgClient(TestCase):
    """ Tests for GithubOrgClient class in client module"""
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, get_json_mock):
        """test org method"""
        # Create expected return value
        expected_payload = {"org": org_name}

        # Configure mocked object
        get_json_mock.return_value = expected_payload

        # Create an instance from GithubOrgClient class
        client = GithubOrgClient(org_name)
        # Call org method
        result = client.org

        # Assert get_json was called correctly and returned the mock payload
        get_json_mock.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
            )
        self.assertEqual(result, expected_payload)

    def test_public_repos_url(self):
        """ test public_repos_url property"""
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock)\
                as mock_public_repos:
            payload = {"repos_url": "https://api.github/orgs/org/repos"}
            mock_public_repos.return_value = payload
            client = GithubOrgClient("org")
            result = client._public_repos_url
            self.assertEqual(result, payload["repos_url"])
