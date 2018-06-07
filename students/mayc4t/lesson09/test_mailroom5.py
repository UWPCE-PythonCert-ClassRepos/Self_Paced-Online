#!/usr/bin/env python

# #############################################################################
# Written By: Mayc4t
# June 03, 2018
# Self-paced Python
# lesson 9
# fileID: test_mailroom5.py
# #############################################################################


import mailroom5 as mr
import unittest


class TestMailroom(unittest.TestCase):

    # test DONOR CLASS
    def test_dn_donations(self):
        dn = mr.Donor("Test", "Person", [100, 100, 100])
        self.assertEqual(dn.donations, [100, 100, 100])

    def test_dn_name(self):
        dn = mr.Donor("Test", "Person", [100, 100, 100])
        self.assertEqual(dn.name, "Test Person")

    def test_dn_total_donation(self):
        dn = mr.Donor("Test", "Person", [100, 100, 100])
        self.assertEqual(dn.total_donation, 300)

    def test_dn_avg(self):
        dn = mr.Donor("Test", "Person", [100, 100, 100])
        self.assertEqual(dn.avg, 100)

    def test_dn_sort_by_total(self):
        dn = mr.Donor("Test", "Person", [100, 100, 100])
        self.assertEqual(dn.total_donation, 300)

    # def test_dn_str (self):
        #dn = mr.Donor("Test", "Person", [100, 100, 100])
        # self.assertEqual(,)

    def test_dn_add_donation(self):
        dn = mr.Donor("Test", "Person", [100, 100, 100])
        dn.add_donation(60)
        self.assertEqual(dn.donations, [100, 100, 100, 60])
        self.assertEqual(dn.avg, 90)
        self.assertEqual(dn.total_donation, 360)

    # test DONOR_db CLASS
    # def test_dn (self):
    #     pass
    # def test_dn (self):
    #     pass
    # def test_dn (self):
    #     pass

    def test_dndb_names(self):
        d1 = mr.Donor("Apple", "First", [10, 10])
        d2 = mr.Donor("Mango", "Second", [5, 5])
        db = mr.Donor_DB([d1, d2])
        expected_names = ["Apple First", "Mango Second"]
        self.assertEqual(db.names, expected_names)

    def test_dndb_add_donations_to_existname(self):
        d1 = mr.Donor("Apple", "First", [10, 10])
        d2 = mr.Donor("Mango", "Second", [5, 5])
        db = mr.Donor_DB([d1, d2])

        d3 = mr.Donor("Fashion", "Shoes", [2000, 2000])
        db.add_donation(d3)

        exp_names = ["Apple First", "Mango Second", "Fashion Shoes"]
        self.assertEqual(db.names, exp_names)

    def test_dndb_add_new_donor(self):
        d1 = mr.Donor("Apple", "First", [10, 10])
        d2 = mr.Donor("Mango", "Second", [5, 5])
        db = mr.Donor_DB([d1, d2])

        d3 = mr.Donor("Apple", "First", [2000, 2000])
        db.add_donation(d3)

        exp_names = ["Apple First", "Mango Second"]
        self.assertEqual(db.names, exp_names)


if __name__ == "__main__":
    unittest.main()
