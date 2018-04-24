import unittest
import mailroom6
import os.path
import io
import sys



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
        self.DonorDict.challenge(5)
        print(self.DonorDict.donors.keys())
        print(self.DonorDict.donors.values())


if __name__ == '__main__':
    unittest.main()
