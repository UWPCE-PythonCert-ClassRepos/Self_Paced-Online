#!/usr/bin/env python3
"""This is a test module that tests mailroom3.py"""

import sys
import unittest
from unittest import mock
from io import StringIO
from collections import defaultdict
import mailroom3 as mr


def redirect_stdout():
    """Redirect stdout to the returned StringIO object.

    Returns:
        StringIO: Object containing redirected stdout.
    """
    redirect = StringIO()
    sys.stdout = redirect

    return redirect


def reset_stdout():
    """Reset stdout back to default"""
    sys.stdout = sys.__stdout__


class TestMailRoom(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_donor_data(self):
        """Tests the init_donor_data() fxn"""

        # Test with default parameter
        ret_dict = mr.init_donor_data()
        self.assertTrue(ret_dict[mr.GIFTS_KEY] == [],
                        ret_dict[mr.GIFTS_KEY])
        self.assertTrue(ret_dict[mr.NUM_GIFTS_KEY] == 0,
                        ret_dict[mr.NUM_GIFTS_KEY])
        self.assertTrue(ret_dict[mr.TOTAL_KEY] == 0,
                        ret_dict[mr.TOTAL_KEY])
        self.assertTrue(ret_dict[mr.AVE_KEY] == 0,
                        ret_dict[mr.AVE_KEY])

        # Test with argument
        gifts = [5, 10, 20, 15]
        ret_dict = mr.init_donor_data(gifts=gifts)
        self.assertTrue(ret_dict[mr.GIFTS_KEY] == gifts,
                        ret_dict[mr.GIFTS_KEY])
        self.assertTrue(ret_dict[mr.NUM_GIFTS_KEY] == 4,
                        ret_dict[mr.NUM_GIFTS_KEY])
        self.assertTrue(ret_dict[mr.TOTAL_KEY] == 50,
                        ret_dict[mr.TOTAL_KEY])
        self.assertTrue(ret_dict[mr.AVE_KEY] == 12.5,
                        ret_dict[mr.AVE_KEY])

    def test_get_usr_input(self):
        """Tests the get_usr_input() fxn"""

        # Test all valid user input prompts
        with mock.patch('builtins.input') as mock_input:
            for prompt in mr.PROMPT_OPTS:
                mock_input.return_value = prompt
                self.assertTrue(mr.get_usr_input() == prompt)

        # Test invalid input type
        se = ['two', 1]
        with mock.patch('builtins.input', side_effect=se) as mock_input:
            captured_print = redirect_stdout()
            mr.get_usr_input()
            reset_stdout()

            self.assertTrue(captured_print.getvalue() == (f'\nPlease try again. '
                                                          f'Valid options are: '
                                                          f'{mr.PROMPT_OPTS}\n'))

        # Test valid input type, but not a valid option
        se = [-5, 1]
        with mock.patch('builtins.input', side_effect=se) as mock_input:
            captured_print = redirect_stdout()
            mr.get_usr_input()
            reset_stdout()

            self.assertTrue(captured_print.getvalue() == (f'\nPlease select a '
                                                          f'number between '
                                                          f'{mr.PROMPT_OPTS[0]}'
                                                          f' and '
                                                          f'{mr.PROMPT_OPTS[-1]}\n'))

    def test_get_donor_names(self):
        """Test the get_donor_names() fxn"""
        test_donor_db = {'Test Donor 1': 'na',
                         'Test Donor 2': 'na',
                         'Test Donor 3': 'na'}
        with mock.patch.dict(mr.donor_db, test_donor_db, clear=True):
            self.assertTrue(mr.get_donor_names() == ['test donor 1',
                                                     'test donor 2',
                                                     'test donor 3'],
                            mr.get_donor_names())

    def test_prompt_for_donor(self):
        """Test the prompt_for_donor() fxn"""

        # Test when user enters a name
        with mock.patch('builtins.input') as mock_input:
            mock_input.return_value = 'mr. test donor'
            result = mr.prompt_for_donor('')

            self.assertTrue(result == 'Mr. Test Donor')

        # Test when user enters "quit"
        with mock.patch('builtins.input') as mock_input:
            mock_input.return_value = 'quit'
            captured_print = redirect_stdout()
            result = mr.prompt_for_donor('')
            reset_stdout()

            self.assertTrue(result is None)
            self.assertTrue(captured_print.getvalue() == '')

        # Test when user enters "list"
        test_donor_db = {'Test Donor 1': 'na',
                         'Test Donor 2': 'na',
                         'Test Donor 3': 'na'}
        se = ['list', 'quit']
        with mock.patch.dict(mr.donor_db, test_donor_db, clear=True):
            with mock.patch('builtins.input', side_effect=se) as mock_input:
                captured_print = redirect_stdout()
                result = mr.prompt_for_donor('')
                reset_stdout()

                self.assertTrue(result is None)
                self.assertTrue(captured_print.getvalue() == ('\nTest Donor 1\n'
                                                              'Test Donor 2\n'
                                                              'Test Donor 3\n'))

    def test_prompt_for_donation(self):
        """Test the prompt_for_donation() fxn"""

        # Test when user enters donation attempts
        se = ['foufty', '50']
        with mock.patch('builtins.input', side_effect=se):
            captured_print = redirect_stdout()
            result = mr.prompt_for_donation('')
            reset_stdout()

            self.assertTrue(result == 50.0, msg=result)
            self.assertTrue(captured_print.getvalue() ==
                            '\nDonation amount must be a number\n')

        # Test when user enters 'quit'
        with mock.patch('builtins.input') as mock_input:
            mock_input.return_value = 'quit'
            captured_print = redirect_stdout()
            result = mr.prompt_for_donation('')
            reset_stdout()

            self.assertTrue(result is None, msg=result)
            self.assertTrue(captured_print.getvalue() == '')

    def test_add_donation(self):
        """Test the add_donation() fxn"""
        mr.donor_db = defaultdict(lambda: mr.init_donor_data(),
                                  {'Test Donor 1': {},
                                   'Test Donor 2': {}})

        # Test adding new donor
        test_results = {mr.GIFTS_KEY: [500],
                        mr.NUM_GIFTS_KEY: 1,
                        mr.TOTAL_KEY: 500,
                        mr.AVE_KEY: 500}
        mr.add_donation('Test Donor 3', 500)
        self.assertTrue(mr.donor_db['Test Donor 3'] == test_results,
                        msg=mr.donor_db['Test Donor 3'])

        # Test adding to existing donor
        test_results = {mr.GIFTS_KEY: [500, 1000],
                        mr.NUM_GIFTS_KEY: 2,
                        mr.TOTAL_KEY: 1500,
                        mr.AVE_KEY: 750}
        mr.add_donation('Test Donor 3', 1000)
        self.assertTrue(mr.donor_db['Test Donor 3'] == test_results,
                        mr.donor_db['Test Donor 3'])

    def test_send_thank_you(self):
        """Test send_thank_you() fxn"""

        # Test output thank you string
        se = ['Bert', '1000']
        with mock.patch('builtins.input', side_effect=se):
            captured_print = redirect_stdout()
            mr.send_thank_you()
            reset_stdout()

            self.assertTrue(captured_print.getvalue() ==
                            mr.THANK_YOU_FMT.format('Bert', 1000) + '\n')

    def test_create_report(self):
        pass

    def test_quit_mailroom(self):
        pass

    def test_send_letters(self):
        pass


if __name__ == '__main__':
    unittest.main()
