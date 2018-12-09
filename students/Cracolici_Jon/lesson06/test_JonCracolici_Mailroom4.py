#
# Jon Cracolici
# Lesson 06
# Mailroom 4 Testing Suite
#
# I refactored my code after speaking with a programmer friend who told
# me that it is important to fully isolate the user input from the logic to
# make unit testing easier - otherwise I have to mock the inputs. I might not get
# to every possible test but I am trying. Honestly, given what I intend to do with
# python in my workplace I feel that this lesson is the most valuable.
#

import JonCracolici_Mailroom4 as mr
import pytest
import unittest
import os

# create a local instance of the problem database to pass to functions
dB = mr.initialize_database()


class TestMailroom(unittest.TestCase):

    db = mr.initialize_database()
    print(db)

    def test_q_check(self):
        """This tests the quit-checking function"""
        self.assertEqual(mr.q_check('quit'), False)
        self.assertEqual(mr.q_check('q'), False)
        self.assertEqual(mr.q_check('Some Name'), 'Some Name')
        self.assertEqual(mr.q_check(1000.0), False)

    def test_ud_name_handle(self):
        """This tests the function's ability to correctly identify all current names,
        as well as some new names."""
        # This builds a set of names already in the list for testing.

        db = mr.initialize_database()

        test_in_name = 'Jeff Bezos'

        self.assertEqual(mr.ud_name_handle(test_in_name, db, io='in'), test_in_name)
        self.assertEqual(mr.ud_name_handle(test_in_name, db, io='out'), False)

        # This builds a set of names not in the list for testing.
        test_out_name = 'George Costanza'

        self.assertEqual(mr.ud_name_handle(test_out_name, db, io='in'), False)
        self.assertEqual(mr.ud_name_handle(test_out_name, db, io='out'), test_out_name)

    def test_ud_don_handle(self):
        """This function tests that donation input can be converted to float type."""
        self.assertEqual(mr.ud_don_handle('1000.0'), 1000.00)
        self.assertEqual(mr.ud_don_handle('something'), False)

    def test_print_letters(self):
        db = mr.initialize_database()
        for item in db.values():
            mr.print_letters(item)
            file_name = item['f_name']+'.txt'
            self.assertTrue(file_name, os.path.exists(file_name))

    def test_updating(self):
        db = mr.initialize_database()
        new_donor_dict = {'donor_name_key': 'jeff_bezos', 'donor': 'Jeff Bezos', 'donation': 1000.00}
        db2 = mr.update_donor(new_donor_dict, db)
        william_gates_iii = {'f_name': 'William_Gates_III', 'donor': 'William Gates, III', 'total_donated': 653784.49,
                         'num_donations': 2, 'avg_donated': 326892.24, 'last_donation': 30000.00}
        mark_zuckerberg = {'f_name': 'Mark_Zuckerberg', 'donor': 'Mark Zuckerberg', 'total_donated': 16396.10,
                       'num_donations': 3, 'avg_donated': 5465.37, 'last_donation': 5000.25}
        jeff_bezos = {'f_name': 'Jeff_Bezos', 'donor': 'Jeff Bezos', 'total_donated': 1877.33, 'num_donations': 2,
                  'avg_donated': 877.33, 'last_donation': 938.67}
        paul_allen = {'f_name': 'Paul_Allen', 'donor': 'Paul Allen', 'total_donated': 708.42, 'num_donations': 3,
                  'avg_donated': 236.14, 'last_donation': 100.95}

        db3 = {'william_gates_iii': william_gates_iii, 'mark_zuckerberg': mark_zuckerberg, 'jeff_bezos': jeff_bezos,
          'paul_allen': paul_allen}
        self.assertTrue(db2, db3)

    def test_new(self):
        db = mr.initialize_database()
        new_donor_dict = {'donor_name_key': 'val_halen', 'donor': 'Van Halen', 'donation': 1000.00}
        db2 = mr.new_donor(new_donor_dict, db)
        william_gates_iii = {'f_name': 'William_Gates_III', 'donor': 'William Gates, III', 'total_donated': 653784.49,
                         'num_donations': 2, 'avg_donated': 326892.24, 'last_donation': 30000.00}
        mark_zuckerberg = {'f_name': 'Mark_Zuckerberg', 'donor': 'Mark Zuckerberg', 'total_donated': 16396.10,
                       'num_donations': 3, 'avg_donated': 5465.37, 'last_donation': 5000.25}
        jeff_bezos = {'f_name': 'Jeff_Bezos', 'donor': 'Jeff Bezos', 'total_donated': 877.33, 'num_donations': 1,
                  'avg_donated': 877.33, 'last_donation': 877.33}
        paul_allen = {'f_name': 'Paul_Allen', 'donor': 'Paul Allen', 'total_donated': 708.42, 'num_donations': 3,
                  'avg_donated': 236.14, 'last_donation': 100.95}
        van_halen = {'f_name': 'Van_Halen', 'donor': 'Van Halen', 'total_donated': 1000.00, 'num_donations': 1,
                  'avg_donated': 1000.00, 'last_donation': 1000.00}

        db3 = {'william_gates_iii': william_gates_iii, 'mark_zuckerberg': mark_zuckerberg, 'jeff_bezos': jeff_bezos,
          'paul_allen': paul_allen, 'van_halen': van_halen}
        self.assertTrue(db2, db3)

    def test_note_gen(self):
        william_gates_iii = {'f_name': 'William_Gates_III', 'donor': 'William Gates, III', 'total_donated': 653784.49,
                         'num_donations': 2, 'avg_donated': 326892.24, 'last_donation': 30000.00}
        a = mr.note_gen(william_gates_iii, dest='s')
        b = mr.note_gen(william_gates_iii, dest='f')
        message = "Dear William Gates, III, \nThank you for your generous donation of $30000.00. " \
                  "Please rest assured that we will use at least \n95% of your contribution to feed the homeless" \
                  " to wolves. We could not do this work without you. \nSincerely, \nThe Billionaires' Club"
        self.assertEqual(a, print(message))
        self.assertEqual(b, message)

    def test_name_list(self):
        db = mr.initialize_database()
        a = mr.show_current_names(db)
        b = 'The current donors are William Gates, III, Mark Zuckerberg, Jeff Bezos, and Paul Allen.'
        self.assertEqual(a, print(b))

    def test_report(self):
        db = mr.initialize_database()
        a = mr.create_report(db)
        b = 'Donor Name                | Total Given | Num Gifts | Average Gift' \
            '\n------------------------------------------------------------------'\
            '\nWilliam Gates, III        $    653784.49           2 $   326892.24'\
            '\nMark Zuckerberg           $     16396.10           3 $     5465.37'\
            '\nJeff Bezos                $       877.33           1 $      877.33'\
            '\nPaul Allen                $       708.42           3 $      236.14'

        self.assertEqual(a, print(b))


if __name__ == '__main__':
    unittest.main()
