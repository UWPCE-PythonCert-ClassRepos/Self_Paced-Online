import unittest
import mailroom4
from mailroom4 import check_input
from mailroom4 import check_donation
from mailroom4 import create_report
from mailroom4 import letters_to_everyone

class MyTests(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_check_input_is_quit(self):
        self.assertFalse(check_input('quit'))
        
    def test_check_input_is_list(self):
        self.assertTrue(check_input('list'))
        
    def test_check_input_is_new_donor(self):
        self.assertIsNone(check_input('New Donor'))
        
    def test_check_donation_is_quit(self):
        self.assertFalse(check_donation('New Donor', 'quit'))
        
    def test_check_donation_is_non_number(self):
        self.assertTrue(check_donation('New Donor', 'Non-number'))
        
    def test_check_donation_existing_donor(self):
        self.assertIsNone(check_donation('Ralph Anders', 300))
        self.assertIn(300, mailroom4.donors_list['Ralph Anders'])
        
    def test_check_donation_new_donor(self):
        self.assertIsNone(check_donation('New Donor', 400.56))
        self.assertIn(400.56, mailroom4.donors_list['New Donor'])
        
    def test_create_report(self):        
        self.assertEqual(create_report(), mailroom4.reportvariable)
        
    def test_create_report_sorting(self):
        self.assertEqual(mailroom4.sorted_donors, (sorted(mailroom4.donors_list.items(), key=lambda k: sum(k[1]), reverse=True)))
    
    def test_letters_to_everyone_files(self):
        letters_to_everyone()
        for i, val in mailroom4.donors_list.items():
            with open(f'{i}.txt', 'r') as outfile:
                donation = sum(val)
                check_text = f'Dear {i}, \n\n{mailroom4.tab}Thank you very much for your most recent donation \
of ${val[-1]:.2f}! \n\n{mailroom4.tab}You have now donated a total of ${donation:.2f}. \n\n{mailroom4.tab}Your support \
is essential to our success and will be well utilized. \n\n{mailroom4.tab*2}Sincerely, \n{mailroom4.tab*3}-The Company'
                self.assertEqual(check_text, outfile.read())

if __name__ == '__main__':
    unittest.main()