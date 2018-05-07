#!/usr/bin/env python3

import unittest
from mailroom import list_donors, add_new_donor, get_donation, donor_dict

class MailroomTest(unittest.TestCase):
    def test_add_new_donor(self):
        add_new_donor('Albus Dumbledore')
        self.assertTrue("Albus Dumbledore" in donor_dict)

    def test_list_donors(self):
        self.assertEqual(list_donors(),'Harry Potter\nRonald Weasley\nHermione Granger\nDraco Malfoy\nNeville Longbottom\nAlbus Dumbledore')

#    def test_get_donation(self):


 



if __name__ == '__main__': 
    unittest.main()