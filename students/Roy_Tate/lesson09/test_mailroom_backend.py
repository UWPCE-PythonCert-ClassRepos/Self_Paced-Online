#!/usr/bin/python3

## Author/Student:  Roy Tate (githubtater)

import unittest
import mailroom_backend as mb
import os, os.path


class TestMailroomBackend(unittest.TestCase):

    def setUp(self):
        self.collection = mb.DonorCollection()
        self.collection.add('Fred Flintstone', 999)
        self.collection.add('Fred Flintstone', 1000)
        self.collection.add('Wilma Willbanks', 23380)
        self.collection.add('Barney Rubble' , 90300)
        self.collection.add('Barney Rubble' , 287100)
        self.collection.add('Barney Rubble' , 2323)
        self.collection.add('Barney Rubble' , 7673324)


    def test_donor_collection_instance_created(self):
        assert isinstance(self.collection, mb.DonorCollection)

    def test_donor_can_be_added(self):
        self.collection.add('Tommy Tommerson', 1400)
        self.assertIn('Tommy Tommerson', self.collection.donors)

    def test_str_function_returns_expected_value(self):
        self.assertEqual((str(self.collection.donors['Fred Flintstone'])), self.collection.donors['Fred Flintstone'].__str__())

    def test_verify_file_is_saved(self):
        with self.assertRaises(FileNotFoundError):
            self.collection.save_emails('/asdfasd/asdfasdfasdsf')

        with self.assertRaises(PermissionError):
            self.collection.save_emails('/root/')
        cur_dir = os.getcwd()
        self.collection.save_emails(cur_dir)

        read_file = open('Fred Flintstone.txt')
        self.assertEqual(read_file.read(), str(self.collection.donors['Fred Flintstone'].letter))
        read_file.close()
        if os.path.isfile('Fred Flintstone.txt'):
            pass
        else:
            raise FileNotFoundError

    def test_max_donations_returned(self):
        max_donation = self.collection.donors['Barney Rubble'].max_donation
        self.assertEqual(max_donation, 7673324)

    def test_total_donations_returned(self):
        total_donations = self.collection.donors['Barney Rubble'].total_donations
        self.assertEqual(total_donations, 8053047)

    def test_num_gifts_returned(self):
        num_gifts = self.collection.donors['Barney Rubble'].num_gifts
        self.assertEqual(num_gifts, 4)


    def test_donations_are_added(self):
        self.collection


if __name__=="__main__":
    unittest.main()