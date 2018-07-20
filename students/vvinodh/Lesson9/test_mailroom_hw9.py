import mailroom_hw9 as m
import unittest
import os

donor_data = m.donor_data


class test_Donor(unittest.TestCase):

    def test_donations(self):
        test = m.Donor(donor_data['Jeff Bezos'])
        self.assertEqual(test.donation, [877.33, 1, 877.33])

    def test_total(self):
        test = m.Donor(donor_data['Jeff Bezos'])
        self.assertEqual(test.total, 1755.66)

    def test_ave(self):
        test = m.Donor(donor_data['Jeff Bezos'])
        self.assertEqual(test.ave, 585.22)

    def test_num(self):
        test = m.Donor(donor_data['Jeff Bezos'])
        self.assertEqual(test.num_donations, 3)

    def test_last(self):
        test = m.Donor(donor_data['Jeff Bezos'])
        self.assertEqual(test.last, 877.33)


class test_Donor_oporations(unittest.TestCase):


    def test_thank_you_self(self):
        expected = ("\n---------------- Thank You ----------------\n\n"
                    "Dear Jeff Bezos,\n\n"
                    "Thank you for your contribution of $877.33.\n"
                    "It will be put to very good use.\n\n"
                    "Sincerely,\n"
                    "Vinodh")
        actual = m.Donor_ops.thank_you('Jeff Bezos')
        self.assertEqual(actual, expected)

    def test_list_donors(self):
        expected = ("\n---------------- List of Donors ----------------\n\n"
                    "William Gates, III\n"
                    "Mark Zuckerberg\n"
                    "Jeff Bezos\n"
                    "Paul Allen\n")
        actual = m.Donor_ops.list_donors()
        self.assertEqual(actual, expected)

    def test_report(self):
        self.maxDiff = None
        expected = ("\n--------------- Report -------------\n\n"
                    "DONOR                         TOTAL          AVERAGE        NUMBER         \n"
                    "William Gates, III            391894.24      130,631.41     3              \n"
                    "Mark Zuckerberg               21468.37       7,156.12       3              \n"
                    "Jeff Bezos                    1755.66        585.22         3              \n"
                    "Paul Allen                    947.56         315.85         3              \n")
        actual = m.Donor_ops.report()
        self.assertEqual(actual, expected)

    def test_letters(self):
        assert os.path.isfile('William Gates, III_2018-07-17.txt')
        assert os.path.isfile('Mark Zuckerberg_2018-07-17.txt')
        assert os.path.isfile('Jeff Bezos_2018-07-17.txt')
        assert os.path.isfile('Paul Allen_2018-07-17.txt')

if __name__ == '__main__':
    unittest.main()
