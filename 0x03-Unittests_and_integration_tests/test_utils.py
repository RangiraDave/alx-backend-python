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

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """
        Test the access_nested_map function with different inputs that
        should raise an exception.
        args:
            nested_map (dict): The nested map to access.
            path (tuple): The path to the desired value in the nested map.
            expected_output: The expected exception to be raised.

        Returns:
            None
        """

        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test case class for the get_json function.
    """

    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expected_output):
        """
        Test the get_json function with different inputs.

        Args:
            url (str): The URL to fetch JSON from.
            expected_output (dict): The expected JSON output.

        Returns:
            None
        """

        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """
    Test case class for the memoize function.
    """

    def test_memoize(self):
        """
        Test the memoize function.

        Returns:
            None
        """

        class TestClass:
            """
            Test class to test the memoize function.
            """

            def a_method(self):
                """
                A method to test memoization.

                Returns:
                    int: 42
                """

                return 42

            @memoize
            def a_property(self):
                """
                A property to test memoization.

                Returns:
                    int: 42
                """

                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
