import mailroom_pt5 as m
import unittest
import os

donor_data = m.donor_data


class test_Donor(unittest.TestCase):

    def test_donations(self):
        test = m.Donor(donor_data['Jill'])
        self.assertEqual(test.donation, [50, 200, 100, 250])

    def test_total(self):
        test = m.Donor(donor_data['Jill'])
        self.assertEqual(test.total, 600)

    def test_ave(self):
        test = m.Donor(donor_data['Jill'])
        self.assertEqual(test.ave, 150)

    def test_num(self):
        test = m.Donor(donor_data['Jill'])
        self.assertEqual(test.num_donations, 4)

    def test_last(self):
        test = m.Donor(donor_data['Jill'])
        self.assertEqual(test.last, 250)


class test_Donor_oporations(unittest.TestCase):

    def test_donor_append(self):
        m.Donor_ops.donor_append('Jill', 99)
        self.assertEqual(donor_data['Jill'], [50, 200, 100, 250, 99])

    def test_thank_you_self(self):
        expected = ("\n---------------- Thank You ----------------\n\n"
                    "Dear Edwin Hubble,\n\n"
                    "You rock. Your fat contribution of $1,899.00\n"
                    "will go a long way to lining my pockets.\n\n"
                    "Sincerely,\n"
                    "Scrooge McDuck")
        actual = m.Donor_ops.thank_you('Edwin Hubble')
        self.assertEqual(actual, expected)

    def test_list_donors(self):
        expected = ("\n---------------- List of Donors ----------------\n\n"
                    "Galileo Galilei\n"
                    "Giovanni Cassini\n"
                    "Christiaan Huygens\n"
                    "Edmond Halley\n"
                    "Edwin Hubble\n"
                    "Jill\n")
        actual = m.Donor_ops.list_donors()
        self.assertEqual(actual, expected)

    def test_report(self):
        self.maxDiff = None
        expected = ("\n--------------- Report -------------\n\n"
                    "DONOR                         TOTAL          AVERAGE        NUMBER         \n"
                    "Galileo Galilei               8848           2,949.33       3              \n"
                    "Giovanni Cassini              209            209.00         1              \n"
                    "Christiaan Huygens            9174           4,587.00       2              \n"
                    "Edmond Halley                 1856           618.67         3              \n"
                    "Edwin Hubble                  1899           1,899.00       1              \n"
                    "Jill                          699            139.80         5              \n")
        actual = m.Donor_ops.report()
        self.assertEqual(actual, expected)

    def test_letters(self):
        assert os.path.isfile('Giovanni Cassini_2018-06-10.txt')
        assert os.path.isfile('Edmond Halley_2018-06-10.txt')
        assert os.path.isfile('Edwin Hubble_2018-06-10.txt')
        assert os.path.isfile('Galileo Galilei_2018-06-10.txt')
        assert os.path.isfile('Christiaan Huygens_2018-06-10.txt')
        assert os.path.isfile('Jill_2018-06-10.txt')


if __name__ == '__main__':
    unittest.main()
