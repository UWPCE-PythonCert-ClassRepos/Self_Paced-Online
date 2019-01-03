#!/usr/bin/env python3
"""
test function utilizing unittest module
file: test_amount_lengths.py
"""
import unittest
from mailroom_6_functions import amount_lengths


class MyFuncTestCase(unittest.TestCase):
    """
    test func amount_lengths in mailroom_6_functions.py module, returns len of
        input str
    """
    def test_input_match(self):
        """
        test_vals: {"str": [list of float], ....}
        """
        test_vals = {
            'test_a'   : {'total': [1.00]},
            'test_b'   : {'total': [1.0/3]},
            'test_c'   : {'total': [1.1234567890123]},
            'test_d'   : {'total': [3.14159265]},
            'test_e'   : {'total': [2.718281828459045]},
            'test_ab'  : {'total': [1.00, 1.0/3]},
            'test_de'  : {'total': [3.14159265, 2.718281828459045]},
            'test_bcd' : {'total': [1.0/3, 1.1234567890123, 3.14159265]},
            'test_bcde': {'total': [1.0/3, 1.1234567890123, 3.14159265, 2.718281828459045]}
            }

        # data: {"Name1": [list of donations], ....}
        actual = amount_lengths(test_vals)
        for length in actual:
            expected = 4
            self.assertEqual(expected, length)


if __name__ == '__main__':
    unittest.main()
