#!/usr/bin/env python3
""" Module test_utils """
from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import get_json
from utils import memoize


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
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Test the get_json method to ensure it returns the expected output.

        Args:
            test_url: URL to send the fake HTTP request to
            test_payload: Expected JSON response from the mocked request
        """

        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """Tests for the memoize function"""
    def test_memoize(self):
        """Test memoize decorator"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()
