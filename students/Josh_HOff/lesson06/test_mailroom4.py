import unittest
import mailroom4
from mailroom4 import check_input
from mailroom4 import check_donation
from mailroom4 import create_report
from mailroom4 import letters_to_everyone
from mailroom4 import add_donation_to_list

class MyTests(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_01_check_input_is_quit(self):
        self.assertFalse(check_input('quit'))
        
    def test_02_check_input_is_list(self):
        self.assertTrue(check_input('list'))
        
    def test_03_check_input_is_new_donor(self):
        self.assertIsNone(check_input('New Donor'))
        
    def test_04_check_donation_is_quit(self):
        self.assertFalse(check_donation('New Donor', 'quit'))
        
    def test_05_check_donation_is_non_number(self):
        self.assertTrue(check_donation('New Donor', 'Non-number'))
        
    def test_06_check_donation_existing_donor(self):
        self.assertIsNone(check_donation('Ralph Anders', 300))
        
    def test_07_existing_donor_in_list(self):
        add_donation_to_list('Ralph Anders', 300)
        self.assertIn(300, mailroom4.donors_list['Ralph Anders'])
        
    def test_08_check_donation_new_donor(self):
        self.assertIsNone(check_donation('New Donor', 400.56))
        
    def test_09_new_donor_in_list(self):
        add_donation_to_list('New Donor', 400.56)
        self.assertIn(400.56, mailroom4.donors_list['New Donor'])  
                
    def test_10_create_report(self):
        self.assertEqual(create_report(), 'Donor Name             | Total Given | Num Gifts | Average Gift\n\
---------------------------------------------------------------\n\
New Donor               $      400.56           1      400.56\n\
Andrei Wasinski         $      327.00           3      109.00\n\
Ralph Anders            $      315.00           3      105.00\n\
Angelica Kisel          $      125.60           3       41.87\n\
James Hendrick          $       60.00           1       60.00\n\
Stalk Holmes            $       40.00           1       40.00\n\
Traci Johnston          $       20.00           1       20.00')
        
    def test_11_create_report_sorting(self):
        create_report()
        self.assertEqual(mailroom4.sorted_donors, [('New Donor', [400.56]), ('Andrei Wasinski',\
        [101, 151, 75]), ('Ralph Anders', [5, 10, 300.0]), ('Angelica Kisel', [45, 25, 55.6]),\
        ('James Hendrick', [60]), ('Stalk Holmes', [40]), ('Traci Johnston', [20])])

    def test_12_letters_to_everyone_files(self):
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