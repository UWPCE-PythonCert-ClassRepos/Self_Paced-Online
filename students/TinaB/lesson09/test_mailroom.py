#!/usr/bin/env python3

import unittest
from collections import defaultdict
import donor as dr


class TestDonor(unittest.TestCase):

    def test_donor(self):
        test_donor = dr.Donor("Tina", "Brownfield", [250.25])
        self.assertEqual(test_donor.firstname, "Tina")
        self.assertEqual(test_donor.lastname, "Brownfield")
        self.assertEqual(test_donor.donations, [250.25])
        self.assertEqual(test_donor.fullname, "Tina Brownfield")
        self.assertTrue(test_donor.fullname == "Tina Brownfield",
                        msg=(test_donor.fullname, "Tina Brownfield"))

        test_donor.add_donation(72.75)
        self.assertEqual(test_donor.donations, [250.25, 72.75])
        self.assertTrue(test_donor.donations == [250.25, 72.75], msg=(
            test_donor.donations, [250.25, 72.75]))
        self.assertTrue(test_donor.donation_count() == 2,
                        msg=(test_donor.donation_count(), 2))
        self.assertTrue(test_donor.average_donation() == 161.5,
                        msg=(test_donor.average_donation(), 161.5))
        self.assertTrue(test_donor.donations_total() == 323,
                        msg=(test_donor.donations_total(), 323))

    def test_mailroom_functions(self):
        donor1 = dr.Donor("Steven", "Hawking", [
                          326892.24, 123, 123.33, 123, 123])
        donor2 = dr.Donor("Justin", "Timberlake", [999658.25, 1233, 123])
        test_donorfunctions = dr.DonorFunctions([donor1, donor2])

        donor3 = dr.Donor("Jeff", "Bezos", [52636.27])
        test_donorfunctions.add_donor(donor3)

        self.assertEqual(test_donorfunctions.donorslist[1].lastname, 'Timberlake')
        self.assertEqual(test_donorfunctions.donorslist[0].firstname, 'Steven')

        self.assertEqual(test_donorfunctions.donorslist[0].donations, [
                         326892.24, 123, 123.33, 123, 123])

        self.assertEqual(
            test_donorfunctions.donorslist[2].fullname, 'Jeff Bezos')
        self.assertEqual(
            test_donorfunctions.donorslist[2].donations, [52636.27])

        self.assertEqual(test_donorfunctions.get_all_donors(), [
            "Steven Hawking", "Justin Timberlake", "Jeff Bezos"])


if __name__ == '__main__':
    unittest.main()
