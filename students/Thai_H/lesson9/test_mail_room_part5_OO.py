#!/usr/bin/env python3

import unittest
import os.path
import mail_room_part5_OO as mroo
#from mail_room_part5_OO import *


class TestMailroomPart5(unittest.TestCase):

    def test_donor_class(self):
        # donor #1
        test_donor = mroo.Donor('Thai Huynh')
        expected_name = 'Thai Huynh'
        actual_name = test_donor.donor_name
        self.assertEqual(expected_name, actual_name)

        test_donation_amt = 1000
        test_donor.add_donation(test_donation_amt)
        actual_donation = test_donor.donation[-1]
        self.assertEqual(test_donation_amt, actual_donation)

        # test_donor donated 2,0000
        test_donor.add_donation(2000)
        test_donor_count = test_donor.donation_count
        self.assertEqual(2, test_donor_count)
        self.assertEqual(3000, test_donor.donation_total)
        self.assertEqual(1500, test_donor.donation_avg)



    def test_donor_collection(self):

        test_name = 'Thai'
        test_amt = 100

        donor_collection = mroo.DonorCollection()

        donor_1 = mroo.Donor(test_name)
        donor_1.add_donation(test_amt)

        donor_collection.add_donor_donation(test_name, test_amt)

        actual_name = donor_collection.find_donor(test_name).donor_name
        self.assertEqual(test_name, actual_name)


    def test_write_thank_you(self):

        donor_collection = mroo.DonorCollection()
        donor_collection.add_donor_donation('Thai_H', 1234.56)
        donor_collection.write_thank_you_letter()
        self.assertTrue('THAI_H.txt', os.path.exists('THAI_H.txt'))



if __name__ == '__main__':
    unittest.main()