# Test_Mailroom_pt4.py Exercise by tfbanks

# !/usr/bin/env python3

import unittest
import os
import sys
from io import StringIO

from Mailroom_pt4 import donor_names, thank_you_letter, selection, mass_mail,report


class mailroom_tests(unittest.TestCase):

    def test_selection(self):  # Tests to insure that the n options are in the selection function
        for n in [1, 2, 3, 4]:
            self.assertTrue(selection(n))

    def test_donors(self):  # Tests to insure that the donors listed are indeed on the list, and also tests one given name and donations are on the list
        self.assertEqual(['Tim Cooker', 'Elon Musket', 'Frank Petersmankempt', 'Megan Morgan', 'Marlene Wheeler'],
                         list(donor_names.keys()))
        self.assertTrue(donor_names['Tim Cooker'] == [1500.50, 25050.50, 15680.75])

    def test_thank_you_letter(self):  # insures that given a name and a donation, the letter to be written prints properly
        expected = ('''\n\nDear Fredy Meyers,\n
Thank you for your generous donation of $25,252.00, your generosity is greatly appreciated.
These funds will help continue our efforts to teach Python to the next generation.\n
Sincerely,\n\n
Joesef Edword Bringingham''')
        assert thank_you_letter('Fredy Meyers', 25252) == expected

    def test_mass_mail(self):  # tests to make sure tht with the mass email function, an example donor's file is correctly populated
        mass_mail()
        assert os.path.isfile('Tim Cooker.txt')
        assert os.path.isfile('Elon Musket.txt')
        assert os.path.isfile('Frank Petersmankempt.txt')
        assert os.path.isfile('Megan Morgan.txt')
        assert os.path.isfile('Marlene Wheeler.txt')
        
    def test_report(self):
        sys.stdout = StringIO()
        report()
        out = sys.stdout.getvalue()
        expected = '''
Donor Name            |  Total Given | Num Gifts |  Average Gift
------------------------------------------------------------------
Tim Cooker              $  42,231.75        3        $  14,077.25
Elon Musket             $  31,750.25        2        $  15,875.12
Megan Morgan            $  22,875.80        3        $   7,625.27
Marlene Wheeler         $   2,042.80        2        $   1,021.40
Frank Petersmankempt    $     550.60        1        $     550.60
'''
        assert out == expected
