import unittest
import mailroom4
from mailroom4 import *

#Write a class containing a full suite of tests
class mailroom_tests(unittest.TestCase):

#Test letter output
    def test_letter(self):
        test_dictionary = {'donor':"ME", 'amount': round(float(100),2)}
        expected = """
Dear ME,

Thank you for your generous donation of $100.00

Sincerely,
The Charity
"""
        actual = mailroom4.letter(test_dictionary)
        self.assertEqual(expected,actual)

#Test average and donation count calculations
    def test_calculation(self):
        expected = [['William Gates, III', "$", 653784.49, 2, "$", 326892.24],
['Mark Zuckerberg', "$", 16396.10, 3, "$", 5465.37],
['Jeff Bezos', "$", 877.33, 1, "$", 877.33],
['Paul Allen', "$", 708.42, 3, "$", 236.14]]
        actual = mailroom4.calculation()
        self.assertEqual(expected,actual)

#Test table output format
    def test_table(self):
        expected ="""Donor Name              | Total Given |  Num Gifts  |  Average Gift
-------------------------------------------------------------------
William Gates, III       $   653784.49             2 $    326892.24
Mark Zuckerberg          $    16396.10             3 $      5465.37
Jeff Bezos               $      877.33             1 $       877.33
Paul Allen               $      708.42             3 $       236.14"""
        actual = mailroom4.table(mailroom4.calculation())

#Test that all letters were printed to text files successfully
    def test_send_all(self):
        mailroom4.send_all()
        for person in donation_data:
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
 