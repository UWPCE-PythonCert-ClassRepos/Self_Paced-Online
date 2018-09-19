import unittest
from unittest import TestCase, main as unittest_main
import mailroom_9 as m
import io
import os

donors = {'Joe Edgar Allen Poe the Third ': [1, 4, 200],
          'Jack': [4, 5], 'Jill': [4], 'Jake': [.30],
          'Jim': [1, 2, 1.04]}


class TestMailbox(unittest.TestCase):
    def test_thankyou_1(self):

        new_donor = m.Donor('Jack', 0)
        self.assertEqual(new_donor.thank_you(), None)

    def test_thankyou_2(self):
        new_donor = m.Donor('Jack', 0)
        with self.assertRaises(ValueError):
            new_donor.thank_you()

    def test_thankyou_3(self):
        new_donor = m.Donor('Jack', 0)
        self.assertEqual(new_donor.thank_you(), None)

    def test_thankyou_4(self):
        """test that new donors are being appended"""
        old_donors = m.CollectionDonors()
        new_donor = m.Donor('Shane', 5)
        new_donor.thank_you()
        self.assertEqual(old_donors.donors, {'Joe': [3, 3, 3], 'Jack': [4, 5], 'Shane':[5]} )

    def test_summary_donors_4(self):
        m.donors = {'Joe': [3, 3, 3], 'Jack': [4, 5]}
        self.assertEqual(m.summary_donors(), {'Joe': [9, 3, 3],
                                              'Jack': [9, 2, 4.5]})

    def test_column_name_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(m.column_name_width(donors_f), 11)

    def test_column_name_width_1(self):
        donors_f = {'Joeeeeeeeeee': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(m.column_name_width(donors_f), 12)

    def test_column_total_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(m.column_total_width(donors_f), 12)

    def test_column_total_width_2(self):
        donors_f = {'Joe': [1555555555555, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(m.column_total_width(donors_f), 16)

    def test_column_average_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(m.column_average_width(donors_f), 12)

    def test_column_average_width_1(self):
        donors_f = {'Joe': [9, 3, 3555555555222], 'Jack': [9, 2, 4.5]}
        self.assertEqual(m.column_average_width(donors_f), 16)

    def test_column_number_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(m.column_number_width(donors_f), 12)

    def test_column_number_width_1(self):
        donors_f = {'Joe': [9, 33333333333333, 35555], 'Jack': [9, 2, 4.5]}
        self.assertEqual(m.column_number_width(donors_f), 17)

    def test_sort_list(self):
        donors_f = {'Joe': [15, 3, 35], 'Jack': [9, 2, 4.5]}
        self.assertEqual(m.sort_list(donors_f), ['Joe', 'Jack'])

    def test_sort_list_2(self):
        donors_f = {'Joe': [15, 3, 35], 'Jack': [9, 2, 4.5],
                    'Fred': [2000, 2, 60]}
        self.assertEqual(m.sort_list(donors_f),
                         ['Fred', 'Joe', 'Jack'])

    def test_report(self):
        m.donors = {'Joe': [3, 3, 3]}
        self.assertEqual(m.report(), ['Joe        $        '
                                              '9.00     3         '
                                              '$        3.00'])

    def test_letters_for_all(self):
        m.donors = {'Jack': [4, 11]}

        try:
            m.letters_for_all()
            with open('Jack.txt', 'rU') as f:
                text = f.read()
        finally:
            os.remove('Jack.txt')

        expected_text = 'Dear Jack, thank you so much for your last ' \
                        'contribution of $11.00! You have contributed ' \
                        'a total of $15.00, and we appreciate your ' \
                        'support!'
        self.assertEqual(expected_text, text)


if __name__ == '__main__':
    unittest.main()
