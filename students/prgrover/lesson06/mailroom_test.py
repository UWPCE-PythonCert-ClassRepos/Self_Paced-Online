#!/usr/bin/env python3

import unittest
import os.path
from mailroom import list_donors, add_new_donor, add_donation, create_email_file, donor_dict

class MailroomTest(unittest.TestCase):
    def test_add_new_donor(self):
        add_new_donor('Albus Dumbledore')
        donor_dict['Albus Dumbledore'] = [100.00]
        self.assertTrue('Albus Dumbledore' in donor_dict)

    def test_list_donors(self):
        self.assertEqual(list_donors(),'Harry Potter\nRonald Weasley\nHermione Granger\nDraco Malfoy\nNeville Longbottom\nAlbus Dumbledore')

    def test_add_donation(self):
        add_donation('Harry Potter', 12345.67)
        self.assertEqual(12345.67,donor_dict["Harry Potter"][-1])

    def test_create_email_file(self):
        create_email_file()
        self.assertTrue('Draco Malfoy.txt', os.path.exists('Draco Malfoy.txt'))


if __name__ == '__main__': 
    unittest.main()