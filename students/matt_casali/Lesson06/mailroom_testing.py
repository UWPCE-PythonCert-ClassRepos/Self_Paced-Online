#!/usr/bin/env python3

import unittest, os, datetime
from mailroom_4 import donors, list_donors, make_report, send_all_letters
now = datetime.datetime.now()

class MailroomTest(unittest.TestCase):
    donors = {"William Gates, III": [326892.23, 326892.25], "Mark Zuckerberg": [500.00, 800.00, 2.00],
              "Jeff Bezos": [877.33],
              "Paul Allen": [750.23, 23.53, 999.99], "Dakota Dakota": [10.00, 100.00, 1000.00]}

    def test_donors_list(self):
        donor_list = "William Gates, III, Mark Zuckerberg, Jeff Bezos, Paul Allen, Dakota Dakota"
        self.assertEqual(list_donors(donors), donor_list)


    def test_report(self):
        expected_report = "          Donor Name        | Total Given | Num Gifts | Average Gift\n" \
                          "     William Gates, III       653,784.48        2       326,892.24\n"\
                          "         Paul Allen            1,773.75         3       591.25\n" \
                          "      Mark Zuckerberg          1,302.00         3       434.00\n" \
                          "       Dakota Dakota           1,110.00         3       370.00\n" \
                          "         Jeff Bezos             877.33          1       877.33\n"

        assert expected_report == make_report(donors)


    # test_path variable will need to be changed for user performing test
    def test_letters(self):
        send_all_letters(donors)
        test_path = r"D:\\"
        assert os.path.isfile(test_path + f"William_Gates,_III_{now.year}_{now.month:0>2d}_{now.day:0>2d}" + ".txt")
        assert os.path.isfile(test_path + f"Mark_Zuckerberg_{now.year}_{now.month:0>2d}_{now.day:0>2d}" + ".txt")
        assert os.path.isfile(test_path + f"Jeff_Bezos_{now.year}_{now.month:0>2d}_{now.day:0>2d}" + ".txt")
        assert os.path.isfile(test_path + f"Paul_Allen_{now.year}_{now.month:0>2d}_{now.day:0>2d}" + ".txt")
        assert os.path.isfile(test_path + f"Dakota_Dakota_{now.year}_{now.month:0>2d}_{now.day:0>2d}" + ".txt")


if __name__ =='__main__':
    MailroomTest