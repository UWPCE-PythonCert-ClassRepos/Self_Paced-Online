from donor_collection import DonorCollection
from donor import Donor
import unittest
import sys, os 

class TestDonorCollection(unittest.TestCase):

    bad_name = 'Wolf'
    bad_amount = 'not a number'
    good_name = 'Wolf Man'
    good_amount = '900'

    def test_validate_and_create_thank_you_bad_name(self):
        dc = DonorCollection()
        output = dc.validate_and_create_thank_you(self.bad_name, self.good_amount)
        self.assertEqual(output, 'Could not send thank you.  The first and last name of donor must be provided\n')
 
    def test_validate_and_create_thank_you_bad_amount(self):
        dc = DonorCollection()
        output = dc.validate_and_create_thank_you(self.good_name, self.bad_amount)
        self.assertEqual(output, f"invalid donation amount: {self.bad_amount}")

    def test_validate_and_create_thank_you_good_values(self):
        dc = DonorCollection()
        d = Donor(self.good_name)

        amount_list = dc.donation_dict.get(self.good_name, [])
        amount_list.append(float(self.good_amount))

        output = dc.validate_and_create_thank_you(self.good_name, self.good_amount)
        #print('\n' + output)
        #print(f"Hi {self.good_name}\nThank you for your donation of {self.good_amount} to the mailroom!\n")
        #self.assertEqual(output == f"Hi {self.good_name}\nThank you for your donation of {self.good_amount} to the mailroom!\n"
        
        new_amount_list = dc.donation_dict[self.good_name]
        self.assertEqual(amount_list, new_amount_list)

    def test_write_letters(self):
        dc = DonorCollection()
        donation_count = 0
        for donor in dc.donation_dict.keys():
            donation_count += len(dc.donation_dict[donor]) 
        dc.write_letters()
        letter_list = [f for f in os.listdir(dc.letter_directory) if '.txt' in f]

        self.assertEqual(donation_count, len(letter_list))


if __name__ == '__main__':
    unittest.main()
 
