#!/usr/bin/env python3
"""This is a test module that tests mailroom3.py"""

import unittest
from unittest import mock
import mailroom3 as mr


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

        with mock.patch('builtins.input') as fake_input:
            # Test all valid user input prompts
            for prompt in mr.PROMPT_OPTS:
                fake_input.return_value = prompt
                self.assertTrue(mr.get_usr_input() == prompt)

            # Cannot run this test as it get_usr_input() will be in an
            # infinite loop if fake_input is not valid...
            # Test invalid input type
            # fake_input.return_value = 'two'
            # capturedPrint = io.StringIO()
            # sys.stdout = capturedPrint
            # mr.get_usr_input()
            # sys.stdout = sys.__stdout__
            # print_results = capturedPrint.getvalue()
            # self.assertTrue(print_results == (f'\nPlease try again. Valid '
            #                                   f'options are: {mr.PROMPT_OPTS}\n'),
            #                 print_results)

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
        pass

    def test_prompt_for_donation(self):
        pass

    def test_add_donation(self):
        pass

    def test_send_thank_you(self):
        pass

    def test_create_report(self):
        pass

    def test_quit_mailroom(self):
        pass

    def test_send_letters(self):
        pass


if __name__ == '__main__':
    unittest.main()
