from donor import Donor
import unittest

class TestDonor(unittest.TestCase):


    def test_good_init(self):
        d = Donor('John Camp')
        self.assertEqual(d.first_name, 'John')
        self.assertEqual(d.last_name, 'Camp')
 
    def test_bad_init(self):
        d = Donor('John')
        self.assertRaises(IndexError,d)

if __name__ == '__main__':
    unittest.main()
 
