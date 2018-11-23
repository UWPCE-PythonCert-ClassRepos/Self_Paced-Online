'''
Shin Tran
Python 210
Lesson 9 Assignment
'''

import unittest
from oo_mailroom import Donor
from oo_mailroom import DonorCollection
from io import StringIO


class Test_Oo_Mailroom(unittest.TestCase):

    def test_donor_class(self):
        """Creates a new donor, tests the full name, donation acount, donation total,
        average donation, adds a new donation, and tests the stats again"""
        d1 = Donor("James", "Smith", [33558.77, 30929.47, 27173.01])
        self.assertEqual(d1.full_name, "James Smith")
        self.assertEqual(d1.get_donation_count, 3)
        self.assertEqual(d1.get_donation_total, 91661.25)
        self.assertEqual(d1.get_avg_donation, 30553.75)
        d1.add_donation(10000)
        self.assertEqual(d1.get_donation_count, 4)
        self.assertEqual(d1.get_donation_total, 101661.25)
        self.assertEqual(d1.get_avg_donation, 25415.31)

    def test_donor_list(self):
        """Tests to see if the donor collection class returns a list of donors"""
        name_list = ["John Williams","Robert Jones"]
        d2 = Donor("John", "Williams", [41113.42])
        d3 = Donor("Robert", "Jones", [21067.11, 30160.42])
        donor_dict = {"John Williams": d2, "Robert Jones": d3}
        dc = DonorCollection(donor_dict)
        self.assertEqual(dc.generate_name_list(), name_list)

    def test_email_text(self):
        """User enters "John Smith" and a donation of $67,890,
        method outputs a string email"""
        list1 = ["John", "Smith", 67890]
        message_string = "Dear {:s} {:s},\n\
            Thank you for the generous donation of ${:,.2f}.\n\
            Sincerely,\n\
            Your Local Charity".format(*list1)
        self.assertEqual(Donor.get_email_text(self, list1), message_string)

    def test_print_report(self):
        """Compares the report that gets generate based on the donor list"""
        d1 = Donor("James", "Smith", [15000, 20000, 25000])
        d2 = Donor("John", "Williams", [40000])
        d3 = Donor("Robert", "Jones", [20000, 30000])
        donor_dict = {"James Smith": d1, "John Williams": d2, "Robert Jones": d3}
        dc = DonorCollection(donor_dict)
        s1 = "Donor Name          |   Total Given  |  Num Gifts |  Average Gift\n\
-----------------------------------------------------------------\n\
James Smith          $    60,000.00             3  $    20,000.00\n\
Robert Jones         $    50,000.00             2  $    25,000.00\n\
John Williams        $    40,000.00             1  $    40,000.00\n\
"
        self.assertEqual(dc.generate_report(), s1)

    def test_file_output(self):
        """Compares the thank you letter (txt file) output with the preloaded donor list"""
        donor_list = [["James Smith",91661.25],["Robert Jones",51227.53],["John Williams",41113.42]]
        message = "Dear {:s},\n\
        Thank you for donating ${:,.2f}.\n\
        Sincerely,\n\
        Your Local Charity"
        comp_dict = {}
        for item in donor_list:
            comp_dict[item[0]] = message.format(*item)
        for k, v in comp_dict.items():
            with open (k + ".txt", 'r') as f:
                contents = f.read()
                self.assertEqual(contents, v)