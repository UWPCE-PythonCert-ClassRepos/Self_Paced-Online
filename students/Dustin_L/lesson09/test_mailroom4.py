#!/usr/bin/env python3
"""This is a test module that tests mailroom4.py"""

import datetime
import os
import random
import sys
from io import StringIO

import unittest
from unittest import mock

import mailroom4 as mr
from mailroom4 import PROMPT_OPTS, Donor, DonorDatabase


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


class TestDonor(unittest.TestCase):
    """Unit tests for the Donor class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_name = 'Test Donor'
        self.test_dons = [100, 500, 50.05]
        self.test_total = sum(self.test_dons)
        self.test_ave = self.test_total / len(self.test_dons)

    def setUp(self):
        self.donor = Donor(self.test_name, self.test_dons)

    def tearDown(self):
        pass

    def test_get_donations(self):
        """Test donations attribute"""
        self.assertEqual(self.donor.donations, self.test_dons)

    def test_set_donations(self):
        """Test setting donations attribute"""
        with self.assertRaises(AttributeError):
            self.donor.donations = [100, 20]

    def test_get_num_donations(self):
        """Test num_donations attribute"""
        self.assertEqual(self.donor.num_donations, len(self.test_dons))

    def test_set_num_donations(self):
        """Test setting num_donations attribute"""
        with self.assertRaises(AttributeError):
            self.donor.num_donations = 4

    def test_get_total_donations(self):
        """Test total_donations attribute"""
        self.assertEqual(self.donor.total_donations, self.test_total)

    def test_set_total_donations(self):
        """Test setting total_donations attribute"""
        with self.assertRaises(AttributeError):
            self.donor.total_donations = 100

    def test_get_ave_donations(self):
        """Test average_donations attribute"""
        self.assertEqual(self.donor.average_donations, self.test_ave)

    def test_set_ave_donations(self):
        """Test setting average_donations attribute"""
        with self.assertRaises(AttributeError):
            self.donor.average_donations = 100

    def test_add_donation(self):
        """Test add_donation method"""
        donation = random.randint(0, 10000.0)
        self.donor.add_donation(donation)
        self.assertEqual(self.donor.donations, self.test_dons + [donation])
        self.assertEqual(self.donor.num_donations, len(self.test_dons) + 1)
        self.assertEqual(self.donor.total_donations, self.test_total + donation)
        self.assertEqual(self.donor.average_donations,
                         (self.test_total + donation) / (len(self.test_dons) + 1))


class TestDonorDatabase(unittest.TestCase):
    """Unit tests for the DonorDatabase class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.d1_name = 'Test Donor 1'
        self.d2_name = 'Test Donor 2'
        self.d3_name = 'Test Donor 3'
        self.d1_dons = [1000, 5000, 10000]
        self.d2_dons = [12000, 5000, 27000]
        self.d3_dons = [38734, 6273, 67520]

    def setUp(self):
        self.db = DonorDatabase(*[Donor(self.d1_name, self.d1_dons),
                                  Donor(self.d2_name, self.d2_dons),
                                  Donor(self.d3_name, self.d3_dons)])

    def tearDown(self):
        # Remove any added thank you letters
        files = os.listdir(os.getcwd())
        for f in files:
            if f.startswith('Test_Donor'):
                os.remove(os.path.join(os.getcwd(), f))

    def test_add_donor(self):
        """Test adding donor not currently in database"""
        d4 = 'Test Donor 4'
        self.assertEqual(self.db[d4].name, d4)

    def test_create_report(self):
        """Test create_report() fxn"""
        report_lines = self.db.create_report().split('\n')

        self.assertEqual(report_lines[0], '')
        self.assertEqual(report_lines[1], '   Donor Name     | Total Given  |  Num Gifts   | Average Gift')
        self.assertEqual(report_lines[2], '--------------------------------------------------------------')
        self.assertEqual(report_lines[3], 'Test Donor 3      | $  112527.00 |            3 | $   37509.00')
        self.assertEqual(report_lines[4], 'Test Donor 2      | $   44000.00 |            3 | $   14666.67')
        self.assertEqual(report_lines[5], 'Test Donor 1      | $   16000.00 |            3 | $    5333.33')

    def test_send_letters(self):
        """Test send_letters() fxn"""
        now = datetime.datetime.today().strftime('%m-%d-%Y')
        self.db.send_letters()
        files = os.listdir()

        # Check the file names are correct
        self.assertTrue(f'Test_Donor_1_{now}.txt' in files)
        self.assertTrue(f'Test_Donor_2_{now}.txt' in files)
        self.assertTrue(f'Test_Donor_3_{now}.txt' in files)

        # Check the file contents are correct
        with open(f'Test_Donor_1_{now}.txt', 'r') as f:
            contents = f.read(105)
            self.assertEqual(contents, self.db.thank_you_fmt.format(
                'Test Donor 1', 16000))

        with open(f'Test_Donor_2_{now}.txt', 'r') as f:
            contents = f.read(105)
            self.assertEqual(contents, self.db.thank_you_fmt.format(
                'Test Donor 2', 44000))

        with open(f'Test_Donor_3_{now}.txt', 'r') as f:
            contents = f.read(106)
            self.assertEqual(contents, self.db.thank_you_fmt.format(
                'Test Donor 3', 112527))

    def test_get_donor_names(self):
        """Test reading all donor names from database"""
        for i, name in enumerate(self.db):
            self.assertEqual(name, f'Test Donor {i+1}')


class TestUserInteraction(unittest.TestCase):
    """Unit tests for the user interaction functions"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.d1_name = 'Test Donor 1'
        self.d2_name = 'Test Donor 2'
        self.d3_name = 'Test Donor 3'
        self.d1_dons = [1000, 5000, 10000]
        self.d2_dons = [12000, 5000, 27000]
        self.d3_dons = [38734, 6273, 67520]

    def setUp(self):
        self.db = DonorDatabase(*[Donor(self.d1_name, self.d1_dons),
                                  Donor(self.d2_name, self.d2_dons),
                                  Donor(self.d3_name, self.d3_dons)])

    def tearDown(self):
        pass

    def test_get_usr_input(self):
        """Test the get_usr_input() fxn"""

        # Test all valid user input prompts
        with mock.patch('builtins.input') as mock_input:
            for prompt in PROMPT_OPTS:
                mock_input.return_value = prompt
                self.assertEqual(mr.get_usr_input(), prompt)

        # Test invalid input type
        se = ['two', 1]
        with mock.patch('builtins.input', side_effect=se) as mock_input:
            captured_print = redirect_stdout()
            mr.get_usr_input()
            reset_stdout()

            self.assertEqual(captured_print.getvalue(), (f'\nPlease try again. '
                                                         f'Valid options are: '
                                                         f'{PROMPT_OPTS}\n'))

        # Test valid input type, but not a valid option
        se = [-5, 1]
        with mock.patch('builtins.input', side_effect=se) as mock_input:
            captured_print = redirect_stdout()
            mr.get_usr_input()
            reset_stdout()

            self.assertEqual(captured_print.getvalue(), (f'\nPlease select a '
                                                         f'number between '
                                                         f'{PROMPT_OPTS[0]}'
                                                         f' and '
                                                         f'{PROMPT_OPTS[-1]}\n'))

    def test_prompt_for_donor(self):
        """Test the prompt_for_donor() fxn"""

        # Test when user enters a name
        with mock.patch('builtins.input') as mock_input:
            mock_input.return_value = 'mr. test donor'
            result = mr.prompt_for_donor('', self.db)

            self.assertEqual(result, 'Mr. Test Donor')

        # Test when user enters "quit"
        with mock.patch('builtins.input') as mock_input:
            mock_input.return_value = 'quit'
            captured_print = redirect_stdout()
            result = mr.prompt_for_donor('', self.db)
            reset_stdout()

            self.assertTrue(result is None)
            self.assertEqual(captured_print.getvalue(), '')

        # Test when user enters "list"
        se = ['list', 'quit']
        with mock.patch('builtins.input', side_effect=se) as mock_input:
            captured_print = redirect_stdout()
            result = mr.prompt_for_donor('', self.db)
            reset_stdout()

            self.assertTrue(result is None)
            self.assertEqual(captured_print.getvalue(), (f'\n{self.d1_name}\n'
                                                         f'{self.d2_name}\n'
                                                         f'{self.d3_name}\n'))

    def test_prompt_for_donation(self):
        """Test the prompt_for_donation() fxn"""

        # Test when user enters donation attempts
        se = ['foufty', '50']
        with mock.patch('builtins.input', side_effect=se):
            captured_print = redirect_stdout()
            result = mr.prompt_for_donation('')
            reset_stdout()

            self.assertEqual(result, 50.0, msg=result)
            self.assertEqual(captured_print.getvalue(),
                             '\nDonation amount must be a number\n')

        # Test when user enters 'quit'
        with mock.patch('builtins.input') as mock_input:
            mock_input.return_value = 'quit'
            captured_print = redirect_stdout()
            result = mr.prompt_for_donation('')
            reset_stdout()

            self.assertTrue(result is None, msg=result)
            self.assertEqual(captured_print.getvalue(), '')

    def test_send_thank_you(self):
        """Test send_thank_you() fxn"""

        # Test output thank you string
        se = ['Bert', '1000']
        with mock.patch('builtins.input', side_effect=se):
            captured_print = redirect_stdout()
            mr.send_thank_you(self.db)
            reset_stdout()

            self.assertEqual(captured_print.getvalue(),
                             self.db.thank_you_fmt.format('Bert', 1000) + '\n')

    def test_quit_mailroom(self):
        """Test quit_mailroom() fxn"""
        captured_print = redirect_stdout()
        mr.quit_mailroom(self.db)
        reset_stdout()

        self.assertEqual(captured_print.getvalue(), 'Quitting mailroom...\n')


if __name__ == '__main__':
    unittest.main()
