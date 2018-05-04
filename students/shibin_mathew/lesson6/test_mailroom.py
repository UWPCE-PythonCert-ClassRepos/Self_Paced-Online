import unittest
from collections import defaultdict
from mailroom import *



class MailroomTestCase(unittest.TestCase):
    # Tests for 'mailroom.py'
    def test_switch_menu(self):
        self.assertEqual(switch_menu('1'), send_thank_you)
        self.assertEqual(switch_menu('2'), create_report)
        self.assertEqual(switch_menu('3'), send_letters)
        self.assertEqual(switch_menu('4'), quit_menu)

    def test_send_letters(self):
        list_test = []
        list_test2 = []
        #  Test 1
        for names in donors2:
            list_test.append(names+'.txt')
        self.assertEqual(send_letters(donors2), list_test)
        #  Test 2
        for names in donors:
            list_test2.append(names+'.txt')
        self.assertEqual(send_letters(donors), list_test2)

    def test_create_report(self):
        list_test = []
        list_test2 = []
        #  Test 1
        for names in donors2:
            list_test.append([names, round(sum(donors2[names]), 2), len(donors2[names]),
                             round(sum(donors2[names]) / len(donors2[names]), 2)])
        self.assertEqual(create_report(donors2), list_test)
        #  Test 2
        for names in donors:
            list_test2.append([names, round(sum(donors[names]), 2), len(donors[names]),
                             round(sum(donors[names]) / len(donors[names]), 2)])
        self.assertEqual(create_report(donors), list_test2)

    def test_print_donor_names(self):
        list_test = []
        list_test2 = []
        #  Test 1
        for names in donors2:
            list_test.append(names)
        self.assertEqual(print_donor_names(donors2), list_test)
        #  Test 2
        for names in donors:
            list_test2.append(names)
        self.assertEqual(print_donor_names(donors), list_test2)

if __name__ == '__main__':
    #  Example 1
    list_ = [('Shibin', 25.25), ('Shibin', 456.25), ('Kimberly', 125.50), ('Kimberly', 5.55), ('Jordy', 55),
             ('Jordy', 25), ('Andreck', 35)]
    donors2 = defaultdict(list)
    for name, amount in list_:
        donors2[name].append(amount)

    #  Example 2
    list2_ = [('Andrew', 1250), ('Andrew', 16.25), ('Alice', 54), ('Alice', 17.55), ('Alice', 55),
             ('Craig', 126.39), ('Craig', 45.25), ('Craig', 14.24)]
    donors = defaultdict(list)
    for name, amount in list2_:
        donors[name].append(amount)
    unittest.main()
