#!/usr/bin/env python3
"""This is a test module that tests mailroom3.py"""

import unittest
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
        pass

    def test_get_donor_names(self):
        pass

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
