#!/usr/bin/env python3

import unittest
import mailroom_4 as mailroom
import os


class MailroomTest(unittest.TestCase):

    def test_donor_amount(self):
        self.assertEqual(mailroom.donors['Donor A'], [3580, 34124.31, 7654])

    def test_list_donors(self):
        del mailroom.donors['x']
        self.assertEqual(list(mailroom.donor_list()), ['Donor A', 'Donor B',
                         'Donor C', 'Donor D', 'Donor E', 'Donor F'])

    def test_report(self):
        self.assertTrue(mailroom.report())

    def test_letter(self):
        self.assertTrue(mailroom.letter('Donor A', 34124.31))

    def test_add_donation(self):
        mailroom.add_donation('x', 1, mailroom.donors)
        self.assertEqual(mailroom.donors['x'][0], 1)

    def test_donation_summary(self):
        self.assertEqual(mailroom.donor_stat()[0][0], 'Donor E')
        self.assertEqual(mailroom.donor_stat()[0][1], 569796.1)
        self.assertEqual(mailroom.donor_stat()[0][2], 4)
        self.assertEqual(mailroom.donor_stat()[0][3], 142449.025)

    def test_file(self):
        mailroom.write()
        self.assertTrue('Donor E.txt', os.path.exists('Donor E.txt'))


if __name__ == '__main__':
    unittest.main()
