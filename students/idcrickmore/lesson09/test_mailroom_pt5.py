import mailroom_pt5 as m
import unittest

donor_data = m.donor_data

        
class test_Donor(unittest.TestCase):

    def test_donations(self):
        test = m.Donor(donor_data['Jill'])
        self.assertEqual(test.donation, [50, 200, 100, 250])
        
    def test_total(self):
        test = m.Donor(donor_data['Jill'])
        self.assertEqual(test.total, 600)
        
    def test_ave(self):
        test = m.Donor(donor_data['Jill'])
        self.assertEqual(test.ave, 150)
        
    def test_num(self):
        test = m.Donor(donor_data['Jill'])
        self.assertEqual(test.num_donations, 4)
        
    def test_last(self):
        test = m.Donor(donor_data['Jill'])
        self.assertEqual(test.last, 250)
        


class test_Donor_oporations(unittest.TestCase):

    def test_donor_append(self):
        m.Donor_ops.donor_append('Jill', 99)
        self.assertEqual(donor_data['Jill'], [50, 200, 100, 250, 99])
    
    def test_thank_you_self(self):
        expected = (
                    "Dear Jill,\n\n"
                    "You rock. Your fat contribution of $99.00\n"
                    "will go a long way to lining my pockets.\n\n"
                    "Sincerely,\n"
                    "Scrooge McDuck")
        actual = m.Donor_ops.thank_you('Jill')
        
        # assert expected == actual
        self.assertEqual(m.Donor_ops.thank_you('Jill'), expected)
    

        
if __name__ == '__main__':
    unittest.main()