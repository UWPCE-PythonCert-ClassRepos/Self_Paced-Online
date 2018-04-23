import sys
import os
import unittest
import mailroom5 as mr5
from collections import defaultdict



class TestMailRoom5(unittest.TestCase):
    def test_donor_class(self):
        test = mr5.Donor('test1',999)
        self.assertEqual(test.name, 'test1')
        self.assertEqual(test.donation, 999)


    def test_add_donor_in_data(self):
        donor_data = mr5.donor_data
        test1 = mr5.Donor('test1',999)
        test1.add_donor_in_data()
        test1 = mr5.Donor('test1',777)
        test1.add_donor_in_data()
        test2 = mr5.Donor('test2',888)
        test2.add_donor_in_data()

        self.assertEqual(donor_data['test2'], [888])
        self.assertEqual(donor_data['test1'], [999,777])


    def test_collection(self):
        test_data=defaultdict(list, {'test1':[999,888], 'test2':[777]})
        test = mr5.Collection(test_data)
        test.send_letters_to_everyone()
        self.assertEqual(test.sum_donation('test1'), 1887)
        self.assertEqual(test.last_donation('test1'), 888)
        assert os.path.isfile('test1.txt')
        assert os.path.isfile('test2.txt')


















if __name__ == '__main__':
    unittest.main()
