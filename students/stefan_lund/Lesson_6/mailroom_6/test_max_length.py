#!/usr/bin/env python3
"""
test function utilizing unittest module
"""
import unittest
from mailroom_6_functions import max_length



class MyFuncTestCase(unittest.TestCase):
    """
    test func max_length in mailroom_6_functions.py module,
        return represents the max value in the input list or if the len(string)
        is larger, this number is returned.
    function has evolved and the module name should be changed to test_max_length
    """
    def test_input_match(self):
        """
        test_vals: [[list of int], "string"]
        """
        test_vals = [
            [[1, 2, 3, 4, 5], "Donor Name"],
            [[1, 2, 3, 4, 5], "Name"],
            [[10, 100, 1000000, 100000, 10000], "Donor Name"],
            [[10, 100, 1000000, 100000, 10000], "Name"],
            [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], "Donor Name"],
            [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], "Name"],
            [[1000, 100, 10, 1], "Donor Name"],
            [[1000, 100, 10, 1], "Name"]
            ]
        expected = [10, 5, 1000000, 1000000, 10, 4, 1000, 1000]
        for lst, exp in zip(test_vals, expected):
            actual = max_length(*lst)
            self.assertEqual(exp, actual)


if __name__ == '__main__':
    unittest.main()
