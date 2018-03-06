from mailroom_v4 import (get_thank_you, get_report_header, quit_program,
                         get_report_row)
import unittest


class MailroomTest(unittest.TestCase):

    def test_exit(self):
        with self.assertRaises(SystemExit):
            quit_program()

    def test_thankyou(self):
        hemingway_text = 'Dear Ernest Hemingway:\nThank you for your'\
            ' generous donation of $40.00.\nI really appreciate your '\
            '3\ndonations to our organization.\nI assure you that your'\
            ' contributions will be put to\ngood use!\n\nRegards,\nBen'

        self.assertEqual(hemingway_text, get_thank_you('Ernest Hemingway'))

    # I refactored the create_report function by splitting
    # out functions that create the report header and report rows,
    # allowing me to unit test those parts of the function. But
    # I'm not if the added complexity is worth it...

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

    # I'm not sure how to test start_program because it doesn't
    # return a value and all functionality is based on user input

    # Same problem for send_thankyou, though test_thankyou ensures
    # that the string used in send_thankyou is as expected. Same
    # deal for send_to_everyone, which writes to files and doesn't
    # return anything
