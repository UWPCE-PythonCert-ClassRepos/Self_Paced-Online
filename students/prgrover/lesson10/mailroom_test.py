#!/usr/bin/env python3

import unittest
import os.path
import copy
from mailroom_fp import *

class MailroomTest(unittest.TestCase):

    def test_get_total_donations(self):
        expected = 2965.00
        self.assertTrue(expected, get_total_donations(donor_dict))

    def test_multiply_donations(self):
        expected = (2965.00 * 3)
        new_donor_dict = copy.deepcopy(donor_dict)
        multiply_donations(3, new_donor_dict)
        self.assertTrue(expected, get_total_donations(new_donor_dict))

    def test_get_donor(self):
        expected = "Tom Riddle"
        self.assertTrue(expected, get_donor())

    def test_get_donation(self):
        expected = 500.00
        self.assertTrue(expected, get_donation())

    def test_add_new_donor(self):
        add_new_donor('Albus Dumbledore')
        donor_dict['Albus Dumbledore'] = [100.00]
        self.assertTrue('Albus Dumbledore' in donor_dict)

    def test_list_donors(self):
        self.assertEqual(list_donors(),'\nHarry Potter\nRonald Weasley\nHermione Granger\nDraco Malfoy\nNeville Longbottom\nAlbus Dumbledore')

    def test_add_donation(self):
        add_donation('Harry Potter', 12345.67)
        self.assertEqual(12345.67,donor_dict["Harry Potter"][-1])

    def test_create_mail_file(self):
        create_mail_file()
        self.assertTrue('Draco Malfoy.txt', os.path.exists('Draco Malfoy.txt'))

    def test_filter_donations(self):
        expected = {
            "Harry Potter": [10, 20, 30],
            "Ronald Weasley": [],
            "Hermione Granger": [50],
            "Draco Malfoy": [5],
            "Neville Longbottom": [],
            "Albus Dumbledore": []
            }
        new_donor_dict = copy.deepcopy(donor_dict)
        self.assertEqual(expected, filter_donations(0, 100, new_donor_dict))

    def test_challenge(self):
        temp_dict = {
            "Harry Potter": [10, 20, 30],
            "Ronald Weasley": [],
            "Hermione Granger": [50],
            "Draco Malfoy": [5],
            "Neville Longbottom": [],
            "Albus Dumbledore": []
            }
        expected = (get_total_donations(temp_dict) * 4)
        self.assertEqual(expected, get_total_donations(challenge(4, 0, 100, donor_dict)))

if __name__ == '__main__': 
    unittest.main()