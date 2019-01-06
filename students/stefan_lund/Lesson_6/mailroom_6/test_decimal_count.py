#!/usr/bin/env python3
"""
test function utilizing unittest module
file: test_is_digit_or_period.py
"""
import unittest
from mailroom_6_functions import decimal_count

class MyFuncTestCase(unittest.TestCase):
    """ amount entered has already been tested with float(input_amount)
        decimal_count throws ValueError if more than two significant decimals
        present in input_amount"""
    def test_input_match(self):
        """ test if assumed correct entries are accepted and all others
            are rejected"""

        test_vals = [
            (1.0, 1.0),
            (1.1, 1.1),
            (1.12, 1.12),
            (1.0000000, 1.0000000),
            (1.123, ValueError),
            (123.123, ValueError),
            (10000.001, ValueError)
            ]

        # decimal_count func expects float input
        for number, expected_val in test_vals:
            try:
                actual = decimal_count(number)
            except ValueError:
                # is this proper or does the assertRaise test have to be done
                    # separately in another module?
                self.assertRaises(ValueError, decimal_count, number)
            else:
                # runs when no Error has been thrown
                self.assertEqual(expected_val, actual)
                # print("good value", expected_val, actual)


if __name__ == '__main__':
    unittest.main()
