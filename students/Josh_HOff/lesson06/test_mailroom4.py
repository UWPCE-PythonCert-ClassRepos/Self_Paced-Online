import unittest
import mailroom4
from mailroom4 import check_input
from mailroom4 import check_donation
from mailroom4 import create_report

class MyTests(unittest.TestCase):

    def setUp(self):
        pass
    def test_1(self):
        self.assertFalse(check_input('quit'))
    def test_2(self):
        self.assertTrue(check_input('list'))
    def test_3(self):
        self.assertIsNone(check_input('New Donor'))
    def test_4(self):
        self.assertFalse(check_donation('New Donor', 'quit'))
    def test_5(self):
        self.assertTrue(check_donation('New Donor', 'Non-number'))
    def test_6(self):
        self.assertIsNone(check_donation('Ralph Anders', 300))
        self.assertIn(300, mailroom4.donors_list['Ralph Anders'])
    def test_7(self):
        self.assertIsNone(check_donation('New Donor', 400.56))
        self.assertIn(400.56, mailroom4.donors_list['New Donor'])
    def test_8(self):        
        self.assertEqual(create_report(), (mailroom4.top + mailroom4.rows))
if __name__ == '__main__':
    unittest.main()