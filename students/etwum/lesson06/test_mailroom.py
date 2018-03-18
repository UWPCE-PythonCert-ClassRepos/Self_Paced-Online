from unittest import TestCase
from mailroom_part4 import dict_donors, get_donor_list, options, user_selection, create_donor


class TestMailRoom(TestCase):
    def test_get_donor_list(self):
        # testing the get donor list function from the mail room part 4 program
        self.assertEqual(get_donor_list(), dict_donors)

    def test_options(self):
        # testing the options function from the mail room part 4 program
        self.assertEqual(options(), user_selection)

    def test_create_donor(self):
        self.assertEqual(create_donor(), 5)
