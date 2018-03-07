#!/usr/bin/env python3
import unittest
from collections import defaultdict
from mailroom4 import donors, get_all_donor_names, list_all_donor_names, group_donations


# Test Functions:

class TestMailRoom(unittest.TestCase):
    def test_get_all_donor_names(self):
        self.assertEqual(get_all_donor_names(), list(donors))


    def test_list_all_donor_names(self):
        self.assertEqual(list_all_donor_names(),'Ben Williams\nBill Gates\nGuy James\nHarry Potter\nJeff Bezo\nMike Dell\n')


    def test_group_donations(self):
        self.assertEqual(group_donations(), [['Bill Gates', 188655.55, 4],
             ['Harry Potter', 100016.35999999999, 3],
             ['Ben Williams', 30617.34, 2],
             ['Mike Dell', 26572.76, 2],
             ['Jeff Bezo', 4564.23, 1],
             ['Guy James', 127.34, 2]])
