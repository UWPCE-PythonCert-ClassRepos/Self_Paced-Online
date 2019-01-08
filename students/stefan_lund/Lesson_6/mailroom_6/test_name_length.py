#!/usr/bin/env python3
"""
test function utilizing unittest module
file: test_name_length.py
"""

import unittest
from mailroom_6_functions import name_lengths


class MyFuncTestCase(unittest.TestCase):
    """
    test func name_lengths in mailroom_6_functions.py module, returns a list of
        lengths of input strings
    """

    def test_input_match(self):
        """ use the function name_lengths to make a list representing the len of
                the input strings in test_vals
        """
        test_vals = {
            "first": {'x':1, 'Hi':2, 'Hi Me':5, 'Stefan':6, 'Stefan Lund':11},
            "second": {'thank':5, 'you':3, 'for':3, 'choosing':8},
            "third": {'thank':5, 'for':3, 'choosing':8, 'your agent':10}
            }

        for string_dict in test_vals.values():
            expected = list(string_dict.values())
            actual = name_lengths(string_dict)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
