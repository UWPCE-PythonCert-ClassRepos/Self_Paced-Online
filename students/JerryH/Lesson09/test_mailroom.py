#!/usr/bin/env python3
import unittest
from collections import defaultdict
import mailroom as mr


# Test Functions:

class TestMailRoom(unittest.TestCase):

    def test_donor(self):
        test_donor = mr.Donor("Victor", "James", [123.45])
        self.assertEqual(test_donor.first, "Victor" )
        self.assertEqual(test_donor.last, "James" )
        self.assertEqual(test_donor.donations, [123.45])
        self.assertEqual(test_donor.full_name, "Victor James" )

        test_donor.add_donation(678.90)
        self.assertEqual(test_donor.donations, [123.45, 678.90] )

    def test_donorbook(self):
        d1 = mr.Donor("Bill", "Gates", [234.22, 45645.24, 43953.09, 98823])
        d2 = mr.Donor("Jeff", "Bezo", [4564.23])
        test_db = mr.DonorBook([d1, d2])
        self.assertEqual(test_db.donors[0].first, 'Bill')
        self.assertEqual(test_db.donors[1].last, 'Bezo')
        self.assertEqual(test_db.donors[0].donations, [234.22, 45645.24, 43953.09, 98823])

        d3 = mr.Donor("Mike", "Dell", [299.09, 26273.67])
        test_db.add_donor(d3)
        self.assertEqual(test_db.donors[2].full_name, 'Mike Dell')
        self.assertEqual(test_db.donors[2].donations, [299.09, 26273.67])

        self.assertEqual(test_db.get_all_donor_names(), ["Bill Gates", "Jeff Bezo", "Mike Dell"])

    def test_group_donations(self):
        d1 = mr.Donor("Mike", "Dell", [299.09, 26273.67])
        test_db = mr.DonorBook([d1])
        self.assertEqual(test_db.group_donations(), [["Mike Dell", 299.09 + 26273.67, 2]])
        d2 = mr.Donor("Bill", "Gates", [234.22, 45645.24, 43953.09, 98823])
        test_db.add_donor(d2)
        self.assertEqual(test_db.group_donations(), [
            ["Bill Gates", 234.22 + 45645.24 + 43953.09 + 98823, 4],
            ["Mike Dell", 299.09 + 26273.67, 2]
            ])
