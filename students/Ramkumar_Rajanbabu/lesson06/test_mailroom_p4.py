#Mailroom Part 4 Test

import unittest
import os
import mailroom_p4 as m

class TestMailroom(unittest.TestCase):
    """Write a class with a full suite of unit tests. Not sure how to test display_report()/create_table()"""
    
    def test_donor_names(self):
        expected = ["William Gates, III", "Mark Zuckerberg", "Jeff Bezos", "Paul Allen","Ramkumar Rajanbabu"]
        actual = list(m.donors_db)
        self.assertEqual(expected, actual)

    def test_table_calculations(self):
        expected = [('William Gates, III', 653784.49, 2, 326892.245), ('Mark Zuckerberg', 16396.1, 3, 5465.366666666666), ('Jeff Bezos', 877.33, 1, 877.33), ('Paul Allen', 708.4200000000001, 3, 236.14000000000001), ('Ramkumar Rajanbabu', 255.65, 3, 85.21666666666667)]
        actual = m.calc_donor()
        self.assertEqual(expected, actual)
    
    def test_letter(self):
        expected = "\n\tDear Ram, \n\n\tThank you for choosing to donate to this group. A special thank you for your generous donation of $25.00. \n\n\tSincerely, \n\tDonation Society"
        actual = m.write_letter("Ram", 25)
        self.assertEqual(expected, actual)
    
    def test_file_names(self):
        assert os.path.isfile("William Gates, III.txt")
        assert os.path.isfile("Mark Zuckerberg.txt")
        assert os.path.isfile("Jeff Bezos.txt")
        assert os.path.isfile("Paul Allen.txt")
        assert os.path.isfile("Ramkumar Rajanbabu.txt")
        
if __name__ == "__main__":
    unittest.main()
