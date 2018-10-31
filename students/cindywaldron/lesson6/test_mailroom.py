#!/usr/bin/env python3

import unittest
import os
from datetime import date
from mailroom import write_letter, send_letters, update_donor, donors, generate_report

class MyMailRoomTestCase(unittest.TestCase):
    def test_write_letter(self):
        """test letter to donor"""
        donor = ["Cindy", 1000.00]
        expected = ("Dear Cindy,",
                            "\n\n\tThank you for your very kind donation of $1000.00.",
                            "\n\n\tIt will be put to very good use.",
                            "\n\n\t\t\t\tSincerely,",
                            "\n\t\t\t\t-The Team\n")
        # call method
        actual = write_letter(donor[0], donor[1])
        self.assertEqual("".join(expected), actual)

    def test_send_letters(self):
        actual = os.listdir()
        # call method
        send_letters()
        self.assertTrue("Jeff_Bezos-{}.txt".format(str(date.today())) in actual)
        self.assertTrue("Mark_ZuckerBerg-{}.txt".format(str(date.today())) in actual)
        self.assertTrue("Paul_Allen-{}.txt".format(str(date.today())) in actual)
        self.assertTrue("William_Gates_III-{}.txt".format(str(date.today())) in actual)

    def test_update_donor1(self):
        """add new donor"""
        new_donor = ["Cindy", 99.99]
        # call method
        update_donor(new_donor[0], new_donor[1])
        self.assertTrue("Cindy" in donors)
        self.assertEqual([99.99, 1, 99.99], donors["Cindy"])

    def test_update_donor2(self):
        """test existing donor"""
        existing_donor = ["Paul Allen", 1234.45]
        # call method
        update_donor(existing_donor[0], existing_donor[1])
        self.assertEqual([1942.87, 4, 485.7175], donors["Paul Allen"])

    def test_generate_report(self):
        """test repoet"""
        expected = ["--------------------------------------------------------------",
                    "Donor Name           | Total Given | Num Gifts | Average Gift",
                    "--------------------------------------------------------------",
                    "William Gates, III    $  653784.49           2  $   326892.24",
                    "Mark ZuckerBerg       $   16396.10           3  $     5465.37",
                    "Jeff Bezos            $     877.33           1  $      877.33",
                    "Paul Allen            $     708.42           3  $      236.14"
                    ]
        actual = generate_report()
        self.assertEqual("\n".join(expected), actual)

if __name__ == '__main__':
    unittest.main()