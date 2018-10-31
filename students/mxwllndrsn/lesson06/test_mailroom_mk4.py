#!/usr/bin/env/ python3

#uw python 210
#lesson 05
#max anderson

#mailroom_mk4_tests.py
#unit tests

import os
import unittest
from mock import patch
import mailroom_mk4 as mailroom

class MailroomTest(unittest.TestCase):


    #test default dict against known k/v and defaulting k/v
    def test_dictionary(self):
        self.assertEqual(mailroom.donor['Andrew Jackson'], [10000, 5, 2000])
        self.assertEqual(mailroom.donor['Not inDict'], [0, 0, 0])
        del mailroom.donor['Not inDict']


    def test_donor_list(self):
        self.assertEqual(mailroom.list_donors(),
                         ['Andrew Jackson', 'Benjamin Franklin',
                         'John Kennedy', 'Abraham Lincoln', 'Jim Jones'])


    #test entry updating with defaulting k/v and again as existing k/v
    def test_entry_update(self):
        self.assertEqual(mailroom.entry_update('Not inDict', 10), [10, 1, 10])
        self.assertEqual(mailroom.entry_update('Not inDict', 15), [25, 2, 12.50])
        del mailroom.donor['Not inDict']


    #assert file open and thank you letter formatting successful
    def test_prompt_thx(self):
        with patch('builtins.input', return_value = 'y'):
            self.assertEqual(mailroom.prompt_thx('Andrew Jackson'), None)


    def test_sort_donations(self):
        self.assertEqual(mailroom.sort_donations()[0][0], 'Benjamin Franklin')

    #test letters generated
    def test_generate_letters(self):
        with patch('builtins.input', return_value = 'y'):
            mailroom.generate_letters()
            self.assertTrue('Andrew Jackson_Thanks_081418.txt',
                os.path.exists('Andrew Jackson_Thanks_081418.txt'))


if __name__ == "__main__":

    unittest.main()