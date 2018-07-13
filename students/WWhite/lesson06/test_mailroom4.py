#!/usr/bin/env python3

import unittest
import mailroom4


class TestMailroom(unittest.TestCase):

    def setUp(self):
        mailroom4.dict_donations = {
            "bill gates": [25000.00, 3], "john snow": [10.56, 1], "monet holt": [50000.00, 2], "jeff bezos": [123500.09, 3],
            "john wick": [120000.00, 2]
        }

    def tearDown(self):
        pass

    def test_sort_list(self):
        newList = mailroom4.sort_list()
        self.assertEqual("jeff bezos", newList[0][0])
        self.assertEqual("john snow", newList[-1][0])

    def test_add_donation_amount(self):
        mailroom4.add_donation_amount("test person", 1000)
        self.assertIn("test person", mailroom4.dict_donations)

    def test_print_letter(self):
        expected = '''
Dear Bill Gates,

Thank you for your donation of 1000.00, it is very much appreciated.

Kind Regards,
Your Favorite Local Charity
'''
        self.assertEqual(expected, mailroom4.print_letter("bill gates", 1000))


if __name__ == '__main__':
    unittest.main()