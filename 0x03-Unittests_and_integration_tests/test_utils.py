#!/usr/bin/env python3
""" Module test_utils """
from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import get_json


class TestAccessNestedMap(TestCase):
    """Tests for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ['a'], 1),
        ({"a": {"b": 2}}, ['a'], {"b": 2}),
        ({"a": {"b": 2}}, ['a', 'b'], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map returns the correct value for given path"""
        return self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ['a']),
        ({'a': 1}, ['a', 'b']),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised when path is invalid"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """Tests for the get_json function in utils module"""
    @parameterized.expand([
        ("example", "http://example.com", {"payload": True}),
        ("holberton", "http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, name, test_url, test_payload, mock_get):
        """Test get_json returns correct payload
        without making real HTTP calls"""
        # Configure the mock
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function
        result = get_json(test_url)

        # Assertions
        mock_get.assert_called_once_with(test_url)  # Called once with test_url
        self.assertEqual(result, test_payload)      # Output matches payload
