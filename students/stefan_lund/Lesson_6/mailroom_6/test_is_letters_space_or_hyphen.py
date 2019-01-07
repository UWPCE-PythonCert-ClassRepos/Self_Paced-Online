#!/usr/bin/env python3
"""
test function utilizing unittest module
file: test_is_letters_space_or_hyphen.py
"""
import unittest
from mailroom_6_functions import is_letters_space_or_hyphen


class MyFuncTestCase(unittest.TestCase):
    """
    test func is_letters_space_or_hyphen in mailroom_6_functions.py module,
        returns True or False
    """
    def test_input_match(self):
        """
        test_vals: function expects a string, test_vals is a list of strings
        """
        test_vals = ["Stefan", "Stefan Lund", "Stefan-Lund", "Stefan- Lund",
                     "6tefan", "Stefan.", "St'ef'an.", "Ste&fan."]
        expected = [True, True, True, True, False, False, False, False]

        for string, expected_bool in zip(test_vals, expected):
            actual_bool = is_letters_space_or_hyphen(string)
            self.assertEqual(expected_bool, actual_bool)


if __name__ == '__main__':
    unittest.main()
