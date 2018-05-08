#!/usr/bin/env python3

# Lesson 06: Mailroom: Part 4, With Unit Testing
# Natalie Rodriguez
# April 22, 2018


import unittest
import mailroom_part4 as mailroom
import os

class MailroomTest(unittest.TestCase):

    def donor_utest(self):
        mailroom.donors = {'Luke Rodriguez':[12.75, 50.31, 42.59]}

    def test_report(self):
        report = mailroom.create_report()

    def test_thank_all(self):
        assert os.path.isfile('River Tails.txt')

    def test_create_form_letter_1(self):
        assert mailroom.create_form_letter('Virginia Ferdinand', 1000)

    def test_create_form_letter_2(self):
        assert mailroom.create_form_letter('Luke Rodriguez', 88.89)


if __name__ == '__main__':
    unittest.main()