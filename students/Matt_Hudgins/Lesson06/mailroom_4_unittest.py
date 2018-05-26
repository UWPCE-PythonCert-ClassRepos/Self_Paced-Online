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
from mailroom_4 import donors


class MailroomTest(unittest.TestCase):

    def donor_list_test(self):
        self.assertEqual(mailroom_4.donor_list(), list(donors))

    def test_adding_a_donor(self):gi
            mailroom_4.adding_a_donor('Matt Hudgins')
            self.assertEqual(list(donors), ['Rick Grimes', 'Shane Walsh', 'Carl Grimes', 'Morgan Jones', 'Matt Hudgins'])


    def test_send_letter(self):
        mailroom_4.send_letter('Matt Hudgins', '40.00')
        self.assertEqual(mailroom_4.send_letter(),'Dear Matt Hudgins,\n Thank you for your donation of $40.00')
        with self.assertRaises(TypeError):
            mailroom_4.send_letter('Matt Hudgins', '40.00')


def test_quit(self):
    self.assertEqual(mailroom_4.quit(), 'exit menu')

if __name__ == '__main__':
    print("Unit Test for mailroom_4 assignment")
    unittest.main()
