import unittest
import donors as d
import os

new_group = d.Group()
new_group.add('Joe', 3)
new_group.add('Joe', 3)
new_group.add('Joe', 3)
new_group.add('Jack', 4)
new_group.add('Jack', 5)


class TestMailbox(unittest.TestCase):
    def test_Group_get(self):
        self.assertEqual(new_group.donors, {'Joe': [3, 3, 3],
                                            'Jack': [4, 5], 'Shane': [5]})

    def test_Group_search1(self):
        """Returns None when name does not exist"""
        self.assertEqual(new_group.search('Bob'), None)

    def test_Group_search2(self):
        """Returns 'name' when name does exist"""
        self.assertEqual(new_group.search('Jack'), 'Jack')

    def test_Group_Add(self):
        """Test that the new donors are being appended to the donor list."""
        new_group.add('Shane', 5)
        self.assertEqual(new_group.donors, {'Joe': [3, 3, 3],
                                            'Jack': [4, 5], 'Shane': [5]})

    def test_thankyou(self):
        test_text = 'Thank you so much for the generous gift of $5.00, Shane!'
        self.assertEqual(d.Individual.thank_you('Shane', 5), test_text)

    def test_summary(self):
        """Add a donor to the list and test that the donor summary
        is correct"""
        donor_summary = new_group.summary()
        self.assertEqual(donor_summary, {'Joe': [9, 3, 3],
                                         'Jack': [9, 2, 4.5],
                                         'Shane': [5, 1, 5]})

    def test_column_name_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_name_width(donors_f), 11)

    def test_column_name_width_1(self):
        donors_f = {'Joeeeeeeeeee': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_name_width(donors_f), 12)

    def test_column_total_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_total_width(donors_f), 12)

    def test_column_total_width_2(self):
        donors_f = {'Joe': [1555555555555, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_total_width(donors_f), 16)

    def test_column_average_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_average_width(donors_f), 12)

    def test_column_average_width_1(self):
        donors_f = {'Joe': [9, 3, 3555555555222], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_average_width(donors_f), 16)

    def test_column_number_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_number_width(donors_f), 12)

    def test_column_number_width_1(self):
        donors_f = {'Joe': [9, 33333333333333, 35555], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.column_number_width(donors_f), 17)

    def test_sort_list(self):
        donors_f = {'Joe': [15, 3, 35], 'Jack': [9, 2, 4.5]}
        self.assertEqual(new_group.sort_list(donors_f), ['Joe', 'Jack'])

    def test_sort_list_2(self):
        donors_f = {'Joe': [15, 3, 35], 'Jack': [9, 2, 4.5],
                    'Fred': [2000, 2, 60]}
        self.assertEqual(new_group.sort_list(donors_f),
                         ['Fred', 'Joe', 'Jack'])

    def test_report(self):
        assert "Joe        $" in new_group.report
        assert "9.00     3         " in new_group.report
        assert '$        3.00' in new_group.report

    def test_letters_for_all(self):
        try:
            new_group.letters()
            with open('Jack.txt', 'rU') as f:
                text = f.read()
        finally:
            os.remove('Jack.txt')

        expected_text = 'Dear Jack, thank you so much for your last ' \
                        'contribution of $5.00! You have contributed ' \
                        'a total of $9.00, and we appreciate your ' \
                        'support!'
        self.assertEqual(expected_text, text)


if __name__ == '__main__':
    unittest.main()
