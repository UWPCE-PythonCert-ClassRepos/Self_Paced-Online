#!/usr/bin/env python3
import unittest
import mailroom_OO as mrOO


class DonorTest(unittest.TestCase):
    def setUp(self):
        self.test = mrOO.Donor('Mr.', 'Brin', 100000)

    def test_donor(self):
        self.assertEqual(self.test.donor, {'Brin': {'title': 'Mr.',
                         'donations': 100000, 'num_donations': 1}})
        self.test.title = 'Dr.'
        self.assertEqual(self.test.donor, {'Brin': {'title':
                         'Dr.', 'donations': 100000, 'num_donations': 1}})
        self.test.donation = 150000
        self.assertEqual(self.test.donor, {'Brin': {'title':
                         'Dr.', 'donations': 250000, 'num_donations': 2}})


class DonorGroupTest(unittest.TestCase):
    def setUp(self):
        self.test = mrOO.DonorGroup(mrOO.Donor('Mr.', 'Brin', 100000),
                                    mrOO.Donor('Ms.', 'Wojcicki', 200000),
                                    mrOO.Donor('Ms.', 'Avey', 150000))

    def test_donor_group(self):
        self.assertEqual(self.test.donor_group,
                         [{'Brin': {'title': 'Mr.', 'donations': 100000,
                          'num_donations': 1}},
                          {'Wojcicki': {'title': 'Ms.', 'donations': 200000,
                           'num_donations': 1}},
                          {'Avey': {'title': 'Ms.', 'donations': 150000,
                                    'num_donations': 1}}])
        self.test.donor_group_add = mrOO.Donor('Mr.', 'Page', 50000)
        self.assertEqual(self.test.donor_group,
                         [{'Brin': {'title': 'Mr.', 'donations': 100000,
                          'num_donations': 1}},
                          {'Wojcicki': {'title': 'Ms.', 'donations': 200000,
                           'num_donations': 1}},
                          {'Avey': {'title': 'Ms.', 'donations': 150000,
                                    'num_donations': 1}},
                          {'Page': {'title': 'Mr.', 'donations': 50000,
                                    'num_donations': 1}}])
        self.test.donor_group_remove = 'Brin'
        self.assertEqual(self.test.donor_group,
                         [{'Wojcicki': {'title': 'Ms.', 'donations': 200000,
                           'num_donations': 1}},
                          {'Avey': {'title': 'Ms.', 'donations': 150000,
                                    'num_donations': 1}},
                          {'Page': {'title': 'Ms.', 'donations': 150000,
                                    'num_donations': 1}}])
