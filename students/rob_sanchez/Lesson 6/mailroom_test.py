#!/usr/bin/env python3
import unittest
import mailroom_pt4
import os.path


class mailroom_tests(unittest.TestCase):

    # Initial setup of test values
    def setUp(self):
        self.donor_dict = mailroom_pt4.donor_dict

    # Test sum values and donor ascending order
    def test_sum_values(self):
        test_values = {"Bill Gates": [100, 200, 300],
                       "Mark Zuckerberg": [100],
                       "Jeff Bezos": [100, 200]}
        test_compare = {'Bill Gates': 600, 'Jeff Bezos': 300, 'Mark Zuckerberg': 100}
        self.assertDictEqual(test_compare, mailroom_pt4.get_donor_totals(test_values))

    # Test sum values
    def test_num_gifts(self):
        test_values = {"Bill Gates": [100, 200, 300]}
        self.assertDictEqual({'Bill Gates': 3}, mailroom_pt4.get_num_gifts(test_values))

    # Test sum values
    def test_averages(self):
        test_values = {"Bill Gates": [100, 200, 300]}
        self.assertDictEqual({'Bill Gates': 200}, mailroom_pt4.get_averages(test_values))

    # Test that all the text files for the corresponding donors are created
    def test_send_letters(self):
        mailroom_pt4.send_letters()
        for values in self.donor_dict:
            self.assertTrue(os.path.isfile(values + ".txt"))

    # Tests that the list of existing users is correctly formatted
    def test_get_formatted_values(self):
        # Sample formatted list of users
        tst_list = "Tom Cruise, Michael Jordan, Katy Perry, Adam Sandler"
        self.assertEqual(tst_list, mailroom_pt4.get_formatted_values(list(self.donor_dict)))

    # Tests the that the email template is correctly formatted
    def test_send_email(self):
        new_donor = {"donor_name": "Billy Bob",
                     "amount": 2345}

        body = ("\nDear {donor_name},\n\n"
                "I would like to personally thank you for your generours donation "
                "of ${amount} to our charity organization.\nYour support allows us"
                " to continue supporting more individuals in need of our services."
                "\n\nSincerely,\nCharity Inc.\n").format(**new_donor)

        self.assertEqual(body, mailroom_pt4.send_email(new_donor))

    # Tests the that the individual letter template is correctly formatted
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

        self.assertEqual(body, mailroom_pt4.create_letter(new_donor))

    # Test that a new donor is added to the List
    def test_add_donor(self):
        mailroom_pt4.add_donor("Billy Bob", 2345)
        self.assertEqual(mailroom_pt4.donor_dict.get("Billy Bob"), [2345])

    # Test that if donor exists, the donation value is added to the history
    def test_donor_exists(self):
        mailroom_pt4.add_donor("Michael Jordan", 200)
        self.assertListEqual(mailroom_pt4.donor_dict.get("Michael Jordan"), [1300, 200])

    # Reset list of donors
    def tearDown(self):
        donor_dict = {"Tom Cruise": [100, 200, 300],
                      "Michael Jordan": [1300],
                      "Katy Perry": [4500, 1500],
                      "Adam Sandler": [500, 2400]}
        mailroom_pt4.donor_dict.clear()
        mailroom_pt4.donor_dict = donor_dict


if __name__ == '__main__':
    unittest.main()
