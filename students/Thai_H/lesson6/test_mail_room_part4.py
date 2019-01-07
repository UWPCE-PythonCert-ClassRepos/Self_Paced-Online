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


    #-----------------------------------------------------------------------
    def test_file_creation(self):

        mr4.init_donor_list()
        for donor_name in mr4.list_of_donors.keys():
            file_name = donor_name + '.txt'
            total_donation = sum(mr4.list_of_donors[donor_name])
            thks_letter = open(file_name, 'w')
            thks_letter.write('Dear {name}, \n'
                          'Thank you for your generosity to our Foundation in the total amount of ${amt}'.format(name = donor_name,
                                                                                                                 amt = total_donation))
            thks_letter.close()

            assert os.path.isfile(file_name)


    #-------------------------------------------------------------------------
    def test_add_donation(self):
        mr4.init_donor_list()
        expected = 20000
        mr4.add_donation('Thai', 20000, 'N')
        actual = mr4.list_of_donors['Thai'][0]
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()