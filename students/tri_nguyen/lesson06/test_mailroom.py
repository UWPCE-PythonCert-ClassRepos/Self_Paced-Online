#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  16-Mar-2018
# ------------------------------------------- #

import unittest
import mailroom

class TestMailroom(unittest.TestCase):

    def test_display_menu(self):
        ''' test display_menu function of mailroom.py '''

        known_menu = ''' Select one of the actions below:

    1. Send a Thank You
    2. Create a Report
    3. Send letters to everyone
    4. Quit

    '''

        expected_result = mailroom.display_menu()
        self.assertEqual(expected_result, known_menu)
        # are assertIsNotNone and assertIsInstance necessary??
        self.assertIsNotNone(expected_result)
        self.assertIsInstance(expected_result, str)


    def test_convert_to_float(self):
        ''' test convert_to_float function of mailroom.py '''

        self.assertEqual(mailroom.convert_to_float('100.00'), 100.0)
        self.assertEqual(mailroom.convert_to_float('12.234'), 12.234)
        self.assertEqual(mailroom.convert_to_float('145.12'), 145.12)
        self.assertEqual(mailroom.convert_to_float('14.123456'), 14.123456)


    def test_generate_email_template(self):
        ''' test generate_email_template of mailroom.py '''

        known_temp = '''
                Dear {0},

                Thank you for giving us ${1:,.2f}. Your money will be put to good use.
                Please come back and donate more.

                Best Regards,

                John Doe
            '''

        expected_result = mailroom.generate_email_template()
        self.assertEqual(expected_result, known_temp)
        # are assertIsNotNone and assertIsInstance necessary??
        self.assertIsNotNone(expected_result)
        self.assertIsInstance(expected_result, str)


    def test_format_filename(self):
        ''' test format_filename function of mailroom.py '''

        self.assertEqual(mailroom.format_filename('tri nguyen'), 'tri_nguyen.txt')
        self.assertEqual(mailroom.format_filename('william gates, iii'), 'william_gates_iii.txt')
        self.assertEqual(mailroom.format_filename('one'), 'one.txt')

        with self.assertRaises(TypeError):
            mailroom.format_filename(82)


    def test_print_header(self):
        ''' test print_header function of mailroom.py '''

        known_header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
        known_template = '{0:<26}|{1:^13}|{2:^11}|{3:^14}'
        formatted_columns = known_template.format(*known_header)
        border = '{}'.format('-' * len(formatted_columns))
        
        self.assertEqual(mailroom.print_header()[0], formatted_columns)
        self.assertEqual(mailroom.print_header()[1], border)


    def test_generate_donor_list(self):
        ''' test generate_donor_list function of mailroom.py '''

        known_dict = {
            'William Gates, III': {'total': 653784.49, 'num_gifts': 2, 'avg': 326892.24},
            'Mark Zuckerberg': {'total': 16396.10, 'num_gifts': 3, 'avg': 5465.37},
            'Jeff Bezos': {'total': 877.33, 'num_gifts': 1, 'avg': 877.33},
            'Paul Allen':{'total': 708.42, 'num_gifts': 3, 'avg': 236.14},
            'Tri Nguyen': {'total': 100.00, 'num_gifts': 1, 'avg': 100.00}}

        known_list = [(name, known_dict[name]['total'], known_dict[name]['num_gifts'], known_dict[name]['avg']) for name in known_dict]

        self.assertEqual(mailroom.generate_donor_list(), known_list)

if __name__ == '__main__':
    unittest.main()