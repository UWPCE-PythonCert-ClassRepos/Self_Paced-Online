#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import mailroom4 as mr
import unittest
import os


class MailroomTest(unittest.TestCase):

    def test_initial_donor_names(self):
        # test list name
        expected = sorted(["Amy Walker",
                           "July Jensen",
                           "Paul Allen",
                           "Peter Thomson",
                           "Jenny Palmer"])
        actual = sorted([d['name'] for d in mr.initialize_db()])

        self.assertListEqual(expected, actual)

    def test_donate_amount(self):
        donor_1 = {'name': 'Amy Walker', 'donation amount': [18900.90, 4500]}
        donor_2 = {'name': 'Jenny Palmer', 'donation amount': [66.89]}
        expected_1 = {'name': 'Amy Walker', 'donation amount': [18900.90, 4500, 2]}
        expected_2 = {'name': 'Jenny Palmer', 'donation amount': [66.89, 42.43]}
        actual_1 = mr.donate_amount(donor_1, 2)
        actual_2 = mr.donate_amount(donor_2, 42.43)

        self.assertDictEqual(expected_1, actual_1)
        self.assertDictEqual(expected_2, actual_2)
        self.assertIn(2, actual_1['donation amount'])
        self.assertIn(42.43, actual_2['donation amount'])

    def test_donate_sum(self):
        donor_1 = {'name': 'Amy Walker', 'donation amount': [18900.90, 4500, 2]}
        donor_2 = {'name': 'Jenny Palmer', 'donation amount': [66.89, 42.43]}
        expected_1 = 23402.9
        expected_2 = 109.32
        actual_1 = mr.donate_sum(donor_1)
        actual_2 = mr.donate_sum(donor_2)

        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    def test_create_donor(self):
        expected_1 = {'name': 'John Doe', 'donation amount': []}
        expected_2 = {'name': 'Mary Doe', 'donation amount': []}
        actual_1 = mr.create_donor('John Doe')
        actual_2 = mr.create_donor('Mary Doe')

        self.assertDictEqual(expected_1, actual_1)
        self.assertDictEqual(expected_2, actual_2)

    def test_report_string(self):
        expected = """Donor Name                 | Total Given | Num Gifts | Average Gift
--------------------------------------------------------------------
Amy Walker                  $   23400.90            2 $     11700.45
Peter Thomson               $   16500.87            3 $      5500.29
July Jensen                 $    5500.00            2 $      2750.00
Paul Allen                  $     320.57            1 $       320.57
Jenny Palmer                $      66.89            1 $        66.89
"""

        d = mr.initialize_db()
        actual = mr.report_string(d)

        self.assertEqual(expected, actual)

    def test_letter(self):
        donor_1 = {'name': 'Amy Walker', 'donation amount': [18900.90, 4500, 2]}
        donor_2 = {'name': 'Jenny Palmer', 'donation amount': [66.89, 42.43]}
        expected_1 = 'Dear Amy Walker, we want to thank you for your total donation amount of $23402.9. Have a nice day!'
        expected_2 = 'Dear Jenny Palmer, we want to thank you for your total donation amount of $109.32. Have a nice day!'
        actual_1 = mr.letter(donor_1)
        actual_2 = mr.letter(donor_2)

        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    def test_send_to_everyone(self):
        expected_number_of_files = 5
        mr.send_to_everyone()
        actual_number_of_files = len(os.listdir('letters'))

        self.assertEqual(expected_number_of_files, actual_number_of_files)


if __name__ == '__main__':
    unittest.main()
