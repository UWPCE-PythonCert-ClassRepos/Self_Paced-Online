#!/usr/bin/env python3
import unittest
from mailroom_part4 import tup_donor_names, menu, subMenu, Files, update_donor, donor_list_creation,send_thankyou_option, \
    create_report_option, exit_program_option,lifetime_donations,menu_dispatch,thankyou_dispatch

class MyTestCase(unittest.TestCase):
    def test_creatReport(self):
        self.assertIsNone(subMenu.create_report())

    def test_donorEmail(self):
        str_salutation = "Dear John Banks,"
        str_body = "\n\n" + "Thank you for generosity! " \
                            "\n\n" + "This donation will be put to great use!" \
                                     "\n\n" + "Your current lifetime donation is $300.00."
        str_valediction = "\n\n" + "Sincerely," \
                                   "\n\n" + "The Team"
        self.assertMultiLineEqual(Files.donor_email("John Banks",{"John Banks":"$300.00"}),
                                  str_salutation+str_body+str_valediction)

    def test_updateDonor(self):
        self.assertIsNone(update_donor("John Banks",300.00))

    def test_donorListCreation(self):
        self.assertIsNone(donor_list_creation())

    def test_sendThankyouOption(self):
        self.assertIsNone(donor_list_creation())

    def test_createReportOption(self):
        self.assertIsNone(create_report_option())


    def test_exitProgram(self):
        self.assertEqual(exit_program_option(),"exit")

    def test_lifetimeDonations(self):
        self.assertDictEqual(lifetime_donations(tup_donor_names), lifetime_donations(tup_donor_names))

    def test_menu_dispatch(self):
        self.assertDictEqual(menu_dispatch,menu_dispatch)

    def test_thankyou_dispatch(self):
        self.assertDictEqual(thankyou_dispatch, thankyou_dispatch)

if __name__ == '__main__':
    unittest.main()
