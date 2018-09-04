import unittest
import mailroom4

donors = {'Joe Edgar Allen Poe the Third ': [1, 4, 200],
          'Jack': [4, 5], 'Jill': [4], 'Jake': [.30],
          'Jim': [1, 2, 1.04]}


class TestMailbox(unittest.TestCase):
    def test_thankyou_1(self):
        donors = {'Joe': [3, 3, 3], 'Jack': [4, 5]}
        self.assertEqual(mailroom4.thank_you(donors, 'Jack', 0), None)


    def test_thankyou_2(self):
        donors = {'Joe': [3, 3, 3], 'Jack': [4, 5]}
        self.assertEqual(mailroom4.thank_you(donors, 'Jack', 'p'), ValueError)

    def test_thankyou_3(self):
        donors = {'Joe': [3, 3, 3], 'Jack': [4, 5]}
        self.assertEqual(mailroom4.thank_you(donors, 'Jack', 12), {'Joe':[3,3,3], 'Jack':[4, 5, 12]})

    def test_summary_donors_4(self):
        donors = {'Joe': [3, 3, 3], 'Jack': [4, 5]}
        self.assertEqual(mailroom4.summary_donors(donors), {'Joe': [9, 3, 3],'Jack': [9, 2, 4.5]})

    def test_column_name_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(mailroom4.column_name_width(donors_f), 11)

    def test_column_name_width_1(self):
        donors_f = {'Joeeeeeeeeee': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(mailroom4.column_name_width(donors_f), 12)


    def test_column_total_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(mailroom4.column_total_width(donors_f), 12)


    def test_column_total_width_2(self):
        donors_f = {'Joe': [1555555555555, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(mailroom4.column_total_width(donors_f), 16)

    def test_column_average_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(mailroom4.column_average_width(donors_f), 12)

    def test_column_average_width_1(self):
        donors_f = {'Joe': [9, 3, 3555555555222], 'Jack': [9, 2, 4.5]}
        self.assertEqual(mailroom4.column_average_width(donors_f), 16)

    def test_column_number_width(self):
        donors_f = {'Joe': [9, 3, 3], 'Jack': [9, 2, 4.5]}
        self.assertEqual(mailroom4.column_number_width(donors_f), 12)

    def test_column_number_width_1(self):
        donors_f = {'Joe': [9, 33333333333333, 35555], 'Jack': [9, 2, 4.5]}
        self.assertEqual(mailroom4.column_number_width(donors_f), 17)

    def test_sort_list(self):
        donors_f = {'Joe': [15, 3, 35], 'Jack': [9, 2, 4.5]}
        self.assertEqual (mailroom4.sort_list(donors_f), ['Joe','Jack'])

    def test_sort_list_2(self):
        donors_f = {'Joe': [15, 3, 35], 'Jack': [9, 2, 4.5], 'Fred':[2000,2, 60]}
        self.assertEqual (mailroom4.sort_list(donors_f), ['Fred','Joe','Jack'])


if __name__ == '__main__':
    unittest.main()