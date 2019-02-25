import unittest
import mailroom5
import os
from mailroom5 import *

class TestMailroom(unittest.TestCase):
    """Write a class containing a full suite of tests"""

    def test_donor_class(self):
        """Check that the data for individual donors is being saved properly"""

        test_donor1 = Donor('test_donor',[100.00])
        test_donor2 = Donor('test_donor2',[200.00])
        test_donor1.add_donation(float(50))
        test_donor1.name = 'test_donor1'
        comparison = test_donor1 < test_donor2
        expected_letter = """Dear test_donor1,

Thank you for your generous donation of $50.00.

Sincerely,
The Charity
"""
        self.assertEqual(test_donor1.donations,[100.00,50])
        self.assertTrue(comparison)
        self.assertEqual(test_donor1.num_gifts(),2)
        self.assertEqual(test_donor1.total_given(),150.00)
        self.assertEqual(test_donor1.average(),75)
        self.assertEqual(test_donor1.letter(),expected_letter)
        self.assertEqual(test_donor1.average(),75)

    def test_collection_class(self):
        """Check that the data for a collection of donors is being saved properly"""

        test_collection = Collection([Donor('test_donor1',[100.00]),Donor('test_donor2',[200.00])])
        test_collection.add_new(Donor('test_donor3',[300.00]))
        expected_list = 'test_donor1, test_donor2, test_donor3'
        self.assertEqual(test_collection.list_all(),expected_list)


    def test_table(self):
        """Test table output format"""
        expected ="""
Donor Name              | Total Given |  Num Gifts  |  Average Gift   
-------------------------------------------------------------------
William Gates, III       $   653784.49             2 $    326892.24
Mark Zuckerberg          $    16396.10             3 $      5465.37
Jeff Bezos               $      877.33             1 $       877.33
Paul Allen               $      708.42             3 $       236.14
"""
        actual = collection.create_report()
        self.assertEqual(expected,actual)

    def test_send_all(self):
        """Test that all letters were printed to text files successfully"""
        collection.send_all()
        for person in collection.names:
            self.assertTrue(os.path.exists(str(person).replace(' ','_')+'.txt'))
            try:
                with open(str(person).replace(' ','_')+'.txt','r') as f:
                    actual = f.read()
            except FileNotFoundError:
                print("The file wasn't created")
                actual = ''
            expected = person.letter()
            self.assertEqual(expected,actual)

if __name__ == '__main__':
     unittest.main()
 