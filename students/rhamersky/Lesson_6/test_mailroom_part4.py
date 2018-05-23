#!/usr/bin/env python3
import unittest
from mailroom_part4 import Files, update_donor, dic_sort, menu_options

class MyTestCase(unittest.TestCase):

    def test_donor_email(self):
        str_salutation = "Dear Paul Allen,"
        str_body = "\n\n" + "Thank you for generosity! " \
                            "\n\n" + "This donation will be put to great use!" \
                                     "\n\n" + "Your current lifetime donation is $5,000.00."
        str_valediction = "\n\n" + "Sincerely," \
                                   "\n\n" + "The Team"
        self.assertMultiLineEqual(Files.donor_email("Paul Allen"),
                                  str_salutation+str_body+str_valediction)

    def test_update_donor(self):
        self.assertEqual(update_donor("Jeff Bezos",300.00),{"William Gates, III":[10000.0, 1],
                                                            "Mark Zuckerberg":[20000.0, 1],
                                                            "Jeff Bezos":[1500.0, 2],
                                                            "Paul Allen":[5000.0, 1],
                                                            "Mike Scott":[25.0, 1]})

        self.assertEqual(update_donor("John Banks",300.00),{"William Gates, III":[10000.0, 1],
                                                            "Mark Zuckerberg":[20000.0, 1],
                                                            "Jeff Bezos":[1500.0, 2],
                                                            "Paul Allen":[5000.0, 1],
                                                            "Mike Scott":[25.0, 1],
                                                            "John Banks":[300.0, 1]})

    def test_dic_sort(self):
        self.assertEqual(dic_sort(), {"William Gates, III": [10000.0, 1],
                                                            "Mark Zuckerberg": [20000.0, 1],
                                                            "Jeff Bezos": [1200.0, 1],
                                                            "Paul Allen": [5000.0, 1],
                                                            "Mike Scott": [25.0, 1]})


if __name__ == '__main__':
    unittest.main()
