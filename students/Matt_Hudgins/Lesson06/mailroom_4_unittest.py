#!/usr/bin/env python3

# chmod +x mailroom_4_unittest.py needs to be performed before executable

'''
    File Name: mailroom_4_unittest.py
    Author: Matt Hudgins
    Date created: 5/20/18
    Date last modified: 5/24/18
    Python Version 3.6.4
'''

import unittest
import mailroom_4


class MailroomTest(unittest.TestCase):

    def donor_list_test(self):
        self.asserEqual(mailroom_4.donor_list(), {'Rick Grimes': [5.00, 10.00, 2.00],
            'Shane Walsh': [4.00, 10.00, 9.00], 'Carl Grimes':
            [72.00, 10.00, 88.00], 'Morgan Jones': [68.00, 10.00, 98.00]})


    def test_adding_a_donor(self):
        mailroom_4.adding_a_donor('Matt Hudgins')
        self.assertEqual(mailroom_4.donor_list(), {'Rick Grimes': [5.00, 10.00, 2.00],
            'Shane Walsh': [4.00, 10.00, 9.00], 'Carl Grimes':
            [72.00, 10.00, 88.00], 'Morgan Jones': [68.00, 10.00, 98.00],
            'Matt Hudgins': []})


    def test_send_letter(self):
        self.assertEqual(mailroom_4.send_letter('Matt Hudgins', 40.00),'Dear Matt Hudgins,\n Thank you for you donation of $40.00')


if __name__ == '__main__':
    print("Unit Test for mailroom_4 assignment")
    unittest.main()
