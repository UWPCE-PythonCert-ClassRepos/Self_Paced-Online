import unittest
from unittest import TestCase, main as unittest_main
import donors as d





class TestMailbox(unittest.TestCase):
    def test_Group_get(self):
        new_group = d.Group()
        self.assertEqual(new_group.donors, {'Joe': [3, 3, 3], 'Jack': [4, 5]})

    def test_Group_search1(self):
        """Returns None when name does not exist"""
        new_group = d.Group()
        self.assertEqual(new_group.search('Shane'), None)

    def test_Group_search2(self):
        """Returns 'name' when name does exist"""
        new_group = d.Group()
        self.assertEqual(new_group.search('Jack'), 'Jack')

    def test_Group_Add(self):
        """Test that the new donors are being appended to the donor list."""
        new_group = d.Group()
        new_group.add('Shane', 5)
        self.assertEqual(new_group.donors, {'Joe': [3, 3, 3], 'Jack': [4, 5], 'Shane': [5]})

    def test_thankyou(self):
        test_text = 'Thank you so much for the generous gift of $5.00, Shane!'
        self.assertEqual(d.Individual.thank_you('Shane', 5), test_text)

    def test_summary(self):
        """Add a donor to the list and test that the donor summary is correct"""
        new_group = d.Group()
        new_group.add('Shane', 5)
        donor_summary = new_group.summary()
        self.assertEqual(donor_summary, {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5], 'Shane': [5, 1, 5]})

    def test_column_name_width(self):
        new_group = d.Group()
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_name_width(donors_f), 11)

    def test_column_name_width_1(self):
        new_group = d.Group()
        donors_f = {'Joeeeeeeeeee': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_name_width(donors_f), 12)

    def test_column_total_width(self):
        new_group = d.Group()
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_total_width(donors_f), 12)

    def test_column_total_width_2(self):
        new_group = d.Group()
        donors_f = {'Joe': [1555555555555, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_total_width(donors_f), 16)

    def test_column_average_width(self):
        new_group = d.Group()
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_average_width(donors_f), 12)

    def test_column_average_width_1(self):
        new_group = d.Group()
        donors_f = {'Joe': [9, 3, 3555555555222], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_average_width(donors_f), 16)

    def test_column_number_width(self):
        new_group = d.Group()
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_number_width(donors_f), 12)

    def test_column_number_width_1(self):
        new_group = d.Group()
        donors_f = {'Joe': [9, 33333333333333, 35555], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_number_width(donors_f), 17)

    def test_sort_list(self):
        new_group = d.Group()
        donors_f = {'Joe': [15, 3, 35], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.sort_list(donors_f), ['Joe', 'Jack'])

    def test_sort_list_2(self):
        new_group = d.Group()
        donors_f = {'Joe': [15, 3, 35], 'Jack': [9, 2, 4.5],
                    'Fred': [2000, 2, 60]}
        self.assertEqual(new_group.sort_list(donors_f),
                         ['Fred', 'Joe', 'Jack'])

    def test_report(self):
        new_group = d.Group()
        donors_f = {'Joe': [9, 3, 3]}
        rows = new_group.report(donors_f)
        self.assertEqual(rows[3], 'Joe        $        '
                                              '9.00     3         '
                                              '$        3.00')

#    def test_letters_for_all(self):
#        m.donors = {'Jack': [4, 11]}

#        try:
#            m.letters_for_all()
#            with open('Jack.txt', 'rU') as f:
#                text = f.read()
#        finally:
#            os.remove('Jack.txt')

#        expected_text = 'Dear Jack, thank you so much for your last ' \
#                        'contribution of $11.00! You have contributed ' \
#                        'a total of $15.00, and we appreciate your ' \
#                        'support!'
#        self.assertEqual(expected_text, text)


if __name__ == '__main__':
    unittest.main()
