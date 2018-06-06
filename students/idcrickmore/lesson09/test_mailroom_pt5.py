import mailroom_pt5 as m
import unittest

data = [50, 200, 100, 250]

        
class test_Donor(unittest.TestCase):

    def test_donations(self):
        test = m.Donor(data)
        self.assertEqual(test.donation, [50, 200, 100, 250])
        
    def test_total(self):
        test = m.Donor(data)
        self.assertEqual(test.total, 600)
        
    def test_ave(self):
        test = m.Donor(data)
        self.assertEqual(test.ave, 150)
        
    def test_num(self):
        test = m.Donor(data)
        self.assertEqual(test.num_donations, 4)
        
    def test_last(self):
        test = m.Donor(data)
        self.assertEqual(test.last, 250)
        
    def test_str(self):
        test = m.Donor(data)
        self.assertEqual(str(test), "600            150.00         4              ")

# class test_Donor_oporations(unittest.TestCase):
    
    

        
if __name__ == '__main__':
    unittest.main()