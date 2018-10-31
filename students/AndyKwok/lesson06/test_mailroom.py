# Description: Mailroom Program Tester
# Author: Andy Kwok
# Last Updated: 08/11/2018
# ChangeLog: Initializing

#!/usr/bin/env python3

import unittest
import io
import os
import sys
import mailroom_part4 as atest
from unittest.mock import patch

class test_mailroom_part4(unittest.TestCase):
    def setUp(self):
        self.donor = 'Donor I'
        self.donation = [300.00]
        self.donor2 = 'Donor B'
        self.donation2 = [1.00]           
        self.filelist = ['Donor_A.txt', 'Donor_B.txt', 'Donor_C.txt']
    
    def test_report_select(self):
        expected = {'Donor C': [14349.00, 175.95], 'Donor A': [2300.30, 1000.01, 2000.00], 'Donor B': [1394.12, 1.0], 'Donor I': [300.00]}
        atest.report_select()
        actual = atest.database
        self.assertEqual(expected, actual)
    
    @patch('builtins.input', side_effect=[300.0])
    def test_add_donation_add_new(self, mock):  
        expected = [300.0]
        atest.add_donation(self.donor)   
        actual = atest.database.get(self.donor)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[1.0])
    def test_add_donation_add_exist(self, mock):
        expected = [1394.12, 1.0] 
        atest.add_donation(self.donor2) 
        actual = atest.database.get(self.donor2)
        self.assertEqual(expected, actual)
       
    def test_letters_everyone(self):
        atest.letters_everyone()
        for filename in self.filelist:
            assert os.path.exists(filename) == 1
        
    def test_database_print(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        atest.database_print()
        sys.stdout = sys.__stdout__
        #try comparing the asset?
        print('Print Test Passed...\n', capturedOutput.getvalue())
        
    def test_send_thank_you(self):
        expected =  'To Donor B,' + '\n' + 'Thank you for your donation of $1.00.' + '\n'*2 + '\t'*5 + '-System Generated Email'
        actual = atest.send_thank_you(self.donor2, self.donation2)
        self.assertEqual(expected, actual)
        
    def test_quit_select(self):
        expected = 'quit'
        atest.quit_select()
        actual = atest.option
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
    
