#!/usr/bin/env python3

"""lesson 06, Mail room 4 Assignment - Test file
This file tests all the functions within mail room 4, so that we can ensure the program is working correctly
"""

# import modules and your file that has the functions that we are testing
import unittest
import os
from unittest.mock import patch
from copy import deepcopy
from mailroom4 import list_donors, add_donation, email, sort_dictionary, create_files, quit

# setting up test dictionary for everything
names = ["John Doe", "Jane Anderson", "Carrie Fisher"]
donat = [[100, 1, 300], [200, 2, 400], [1432254.06, 3, 477418.02]]

# use comprehension to zip it up
dons = {names: donat for names, donat in zip(names, donat)}


class TestingMailroom(unittest.TestCase):

    # test list donors
    def test_list_donors(self):
        real = list_donors(dons)
        expected = [item for item in dons]
        self.assertEqual(real, expected)

    # test add donation - new donation, new donor
    def test_add_donation1(self):
        test_dons = deepcopy(dons)
        real = add_donation(test_dons, "Ice T", 1000)
        test_dons["Ice T"] = [1000, 1, 1000]
        self.assertEqual(real, test_dons)

    # test add donation - current donor, using default param
    def test_add_donation2(self):
        test_dons = deepcopy(dons)
        real = add_donation(test_dons, "John Doe", 1000)
        test_dons["John Doe"] = [1100, 2, 550]
        self.assertEqual(real, test_dons)

    # test add donation - current donor, using different number of gifts
    # (changing default)
    def test_add_donation3(self):
        test_dons = deepcopy(dons)
        real = add_donation(test_dons, "John Doe", 800, 2)
        test_dons["John Doe"] = [1800, 3, 600]
        self.assertEqual(real, test_dons)

    # test email output
    def test_email(self):
        real = email("John Doe", 100.00)
        expected = "\nCreating the email: \n\nDear John Doe, \nThank you for your generous donation of $100.00. We appreciate all that you do for us!\n\nBest, \nMail room Assistant\n"
        self.assertEqual(real, expected)

    # test sorted dictionary
    def test_sort_dictionary(self):
        test_dons = deepcopy(dons)
        real = sort_dictionary(test_dons)
        expected = {
            "Carrie Fisher": [
                1432254.06, 3, 477418.02], "Jane Anderson": [
                200, 2, 400], "John Doe": [
                100, 1, 300]}
        self.assertEqual(real, expected)

    # test send all letters
    def test_create_files(self):
        test_dons = deepcopy(dons)
        real = create_files(test_dons)
        self.assertTrue(os.path.exists('John Doe.txt'))
        self.assertTrue(os.path.exists('Jane Anderson.txt'))
        self.assertTrue(os.path.exists('Carrie Fisher.txt'))

    # test quit function
    def test_quit(self):
        # test the quit function actually system exits
        with self.assertRaises(SystemExit) as sysext:
            quit()

        the_exception = sysext.exception
        self.assertEqual(the_exception.code, None)


if __name__ == '__main__':

    # call the main testing function
    unittest.main()
