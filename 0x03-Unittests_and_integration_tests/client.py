#!/usr/bin/env python3
"""A GitHub organization client for fetching organization and repository data.
"""
from typing import List, Dict
from utils import get_json, access_nested_map, memoize


class GithubOrgClient:
    """A client to interact with a GitHub organization via the GitHub API."""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """
        Initialize the GithubOrgClient with the name of the GitHub organization.

        Args:
            org_name (str): The name of the GitHub organization.
        """
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """
        Fetch and cache the GitHub organization data.

        Returns:
            Dict: The JSON response representing the organization metadata.
        """
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """
        Get the URL for the organization's public repositories.

        Returns:
            str: URL pointing to the list of public repos.
        """
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """
        Fetch and cache the payload of the organization's public repositories.

        Returns:
            Dict: The JSON response containing the list of repository data.
        """
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """
        Get the list of public repositories. Optionally filter by license.

        Args:
            license (str, optional): If provided, only repos with this license are returned.

        Returns:
            List[str]: A list of repository names.
        """
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]
        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """
        Check if the given repository has the specified license.

        Args:
            repo (Dict[str, Dict]): The repository metadata.
            license_key (str): The license key to check for.

        Returns:
            bool: True if the repository uses the specified license, False otherwise.
        """
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license
