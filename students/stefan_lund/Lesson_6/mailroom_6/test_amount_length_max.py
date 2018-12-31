#!/usr/bin/env python3
"""
test function utilizing unittest module
"""
import unittest
from mailroom_6_functions import amount_length_max



class MyFuncTestCase(unittest.TestCase):
    """
    test func amount_length_max in mailroom_6_functions.py module,
        returns len of input str + 4 and always >= 15.
    """
    def test_input_match(self):
        """
        test_vals: [list of int]
        """
        test_vals = [
            [1, 2, 3, 4, 5],
            [10, 100, 1000000, 100000, 10000],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [1000, 100, 10, 1]
            ]
        expected = [15, 1000003, 15, 1003]
        for lst, exp in zip(test_vals, expected):
            actual = amount_length_max(lst)
            self.assertEqual(exp, actual)


if __name__ == '__main__':
    unittest.main()
