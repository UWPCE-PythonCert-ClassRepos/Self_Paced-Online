#!/usr/bin/env python3

# Lesson_9 Activity 1 Test Mailroom Part 5

from Mailroom_Pt5 import *
import os.path
import unittest

new_donor1 = Donor('James', 'Franconstein', [3009375072340])
new_donor2 = Donor('Billybob', 'Thorntons', [1, 2, 3, 4, 5])
new_donor3 = Donor('Mama', 'Mia', [666, 222, 333])
new_donor4 = Donor('Your', 'Mother', [10138327492, 2])

dc = DonorChart([new_donor1, new_donor2, new_donor3])


class TestMailroom(unittest.TestCase):

    def test_donor_init(self):
        self.assertTrue(new_donor1.full_name == 'James Franconstein')
        self.assertTrue(new_donor1.first == 'James')
        self.assertTrue(new_donor1.last == 'Franconstein')
        self.assertTrue(new_donor1.donations == [3009375072340])
        self.assertTrue(new_donor2.full_name == 'Billybob Thorntons')
        self.assertTrue(new_donor2.donations == [1, 2, 3, 4, 5])

    def test_donor_chart(self):
        self.assertTrue(dc.donor_list == ['James Franconstein',
                                          'Billybob Thorntons', 'Mama Mia'])

        dc.add_donor(new_donor4)
        self.assertTrue(dc.donor_list == ['James Franconstein',
                                          'Billybob Thorntons',
                                          'Mama Mia', 'Your Mother'])
        self.assertTrue(dc.total_donations == 11)
        self.assertTrue(dc.total_raised == 3019513401070)

        test_list = dc.sort_by_first()
        name_list = []
        for item in test_list:
            name_list.append(item.full_name)
        self.assertTrue(name_list == ['Billybob Thorntons',
                                      'James Franconstein',
                                      'Mama Mia', 'Your Mother'])
        test_list2 = dc.sort_by_last()

        name_list = []
        for item in test_list2:
            name_list.append(item.full_name)
        assert name_list == (['James Franconstein', 'Mama Mia',
                              'Your Mother', 'Billybob Thorntons'])

        money_list = dc.sort_by_total()
        name_list = []
        for item in money_list:
            name_list.append(item.full_name)
        assert name_list == (['James Franconstein', 'Your Mother',
                              'Mama Mia', 'Billybob Thorntons'])

    def test_create_report(self):
        report_test = create_report(dc)
        for item in dc.donors:
            self.assertTrue(item.first in report_test)
            self.assertTrue(f"{item.total_donation:,.2f}" in report_test)

    def test_send_letters(self):
        test_dump = "C:/Users/chris.kenyon/Documents/"
        "Kenyon/UWPython/Testing_File_dump"
        send_letters(test_dump, dc)
        for item in dc.donors:
            assert os.path.isfile((os.path.join(test_dump,
                                                item.full_name + ".txt")))
