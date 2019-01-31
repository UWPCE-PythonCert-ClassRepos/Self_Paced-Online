import unittest
import mailroom4
import os
from mailroom4 import *

class TestMailroom(unittest.TestCase):
    """Write a class containing a full suite of tests"""

    def test_letter(self):
        """Test letter output"""
        test_dictionary = {'donor':"ME", 'amount': round(float(100),2)}
        expected = """
Dear ME,

Thank you for your generous donation of $100.00

Sincerely,
The Charity
"""
        actual = mailroom4.letter(test_dictionary)
        self.assertEqual(expected,actual)

    def test_calculation(self):
        """Test average and donation count calculations"""
        expected = [['William Gates, III', "$", 653784.49, 2, "$", 326892.24],
['Mark Zuckerberg', "$", 16396.10, 3, "$", 5465.37],
['Jeff Bezos', "$", 877.33, 1, "$", 877.33],
['Paul Allen', "$", 708.42, 3, "$", 236.14]]
        actual = mailroom4.calculation()
        self.assertEqual(expected,actual)

    def test_table(self):
        """Test table output format"""
        expected ='\nDonor Name              | Total Given |  Num Gifts  |  Average Gift   \n-------------------------------------------------------------------\nWilliam Gates, III       $   653784.49             2 $    326892.24\nMark Zuckerberg          $    16396.10             3 $      5465.37\nJeff Bezos               $      877.33             1 $       877.33\nPaul Allen               $      708.42             3 $       236.14\n'
        actual = mailroom4.table(mailroom4.calculation())
        self.assertEqual(expected,actual)

    def test_send_all(self):
        """Test that all letters were printed to text files successfully"""
        mailroom4.send_all()
        for person in donation_data:
            self.assertTrue(os.path.exists(person.replace(' ','_')+'.txt'))
            try:
                with open(person.replace(' ','_')+'.txt','r') as f:
                    actual = f.read()
            except FileNotFoundError:
                print("The file wasn't created")
                actual = ''
            expected = mailroom4.letter({'donor':person,'amount':donation_data[person][-1]})
            self.assertEqual(expected,actual)

if __name__ == '__main__':
     unittest.main()
 