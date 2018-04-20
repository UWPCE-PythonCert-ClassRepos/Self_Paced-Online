import unittest
import mailroom5
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

    def test_create_donor(self):
        self.Donor = mailroom5.Donor('jeroen')
        self.assertEqual(self.Donor.name, 'jeroen')
        self.assertEqual(self.Donor.donations, [])

    def test_create_donor_collection(self):
        self.DonorDict = mailroom5.Donor_Collection(self.donors)
        self.assertEqual(self.DonorDict.donors, \
            {'papa': [100, 5, 15], 'mama': [12, 200, 2, 66], \
            'bompa': [1000], 'bobonne': [500, 500], 'onbekende': [1000000]})

    def test_add_donor(self):
        self.DonorDict = mailroom5.Donor_Collection(self.donors)
        self.donor = mailroom5.Donor('jeroen')
        self.DonorDict.add_donor(self.donor)
        self.assertEqual(self.DonorDict.donors, \
            {'papa': [100, 5, 15], 'mama': [12, 200, 2, 66], \
            'bompa': [1000], 'bobonne': [500, 500], 'onbekende': [1000000], 'jeroen': []})

    def test_donate1(self):
        self.DonorDict = mailroom5.Donor_Collection(self.donors)
        self.DonorDict.donate('onbekende', 2)
        self.assertEqual(self.DonorDict.donors, \
            {'papa': [100, 5, 15], 'mama': [12, 200, 2, 66], \
            'bompa': [1000], 'bobonne': [500, 500], 'onbekende': [1000000, 2]})

    def test_donate2(self):
        self.DonorDict = mailroom5.Donor_Collection(self.donors)
        self.DonorDict.donate('jeroen', 2)
        self.assertEqual(self.DonorDict.donors, \
            {'papa': [100, 5, 15], 'mama': [12, 200, 2, 66], \
            'bompa': [1000], 'bobonne': [500, 500], 'onbekende': [1000000], 'jeroen': [2]})

    def test_thankyou(self):
        self.DonorDict = mailroom5.Donor_Collection(self.donors)
        mailroom5.thankyou(self.DonorDict)

    def test_createfile(self):
        self.DonorDict = mailroom5.Donor_Collection(self.donors)
        self.DonorDict.createfile('mama')

    def test_thankyoueveryone(self):
        self.DonorDict = mailroom5.Donor_Collection(self.donors)
        mailroom5.thankyoueveryone(self.DonorDict)

    def test_create_report(self):
        self.DonorDict = mailroom5.Donor_Collection(self.donors)
        self.DonorDict.create_report()

    def test_report(self):
        self.DonorDict = mailroom5.Donor_Collection(self.donors)
        mailroom5.report(self.DonorDict)


if __name__ == '__main__':
    unittest.main()
