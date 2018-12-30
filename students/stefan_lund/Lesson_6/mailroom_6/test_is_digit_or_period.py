#!/usr/bin/env python3
"""
test function utilizing unittest module
file: test_is_digit_or_period.py
"""
import unittest
from mailroom_6_functions import is_digit_or_period

class MyFuncTestCase(unittest.TestCase):
    """ assuming the amount is entered as an int or a float with no more than
        two significant decimals as only possible entries"""
    def test_input_match(self):
        """ test if assumed correct entries are accepted and all others
            are rejected"""

        test_vals = ['1', '1.', '1.1', '1.12', '1.0000000',
                     '1.123', '123.123', '10000.001', 'a.']
        expected = [True, True, True, True, True, False, False, False, False]
        # is_digit_or_period func expects string input
        for string_number, expected_bool in zip(test_vals, expected):
            actual = is_digit_or_period(string_number)
            self.assertEqual(expected_bool, actual)


if __name__ == '__main__':
    unittest.main()
