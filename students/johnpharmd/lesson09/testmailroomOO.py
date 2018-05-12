#!/usr/bin/env python3
import unittest
import mailroom_OO


class MailRoomOOTest(unittest.TestCase):
    def setUp(self):
        self.test = mailroom_OO.Donor('Mr.', 'Brin', 100000)

    def test_donor(self):
        self.assertEqual(self.test.donor, {'Brin': {'title': 'Mr.',
                         'donations': 100000, 'num_donations': 1}})
