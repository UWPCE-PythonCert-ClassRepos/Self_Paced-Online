#!/usr/bin/env python3
import unittest
import mailroom_pt5
import os.path
from donor_class import Donations
from donor_class import Donor


class mailroom_tests(unittest.TestCase):

    # Test sum values
    def test_sum_values(self):
        donations_list = Donations()

        donations_list.add_donation("Bill Gates", 100)
        donations_list.add_donation("Bill Gates", 200)
        donations_list.add_donation("Bill Gates", 300)

        test_compare = {'Bill Gates': 600}
        self.assertDictEqual(test_compare, donations_list.donation_totals)

    # Test number of values
    def test_num_gifts(self):
        donations_list = Donations()

        donations_list.add_donation("Bill Gates", 100)
        donations_list.add_donation("Bill Gates", 200)
        donations_list.add_donation("Bill Gates", 300)

        test_values = {"Bill Gates": [100, 200, 300]}
        self.assertDictEqual({'Bill Gates': 3}, donations_list.num_donations)

    # # Test average values
    def test_averages(self):
        donations_list = Donations()

        donations_list.add_donation("Jeff Bezos", 100)
        donations_list.add_donation("Jeff Bezos", 200)
        donations_list.add_donation("Jeff Bezos", 300)

        test_values = {"Jeff Bezos": [100, 200, 300]}
        self.assertDictEqual({'Jeff Bezos': 200}, donations_list.avg_donations)

    # # Tests that the list of existing users is correctly formatted
    def test_get_formatted_values(self):
        donations_list = Donations()

        donations_list.add_donation("Tom Cruise", 100)
        donations_list.add_donation("Michael Jordan", 200)
        donations_list.add_donation("Katy Perry", 300)

        tst_list = "List of Donors: Tom Cruise, Michael Jordan, Katy Perry"
        self.assertEqual(tst_list, donations_list.get_formatted_list_of_donors())

    # # Tests the that the email template is correctly formatted
    def test_send_email(self):

        new_donor = {"donor_name": "Billy Bob",
                     "amount": 2345}

        body = ("\nDear {donor_name},\n\n"
                "I would like to personally thank you for your generours donation "
                "of ${amount} to our charity organization.\nYour support allows us"
                " to continue supporting more individuals in need of our services."
                "\n\nSincerely,\nCharity Inc.\n").format(**new_donor)

        self.assertEqual(body, mailroom_pt5.send_email(new_donor))

    # # Tests the that the individual letter template is correctly formatted
    def test_create_letter(self):
        new_donor = {"donor_name": "Billy Bob",
                     "last_donation": 2345,
                     "total": 5432}

        body = ("\nDear {donor_name},\n\n"
                "I would like to personally thank you for your recent "
                "donation of ${last_donation} to our charity organization. "
                "You have donated a total of ${total} as of today. "
                "Your support allows us to continue supporting more individuals "
                "in need of our services."
                "\n\nSincerely,\nCharity Inc.\n").format(**new_donor)

        self.assertEqual(body, mailroom_pt5.create_letter(new_donor))

    # # Test that a new donor and donation are added to the List
    def test_add_donor(self):
        donor_list = Donor()

        donor_list.add_donor("Billy Bob")
        donor_list.add_donation(2345)
        self.assertEqual({'amount': 2345, 'donor_name': 'Billy Bob'}, donor_list.get_donor_details())


if __name__ == '__main__':
    unittest.main()
