#!/usr/bin/env python
import unittest
from unittest import mock
from io import StringIO

import mailroom4


class TestMailRoom(unittest.TestCase):
    def test_menu_selection(self):
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            text = ('\nbadinput is not a valid selection. '
                    'Please try again!\n')
            with mock.patch('builtins.input', side_effect=['badinput', 'q']):
                mailroom4.menu_selection(mailroom4.main_prompt,
                                         mailroom4.main_dict)
            self.assertEqual(text, mock_stdout.getvalue())

    def test_exit_menu(self):
        self.assertEqual(mailroom4.exit_menu(), 'Exit Menu')

    def test_donor_and_amount(self):
        with mock.patch('builtins.input', side_effect=['paUl aLLen', 20.65]):
            mailroom4.donor_and_amount()
            result = mailroom4.data_dict.get('Paul Allen')
            self.assertEqual(result, [17.38, 20.65])

        with mock.patch('builtins.input', side_effect=['tEst NaME', 17.38]):
            mailroom4.donor_and_amount()
            result = mailroom4.data_dict.get('Test Name')
            self.assertEqual(result, [17.38])

    def test_amount_input(self):
        with mock.patch('builtins.input', side_effect=['badinput', '3']):
            with mock.patch('sys.stdout', new_callable=StringIO) as \
                 mock_stdout:
                result = mailroom4.amount_input()
                self.assertEqual('\nPlease enter dollar '
                                 'amount and NOT text!\n',
                                 mock_stdout.getvalue())
            self.assertEqual(result, 3)

    def test_summarized_donation(self):
        result = mailroom4.summarize_donation()
        self.assertEqual(result[0].get('donor_name'), 'William Gates III')

    def test_format_letter(self):
        text = ('Dear Test Name,\n\n'
                '    Thank you for your very kind donation of $25.00.\n\n'
                '    It will be put to very good use.\n\n'
                '                   Sincerely,\n'
                '                   -The Team')
        self.assertEqual(mailroom4.format_letter('Test Name', 25), text)


if __name__ == '__main__':
    unittest.main()
