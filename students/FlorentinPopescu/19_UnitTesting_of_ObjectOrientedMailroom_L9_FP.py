# -*- coding: utf-8 -*-
"""
Created on Tu Mar 5 12:31:07 2019
@author: Florentin Popescu
"""

#===================LESSON_09====================
# Unit Testing for Object-Oriented Mailroom
#================================================
#imports
from unittest import TestCase
import importlib, unittest
oo_mailroom = importlib.import_module("18_Object_Oriented_Mailroom_L9_FP", package = None)

#================================================
class OO_MailroomTest(TestCase):
    """
    Methods to alocate and free external resources nedded for the tests
    """
    # called before each test 
    def setUp(self):
        pass
    
    # called after each test
    def tearDown(self):
        pass
        
    #------------------------------------------------
    # test initializers
    #------------------------------------------------
    def test_donor_name_and_donation(self):
        donor_name = oo_mailroom.Donor("Florentin")
        donor_donation = oo_mailroom.Donor("Florentin", 20)
        self.assertEqual(donor_name.name, "Florentin")
        self.assertEqual(donor_donation.donations, 20)
    
    def test_add_new_donor(self):
        old_donors = oo_mailroom.DonorsDataSet(["Florentin1", "Florentin2"])
        new_donor = oo_mailroom.Donor("Florentin3")
        old_donors.add_new_donor(new_donor)
        self.assertEqual(old_donors.donors[2].name, "Florentin3")

    #------------------------------------------------
    # test repers
    #------------------------------------------------
    def test_reper_DonorClass(self):
        donor = oo_mailroom.Donor("Florentin", 20)
        self.assertEqual(str(donor), "Donor Florentin : donation = 20")

    def test_reper_DonorsDataSetClass(self):
        donors = oo_mailroom.DonorsDataSet([oo_mailroom.Donor("Florentin1", 10), oo_mailroom.Donor("Florentin2", 20)])
        self.assertEqual(str(donors), "Donors database: [Donor Florentin1 : donation = 10, Donor Florentin2 : donation = 20]")

    #------------------------------------------------
    # test added donation 
    def test_add_donations(self):
        donor = oo_mailroom.Donor("Florentin")
        donor.add_donations(20)
        self.assertEqual([20], donor.donations)

    #------------------------------------------------
    # test existing donors and donations 
    def test_list_donors(self):
        donors = oo_mailroom.DonorsDataSet([oo_mailroom.Donor("Florentin1", 10), oo_mailroom.Donor("Florentin2", 20)])
        self.assertEqual(donors.list_donors(), ['Florentin1', 'Florentin2'])
        self.assertEqual(donors.list_donations(), [10, 20])
        
    #------------------------------------------------
    # test statistics
    #------------------------------------------------
    def test_number_donations(self):
        donor = oo_mailroom.Donor("Florentin")
        donor.add_donations(10)
        donor.add_donations(20)
        donor.add_donations(30)
        self.assertEqual(3, donor.number_donations())

    def test_sum_donations(self):
        donor = oo_mailroom.Donor("Florentin")
        donor.add_donations(10)
        donor.add_donations(20)
        donor.add_donations(30)
        self.assertEqual(60, donor.sum_donations())
        
    def test_average_donation(self):
        donor = oo_mailroom.Donor("Florentin")
        donor.add_donations(10)
        donor.add_donations(20)
        donor.add_donations(30)
        self.assertEqual(20, donor.average_donations())

    #------------------------------------------------
    # test static methods 
    #------------------------------------------------
    # name's validity
    def test_check_name(self):
        self.assertNotRegex("Florentin", "@Florentin", msg = None)
        self.assertEqual(oo_mailroom.Donor.check_name("Florentin"), False)
        self.assertEqual(oo_mailroom.Donor.check_name("@Florentin"), True)
       
    # letter's validity
    def test_letter(self):
        letter = """\nDear Florentin, \nThank you for you donation of $20.00 to our charity. \nSincerely."""         
        self.assertEqual(oo_mailroom.Donor.letter("Florentin", 20), letter)

    #------------------------------------------------
    # test report
    def test_stat_report(self):
        donor = oo_mailroom.DonorsDataSet([oo_mailroom.Donor("Florentin1", [10, 20, 30, 40, 50])])
        self.assertEqual(donor.stat_report(), "Florentin1          |                150|                 5|              30.0\n")


#================================================
if __name__ == '__main__':
    unittest.main()

#================================================
#--------------- END ----------------------------
#================================================
