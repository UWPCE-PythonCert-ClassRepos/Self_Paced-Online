#!/usr/bin/env python3

import mailroom4
import unittest
from unittest.mock import patch
import os


class TestMailRoom(unittest.TestCase):
    
    # Create "known values" or equivalent to setUp(self)

    def setUp(self):
        """Test SetUp
            Set Up the donor_db before each test
            This is called before every single test to initialize donor_db
        """
        mailroom4.init_db()

    # Clean up after everytime testing
    def tearDown(self):
        """
            Tear Down
            Clear up all the extra .txt thank you note get sent
        """
        for file in os.listdir( os.getcwd()):
             if '.txt' in file:  os.remove(file)

    def test_is_donor_in_list(self):
        """ 
            Test to see if "REAL" donor is in the list regardless how it was written
        """
        # test donor is already in list
        expected = (True, "Kate Spade")
        result = mailroom4.is_donor_in_list("Kate Spade")
        self.assertTrue( expected, result)
        
        # test donor NOT already in list
        expected = (False, "New Person" )
        result = mailroom4.is_donor_in_list("New Person")
        self.assertTrue( expected, result)


    def test_enter_dn_name(self):
        """
        Test Enter Donor Name 
        """
        def input_mock(self):
            return 'Michael Kors'
        mailroom4.input_func = input_mock
        got_dn_name = mailroom4.enter_dn_name()
        assert got_dn_name == 'Michael Kors'


    def test_enter_dn_gift(self):
        """
        Test Enter Gift from donor
        Only accept input as number
        or "quit" to back to main menu
        """
        def input_mock(self):
            return 80

        mailroom4.input_func = input_mock
        got_dn_gift= mailroom4.enter_dn_gift()
        #enter_dn_gift use input_func
        #mailroom4.main use input
        #in mailroom4.main declare 
        assert got_dn_gift == 80
    

    def test_add_donation(self):
        """
        Test the add_donation 
        """

        # test add new donor
        golden_donors_db = {
            'Lily Maycat': [5000],
            'Lulu Lemon': [5000, 5000],
            'Marc Jacobs': [5000, 5000, 5000],
            'Bobbi Brown': [5000, 5000, 5000, 5000],
            'Kate Spade': [5000, 5000, 5000, 5000, 5000],
            'Dragron Four': [300] #new donor to test
        }

        mailroom4.add_donation("Dragron Four", 300)
        assert mailroom4.donors_db == golden_donors_db

        # test add the old name + gift
        golden_donors_db['Kate Spade'].append(300)
        mailroom4.add_donation( 'Kate Spade', 300)
        assert mailroom4.donors_db == golden_donors_db


    def test_init_db(self):
        """
            Make sure the data was created right
        """
        #print('test_check_db: %s', mailroom4.donors_db)
        golden_donors_db = {
            'Lily Maycat': [5000],
            'Lulu Lemon': [5000, 5000],
            'Marc Jacobs': [5000, 5000, 5000],
            'Bobbi Brown': [5000, 5000, 5000, 5000],
            'Kate Spade': [5000, 5000, 5000, 5000, 5000],
        }
        result = mailroom4.init_db()
        self.assertTrue(golden_donors_db , result)



    def test_get_donor_info_by_name(self):
        """
            Test get_donor_infor_by_name
        """
        #print('test_check_db: %s', mailroom4.donors_db)
        dn_db = {
            'Lily Maycat': [5000],
            'Lulu Lemon': [5000, 5000],
            'Marc Jacobs': [5000, 5000, 5000],
            'Bobbi Brown': [5000, 5000, 5000, 5000],
            'Kate Spade': [5000, 5000, 5000, 5000, 5000],
        }
        expected = ['Bobbi Brown', 
                     sum(dn_db['Bobbi Brown']), 
                     len(dn_db['Bobbi Brown']),
                     sum(dn_db['Bobbi Brown'])/len(dn_db['Bobbi Brown'])]

        result = mailroom4.get_dn_info_by_name('Bobbi Brown')
        assert expected == result
 
    
    def test_send_thank(self):
        """
            Test send thank you note
                 - get donor naem
                 - get dn gift
                 - add donor to database
                 check string of send thank you note
        """
        global mock_call
        mock_call = 0
        def input_mock(self):
            global mock_call
            if mock_call == 0:
                mock_call += 1
                return 'Joe Moe'
            else:
                return '80'

        mailroom4.input_func = input_mock
        mailroom4.send_thank()

        #print(mailroom4.donors_db)
        expected = {
            'Lily Maycat': [5000],
            'Lulu Lemon': [5000, 5000],
            'Marc Jacobs': [5000, 5000, 5000],
            'Bobbi Brown': [5000, 5000, 5000, 5000],
            'Kate Spade': [5000, 5000, 5000, 5000, 5000, 300],
            'Joe Moe': [80.0]
        }
        assert mailroom4.donors_db == expected

    def test_create_report(self):
        """
            Test Creat Report
            - print string of report
            - Remove all the space and compare
        """
        expected = (
        '\tDonor Name                              |    Total Give |    Num Gifts |   Average Gift\n'
	'\t________________________________________ ______________   ____________   ______________\n'
	'\tKate Spade                              $           25300            6   $4216.666666666667\n'
	'\tBobbi Brown                             $           20000            4   $        5000.0\n'
	'\tMarc Jacobs                             $           15000            3   $        5000.0\n'
	'\tLulu Lemon                              $           10000            2   $        5000.0\n'
	'\tLily Maycat                             $            5000            1   $        5000.0\n'
        )
        report = mailroom4.create_report()
        assert(report.replace(' ', '').replace('\n', '').replace('\t', '') ==
               expected.replace(' ', '').replace('\n', '').replace('\t', ''))

    def test_send_letter(self):
        mailroom4.send_letters()

        def check_file(file_name):
            state = 0
            with open(file_name, 'r') as infile:
                for line in infile.readlines():
                    if state == 0 and line.startswith('Dear '):
                        state += 1
                    elif state == 1 and line.startswith(
                         'Thank you for your current generous donations: '):
                        state += 1
                    elif state == 2 and line.startswith('This will be put to good use. '):
                        state += 1
                    elif state == 3 and line.startswith('Thanks'):
                        state += 1
            assert state == 4


        num_files = 0
        for file in os.listdir( os.getcwd()):
             if '.txt' in file:
                 num_files += 1
                 check_file(file)

        assert num_files > 0

if __name__ == '__main__':
    unittest.main()

