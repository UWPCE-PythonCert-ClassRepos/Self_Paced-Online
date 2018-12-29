#!/usr/bin/env python3
import os
import unittest
import mail_room_part4 as mr4



class TestMailRoom(unittest.TestCase):

    #---------------------------------------------------------------------
    def test_sum_donation(self):
        donations = [1,2,4,5,6]  # sum should be 18
        expected = 18
        actual = mr4.sum_donation(donations)
        self.assertEqual(actual, expected)


    #---------------------------------------------------------------------
    def test_num_donation(self):
        donations = [1,2,4,5,6]
        expected = 5
        actual = mr4.num_of_donation(donations)
        self.assertEqual(actual, expected)


    #---------------------------------------------------------------------
    def test_avg_donation(self):
        donations = [1,2,4,5,6]
        expected = 3.6
        actual = mr4.sum_donation(donations) / mr4.num_of_donation(donations)
        self.assertEqual(actual, expected)


    #----------------------------------------------------------------------
    def test_letter_file_name(self):
        assert os.path.isfile('Charles Flint.txt')
        assert os.path.isfile('Paul Allen.txt')
        assert os.path.isfile('Steve Jobs.txt')
        assert os.path.isfile('Thomas Edison.txt')
        assert os.path.isfile('William Boeing.txt')


    #-------------------------------------------------------------------------
    def test_add_donation(self):
        mr4.init_donor_list()
        expected = 20000
        mr4.add_donation('Thai', 20000, 'N')
        actual = mr4.list_of_donors['Thai'][0]
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()