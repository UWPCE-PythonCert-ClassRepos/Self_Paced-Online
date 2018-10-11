# ------------------------------------------------- #
# Title: Lesson 6, pt 2/2, Mail room 4 test
# Dev:   Craig Morton
# Date:  9/8/2018
# Change Log: CraigM, 9/8/2018, Mail room 4 test
# ------------------------------------------------- #

# !/usr/bin/env python3

import datetime
import unittest
from unittest.mock import patch
from unittest.mock import mock_open
import mailroom4


class MailRoomUnitTest(unittest.TestCase):
    donors = dict()
    donors[("Jane", "Doe")] = {"donations": [25]}
    donors[("Richard", "Doe")] = {"donations": [30, 60]}

    def test_get_total(self):
        donor_data = ["John Doe", 2, 3, 4]
        result = mailroom4.get_total(donor_data)
        self.assertEqual(result, 2)

    def test_create_row(self):
        data = {"donations": [20, 30, 40]}
        expected = ["John Doe", 90, 3, 30]
        result = mailroom4.create_row(("John", "Doe"), data)
        self.assertEqual(result, expected)

    @patch('mailroom4.get_name', side_effect=["John", "Doe"])
    def test_get_full_name(self, mock_get_name):
        expected = mailroom4.get_full_name(self.donors)
        self.assertEqual(("John", "Doe"), expected)

    @patch('mailroom4.input', side_effect=["list", "John"])
    @patch('mailroom4.print')
    def test_get_name(self, mock_print, mock_input):
        donor_name = mailroom4.get_name("name: ", self.donors)
        self.assertEqual(donor_name, "John")

        for d in self.donors:
            d_name = "{0} {1}".format(*d)
            mock_print.assert_any_call(d_name)

    @patch('mailroom4.input', side_effect=["testing", "1,531"])
    @patch('mailroom4.print')
    def test_get_donation_amount(self, mock_print, mock_input):
        amount = mailroom4.get_donation_amount()
        self.assertEqual(amount, 1531)

    @patch('mailroom4.get_full_name', side_effect=[("Hello", "World"), ("Richard", "Doe")])
    @patch('mailroom4.get_donation_amount', return_value=50)
    @patch('mailroom4.print')
    def test_send_thank_you(self, mock_print, mock_donation, mock_name):
        mailroom4.send_thank_you(self.donors)
        self.assertTrue(("Hello", "World") in self.donors)
        self.assertEqual(self.donors[("Hello", "World")]["donations"], [50])
        mailroom4.send_thank_you(self.donors)
        self.assertEqual(self.donors[("Richard", "Doe")]["donations"], [30, 60, 50])

    @patch('mailroom4.print')
    def test_create_report(self, mock_print):
        expected = list()
        expected.append("Donor Name    | Total Given   | Num Gifts | Average Gift")
        expected.append("\n")
        expected.append("--------------------------------------------------------")
        expected.append("\n")
        expected.append("Richard Doe     $        90.00           2  $       45.00\n")
        expected.append("Jane Doe        $        25.00           1  $       25.00\n")
        mailroom4.create_report(self.donors)
        mock_print.assert_called_with('\n', ''.join(expected))

    @patch('mailroom4.datetime')
    @patch('mailroom4.os.mkdir')
    @patch('mailroom4.open', new_callable=unittest.mock.mock_open, read_data="{firstname} {lastname} {amount} {total}")
    @patch('mailroom4.print')
    def test_send_letters_everyone(self, mock_print, mock_files, mock_mkdir, mock_now):
        mock_now.now.return_value = "2018-03-02 11:41:52.454554"
        mailroom4.send_letters_everyone(self.donors)
        mock_mkdir.assert_called_with('2018-03-02 11_41_52.454554')
        handle = mock_files()
        for name, donations in self.donors.items():
            gifts = donations["donations"]
            donor_file = "{0} {1} {last:.2f} {total:.2f}".format(*name, last=gifts[-1], total=sum(gifts))
            handle.write.assert_any_call(donor_file)


if __name__ == '__main__':
    unittest.main()
