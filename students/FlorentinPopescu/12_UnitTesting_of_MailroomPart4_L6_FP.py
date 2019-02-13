# -*- coding: utf-8 -*-
"""
Created on Tue Feb 5 13:12:17 2019
@author: Florentin Popescu
"""

#===================LESSON_06====================

#================================================
# Unit Testing for Mailroom Part 4
#================================================
import os, io, sys, importlib, unittest, fnmatch, shutil
mailroom = importlib.import_module("11_Mailroom_Part3_L5_FP", package = None)

from contextlib import redirect_stdout
from unittest import TestCase

#================================================
class MailroomTest(TestCase):
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
    def test_donors(self):
        donors_records = ["Name1", "Name2", "Name3", "Name5", "Name6", "Name7"]
        self.assertListEqual(list(mailroom.donors), donors_records)
        self.assertEqual(mailroom.donors["Name1"], [1, 10, 100])
        self.assertEqual(mailroom.donors["Name2"], [5.5, 15.5, 25.5])
        
#------------------------------------------------
    def test_check_name(self):
        self.assertNotRegex("Florentin", "@Florentin", msg = None)
        self.assertEqual(mailroom.check_name("Florentin"), False)
        self.assertEqual(mailroom.check_name("@Florentin"), True)
           
#------------------------------------------------
    def test_letter(self):
        test = """\nDear Florentin, \nThank you for you donation of $20.00 to our charity. \nSincerely."""         
        self.assertEqual(mailroom.letter("Florentin", 20), test)

#------------------------------------------------
    def test_add_donation(self):
        mailroom.add_donation(mailroom.donors, "Florentin", 20)
        self.assertEqual(20, mailroom.donors["Florentin"][0])
        del mailroom.donors["Florentin"]

#------------------------------------------------
    def test_write_letter(self):
        Florentin = io.StringIO()
        
        with redirect_stdout(Florentin):
            mailroom.write_letter({"Florentin": [20]})
        
        out = Florentin.getvalue()
        self.assertEqual("Prepared letter for 'Florentin'.\n", out)
        self.assertFalse(os.path.isdir("./Florentin.txt"))
        self.assertTrue(os.path.exists("Florentin.txt"), "Florentin.txt")
        
        with open("Florentin.txt", "r") as f:
            text = f.read()
        self.assertEqual("\nDear Florentin, \nThank you for you donation of $20.00 to our charity. \nSincerely.", text)
  
#------------------------------------------------
    def test_switch_directories(self):
        current_directory = os.getcwd()
        new_directory = "repository"
        final_directory = os.path.join(current_directory, new_directory)
        
        if not os.path.exists(final_directory):
           os.makedirs(final_directory)
        
        mailroom.switch_directories(mailroom.donors, current_directory, new_directory)
        self.assertEqual(len(mailroom.donors), len(os.listdir(new_directory)))
        
        for file in os.listdir("./repository"):
            self.assertEqual(fnmatch.fnmatch(file, "*.txt"), True)
        
#------------------------------------------------
    def test_report(self):
        orig_stdout = sys.stdout
        f =  open("report.dat", "w")
        sys.stdout = f
        mailroom.report(mailroom.donors)
        sys.stdout = orig_stdout
        f.close()
        
        with open("report.dat", "r") as f:
            rows = [line for line in f]  
        
        del rows[0:2]
        self.assertEqual(rows[1].replace(" ", ""), "DonorName|TotalGiven|NumGifts|AverageGift\n")
        self.assertEqual(rows[3].replace(" ", ""), "Name3|$1,000,000.00|1|1,000,000.00\n")
        self.assertEqual(rows[3].replace(" ", "").split("|")[1], "$1,000,000.00")
 
#------------------------------------------------
    def test_switch_dict(self): 
        test = ['name_donation_letter', 'report', 'sendletter_everyone', 'quit_program']
        switch_dict_val = [str([item for item in mailroom.switch_dict.values()][i]).split()[1] for i in range(len(mailroom.switch_dict))]
        self.assertCountEqual(switch_dict_val, test)
        self.assertListEqual(switch_dict_val, test)
        self.assertEqual(switch_dict_val, test)
        
#------------------------------------------------
    def test_name_donation_letter(self):
        test_donors = {"A":[1,2], "B":[3,4]}
        test_print_letter = "Thank you for your donation"
        test_bad_name_entered = "We are sorry,"
        test_negative_amount_entered = "We accept only positive donations."
        test_wrong_amount = "Wrong amount"
        test_error_on_wrong_ammount = "TypeError"
        
        print("\n'quit' to exit testing and see tests results:")
        try:
            sys.stdout = open("temp_output.txt", "w")
            mailroom.name_donation_letter(test_donors)
            
            with open("temp_output.txt", "r") as f:
                words = " ".join([line.strip() for line in f]).split()  
                
                if not words:
                    self.assertListEqual(words, [])
                    sys.stdout.flush()
            
                elif (words[0] == "Existing"):  
                    self.assertListEqual([words[2], words[5]], list(test_donors.keys()))
                    sys.stdout.flush()
                            
                elif all(elem in words for elem in "Dear"):
                    self.assertListEqual(" ".join(words[6:11]), test_print_letter)
                    sys.stdout.flush()
                    
                elif words[0] == "We":
                    self.assertEqual(" ".join(words[0:3]) , test_bad_name_entered)
                    sys.stdout.flush()
                    
                elif all(elem in words for elem in "Please enter a donation to become one of our donors.".split()):   
                    self.assertEqual(" ".join(words[4:9]) , test_negative_amount_entered)
                    sys.stdout.flush()
                    
        except TypeError:
            self.assertRaises(TypeError) 
            print(sys.exc_info())
            
            with open("temp_output.txt", "r") as f:
                words = " ".join([line.strip() for line in f]).split()  
            
            if all(elem in words for elem in "not convert string to float:".split()):
                    self.assertEqual(" ".join(words[4:6]), test_wrong_amount)
                    self.assertEqual(''.join([letter for letter in words[21] if letter.isalpha()]), test_error_on_wrong_ammount)
                    sys.stdout.flush() 
        
#================================================
if __name__ == '__main__':
    unittest.main()
    os.remove("Florentin.txt")
    os.remove("report.dat")
    shutil.rmtree("repository")
    
#================================================
#--------------- END ----------------------------
#================================================

