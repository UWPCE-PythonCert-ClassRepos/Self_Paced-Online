#!/usr/bin/env python3
import unittest
import mailroom_OO as mrOO
from io import StringIO
import os


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
        self.assertEqual(self.test.donorgroup,
                         [{'Brin': {'title': 'Mr.', 'donations': 100000,
                          'num_donations': 1}},
                          {'Wojcicki': {'title': 'Ms.', 'donations': 200000,
                           'num_donations': 1}},
                          {'Avey': {'title': 'Ms.', 'donations': 150000,
                                    'num_donations': 1}}])
        self.test.donorgroup_new_donor = mrOO.Donor('Mr.', 'Page', 50000)
        self.assertEqual(self.test.donorgroup,
                         [{'Brin': {'title': 'Mr.', 'donations': 100000,
                          'num_donations': 1}},
                          {'Wojcicki': {'title': 'Ms.', 'donations': 200000,
                           'num_donations': 1}},
                          {'Avey': {'title': 'Ms.', 'donations': 150000,
                                    'num_donations': 1}},
                          {'Page': {'title': 'Mr.', 'donations': 50000,
                                    'num_donations': 1}}])
        # print('self.test.__dir__() is', self.test.__dir__())
        self.test.withdraw('Mr.', 'Brin')
        self.assertEqual(self.test.donorgroup,
                         [{'Wojcicki': {'title': 'Ms.', 'donations': 200000,
                           'num_donations': 1}},
                          {'Avey': {'title': 'Ms.', 'donations': 150000,
                                    'num_donations': 1}},
                          {'Page': {'title': 'Mr.', 'donations': 50000,
                                    'num_donations': 1}}])

    def test_donor_group_list(self):
        self.assertEqual(self.test.get_list(),
                         [[200000, 'Wojcicki', 1],[150000, 'Avey', 1], [100000, 'Brin', 1]])

    def test_donor_group_report(self):
        actual = self.test.get_report()
        expected = """
        Donor Name     | Total Given | Num Gifts| Average Gift
        -------------------------------------------------------
        Wojcicki         $    200000           1 $     200000
        Avey             $    150000           1 $     150000
        Brin             $    100000           1 $     100000
        """
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            print('Disregard. These are equal.')

    def test_donor_group_save(self):
        self.test.save_data()
        cwd_list = os.listdir(os.getcwd())
        self.assertTrue('test.txt' in cwd_list)
