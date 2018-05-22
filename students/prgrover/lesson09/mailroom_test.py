#!/usr/bin/env python3

import unittest
import os.path
from mailroom import *

class MailroomTest(unittest.TestCase):

    # Tests for Donor class
    def test_donor_class_init(self):
        donor = Donor("Harry")
        expected_name = "Harry"
        actual_name = donor.donor_name
        expected_list = []
        actual_list = donor.donations
        self.assertEqual(expected_name,actual_name)
        self.assertEqual(expected_list,actual_list)

    def test_add_donation(self):
        donor = Donor("Harry")
        donor.add_donation(250.00)
        donor.add_donation(500.00)
        expected = 500.00
        actual = donor.donations[-1]
        self.assertEqual(expected,actual)

    def test_donor_class_properties(self):
        donor = Donor("Draco")
        donor.add_donation(100.00)
        donor.add_donation(200.00)
        donor.add_donation(300.00)
        expected_total = 600.00
        expected_number = 3
        expected_average = 200.00
        actual_total = donor.donation_total
        actual_number = donor.donation_number
        actual_average = donor.donation_average
        self.assertEqual(expected_total,actual_total)
        self.assertEqual(expected_number,actual_number)
        self.assertEqual(expected_average,actual_average)

    # Test for DonorDictionary class
    def test_donordirectory_class_init(self):
        ddir = DonorDirectory()
        expected_list = []
        actual_list = ddir.donor_list
        self.assertEqual(expected_list,actual_list)

    def test_add_donor(self):
        expected_name = "Ron"
        expected_amount = 100.00
        ddir = DonorDirectory()
        donor = Donor(expected_name)
        donor.add_donation(expected_amount)
        ddir.add_donor("Ron", 100.00)
        actual_name = ddir.find_donor(expected_name).donor_name
        self.assertEqual(expected_name,actual_name)

    def test_list_donors(self):
        ddir = DonorDirectory()
        ddir.add_donor("Albus", 1000)
        ddir.add_donor("Severus", 2000)
        ddir.add_donor("Lucius", 3000)
        expected = "Albus\nSeverus\nLucius"
        actual = ddir.list_donors()
        self.assertEqual(expected,actual)

    def test_create_mail(self):
        ddir = DonorDirectory()
        ddir.add_donor("Harry", 500)
        ddir.create_mail_files()
        self.assertTrue('Harry.txt', os.path.exists('Harry.txt'))


if __name__ == '__main__': 
    unittest.main()