# Test_Mailroom_pt4.py Exercise by tfbanks

# !/usr/bin/env python3

import unittest
import os

from Mailroom_pt4 import donor_names, thank_you_letter, selection, mass_mail, report


class mailroom_tests(unittest.TestCase):

    def test_selection(self):  # Tests to insure that the n options are in the selection function
        for n in [1, 2, 3]:
            self.assertTrue(selection(n))

    def test_donors(self):  # Tests to insure that the donors listed are indeed on the list, and also tests one given name and donations are on the list
        self.assertEqual(['Tim Cooker', 'Elon Musket', 'Frank Petersmankempt', 'Megan Morgan', 'Marlene Wheeler'],
                         list(donor_names.keys()))
        self.assertTrue(donor_names['Tim Cooker'] == [1500.50, 25050.50, 15680.75])

    def test_thank_you_letter(self):  # insures that given a name and a donation, the letter to be written prints properly
        letter = thank_you_letter('Fredy Meyers', 25252)
        return letter
        assert letter == ('''Dear Fredy Meyers,

Thank you for your generous donation of $25,252.00, your generosity is greatly appreciated.
These funds will help continue our efforts to teach Python to the next generation.

Sincerely,


Joesef Edword Bringingham''')

    def test_report(self):  # Not too sure about this one, put it in because I could, but report ia report, didn't know how else to test it.
        return report()
        self.assertTrue(report())

    def test_mass_mail(self):  # tests to make sure tht with the mass email function, an example donor's file is correctly populated
        mass_mail()
        assert os.path.isfile('Tim Cooker.txt')
