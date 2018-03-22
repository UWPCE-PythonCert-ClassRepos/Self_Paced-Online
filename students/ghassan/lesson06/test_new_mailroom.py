#!/usr/bin/env python3

import unittest
from new_mailroom import main_menu, send_thankyou, donors


class TestMailroom(unittest.TestCase):
    def test_main_menu(self):
        ''' this tests if the function is actually
        returning the user's input '''
        users_choice = main_menu()
        self.assertEqual(users_choice, users_choice)

    def test_send_thankyou_new_donor(self):
        ''' tests whether a new donor was actually added
        to the donors list'''
        # I did a list comprehention here to get
        # a fresh copy of the dictionary keys as of
        # a reference or a pointer to the same dictionary
        old_donors = [donor for donor in donors.keys()]
        send_thankyou()
        self.assertGreater([
            new_donor for new_donor in donors.keys()],
            old_donors)

