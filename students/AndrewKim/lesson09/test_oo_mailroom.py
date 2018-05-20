#!/usr/bin/env python3
import unittest
from collections import defaultdict
import oo_mailroom as om


# Test Functions:

class TestMailRoom(unittest.TestCase):

    def test_donor(self):
        test_donor = om.Donor("Manu", "Ginobili", [10.0])
        self.assertEqual(test_donor.donations, [10.0])
        self.assertEqual(test_donor.full_name, "Manu Ginobili" )

        test_donor.add_donation(8.0)
        self.assertEqual(test_donor.donations, [10.0, 8.0] )

    def test_donor_history(self):
        d1 = om.Donor("Andrew", "Kim", [5.0, 3.0])
        d2 = om.Donor("Jamie", "Park", [4.0])
        test_dh = om.DonorHistory([d1, d2])
        self.assertEqual(test_dh.get_all_donor_names(), ["Andrew Kim", "Jamie Park"])
        d3 = om.Donor("Tim", "Duncan", [3.0])
        test_dh.add_donor(d3)
        self.assertEqual(test_dh.get_all_donor_names(), ["Andrew Kim", "Jamie Park", "Tim Duncan"])
        self.assertEqual(test_dh.donors[0].donations, [5.0, 3.0])
        self.assertEqual(test_dh.donors[1].first, 'Jamie')
        self.assertEqual(test_dh.donors[1].last, 'Park')
        self.assertEqual(test_dh.donors[0].full_name, 'Andrew Kim')

if __name__ == '__main__':
    unittest.main()