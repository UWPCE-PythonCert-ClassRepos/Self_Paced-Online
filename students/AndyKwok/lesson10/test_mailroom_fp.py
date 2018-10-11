# Description: Test Mailroom Program - FP 
# Author: Andy Kwok
# last Updated: 10/2/18
# ChangeLog:
# v1.0 - Initialization

import unittest
import mailroom_fp as mail

class Test_DonorInfo(unittest.TestCase):
    def setUp(self):
        mail.DonorInfo.donor_list = [mail.Donor("Test", "Subject", [1,2,3,4,5])]
         
    def test_challenge_map(self):
        mail.DonorInfo.Challenge(2 ,0, 10)
        actual = mail.DonorInfo.donor_list[0].donation_record
        expected = [2,4,6,8,10]
        self.assertEqual(actual, expected)
        
    def test_challenge_reduce(self):
        mail.DonorInfo.Challenge(1 ,2, 3)
        actual = mail.DonorInfo.donor_list[0].donation_record
        expected = [2, 3]
        self.assertEqual(actual, expected)       

    def test_forecast_double(self):
        mail.DonorInfo.donor_list[0].donation_record = [50, 100]
        actual = mail.DonorInfo.Forecast()
        expected = 100
        self.assertEqual(actual[0], expected)  

    def test_forecast_triple(self):
        mail.DonorInfo.donor_list[0].donation_record = [50, 100]
        actual = mail.DonorInfo.Forecast()
        expected = 300
        self.assertEqual(actual[1], expected)  
        
if __name__=="__main__":
    unittest.main()