#!/usr/bin/env python3

import unittest
from mailroom_6_functions import name_length


class MyFuncTestCase(unittest.TestCase):
    def test_input_match(self):
        test_vals = {'x':1, 'Hi':2, 'Hi Me':5, 'Stefan':6, 'Stefan Lund':11}
        # name_length func expects a dict input but is using only the dict key
        for string, string_length in test_vals.items():
            expected = string_length + 4
            actual = name_length({string:string_length})
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
