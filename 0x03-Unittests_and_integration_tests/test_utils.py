#!/usr/bin/env python3
"""
Module containing unit tests for the access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with different inputs.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path to the desired value in the nested map.
            expected_result: The expected result of accessing the nested map.

        Returns:
            None
        """

        self.assertEqual(
            access_nested_map(nested_map, path),
            expected_result
        )

        @parameterized.expand([
                ({}, ("a",), KeyError("Key not found: 'a'")),
                ({"a": 1}, ("a", "b"), KeyError("Key not found: 'b'"))
            ])
        def test_access_nested_map_exception(
                self, nested_map, path, expected_exception):
            """
            Test that a KeyError is raised when accessing a
            non-existent key in the nested map.

            Args:
                nested_map (dict): The nested map to access.
                path (tuple): The path to the non-existent
                key in the nested map.
                expected_exception (KeyError): The expected
                exception to be raised.

            Returns:
                None
            """

            with self.assertRaises(KeyError) as context:
                access_nested_map(nested_map, path)
