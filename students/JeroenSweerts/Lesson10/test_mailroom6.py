import unittest
import mailroom6
import os.path
import io
import sys
from functools import reduce



class TestMailroom(unittest.TestCase):
    def setUp(self):
        self.donors = {}
        self.donors['papa'] = [100, 5, 15]
        self.donors['mama'] = [12, 200, 2, 66]
        self.donors['bompa'] = [1000]
        self.donors['bobonne'] = [500, 500]
        self.donors['onbekende'] = [1000000]


    def test_challenge(self):
        self.DonorDict = mailroom6.Donor_Collection(self.donors)
        self.DonorDict.challenge(1, 5, 0, 1000)
        self.assertEqual(self.DonorDict.donors,{'papa': [100, 5, 15], 'mama': [12, 200, 2, 66], 'bompa': [1000], 'bobonne': [500, 500], 'onbekende': [1000000]})


if __name__ == '__main__':
    unittest.main()
