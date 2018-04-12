from mailroom_v4 import (get_thank_you, get_report_header, quit_program,
                         get_report_row)
import unittest
from collections import defaultdict
import mailroom_v4


class MailroomTest(unittest.TestCase):

    def test_exit(self):
        with self.assertRaises(SystemExit):
            quit_program()

    def test_get_thank_you_single_donation(self):
        mailroom_v4.donor_info = defaultdict(list, {'test donor':
                                                    [100]})
        test_text = 'Dear test donor:\nThank you for your'\
            ' generous donation of $100.00.\nI really appreciate your '\
            '1\ndonation to our organization.\nI assure you that your'\
            ' contributions will be put to\ngood use!\n\nRegards,\nBen'

        self.assertEqual(test_text, get_thank_you('test donor'))

    def test_get_thank_you_multiple_donations(self):
        hemingway_text = 'Dear Ernest Hemingway:\nThank you for your'\
            ' generous donation of $40.00.\nI really appreciate your '\
            '3\ndonations to our organization.\nI assure you that your'\
            ' contributions will be put to\ngood use!\n\nRegards,\nBen'

        self.assertEqual(hemingway_text, get_thank_you('Ernest Hemingway'))

    def test_report_header(self):
        expected_header = 'Donor Name      |Total Given |Num Gifts '\
                          '|Average Gift'
        self.assertEqual(get_report_header(16), expected_header)

    def test_report_row(self):
        expected_row = 'John Steinbeck  |$   55.50   |    3     '\
                       '|$ 18.50  '
        self.assertEqual(get_report_row(('John Steinbeck',
                                        [25.5, 20, 10]), 16),
                         expected_row)
