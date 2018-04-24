#!/usr/bin/python3

# Author/Student:  Roy Tate (githubtater)

import unittest
import mailroom4
import os


class MailroomTests(unittest.TestCase):
    # build the initial donor dict (this is same initial dict as mailroom4.py)
    donor_dict = {}
    donor_dict['Bill'] = [1100, 2100, 3100]
    donor_dict['Mark'] = [1000, 300000.23, 2000]
    donor_dict['Jeff'] = [50, 450.355]
    donor_dict['Roy'] = [4500, 7500, 11221, 30232, 323]

    # Sum the donations and verify they exist in the donor report
    def test_correct_sums_printed_in_report(self):
        for donor, donations in self.donor_dict.items():
            assert str(donor) in mailroom4.create_report()

    # We want to ensure our signature appears as intended
    # This also ensures that nothing appears after our signature
    def test_verify_output_file_has_correct_signature(self):
        output_file = 'Roy.txt'
        signature = 'The good guys at the best organization'
        with open(output_file, 'r') as f:
            lines = f.readlines()
            self.assertEqual(signature, lines[-1].strip())

    def test_add_donation_new_donor(self):
        name = 'BillyBobHexagon'
        donation = 7000
        # add the new donor to the list
        donation_list = mailroom4.add_donation(name, donation)
        # The list returned should contain our new donor
        assert 'BillyBobHexagon' in donation_list
        # Ensure the new donation was appended
        assert donation_list[name] == [donation]

    def test_add_donation_existing_donor(self):
        name = 'Roy'
        donation = 112233445566
        # add the new donor to the list
        donation_list = mailroom4.add_donation(name, donation)
        # Ensure the new donation was appended
        assert donation in donation_list[name]

    def test_single_email_output(self):
        simple_email = 'To: {0}\n' \
                       'Donation amount: ${1:.2f}'
        print(mailroom4.print_email(simple_email, 'George', 7000))

    def test_correct_list_returned_from_print_list(self):
        output = mailroom4.print_list()
        assert 'Roy' in output
        assert type(output) is list

    def test_verify_all_donor_names_included_in_report(self):
        report_text = mailroom4.create_report()
        for name in self.donor_dict.keys():
            assert name in report_text

if __name__ == "__main__":
    unittest.main()