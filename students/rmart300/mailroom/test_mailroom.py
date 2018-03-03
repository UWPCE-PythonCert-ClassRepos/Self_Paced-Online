import mailroom
import unittest, sys


class test_mailroom(unittest.TestCase):

    def test_is_number(self):
        assert mailroom.is_number('a') == False
        assert mailroom.is_number(90) == True

    bad_name = 'Wolf'
    bad_amount = 'not a number'
    good_name = 'Wolf Man'
    good_amount = '900'

    def test_validate_and_create_thank_you_bad_name(self):
        output = mailroom.validate_and_create_thank_you(self.bad_name, self.good_amount)
        assert output == 'Could not send thank you.  The first and last name of donor must be provided\n'
 
    def test_validate_and_create_thank_you_bad_amount(self):
        output = mailroom.validate_and_create_thank_you(self.good_name, self.bad_amount)
        assert output == f"invalid donation amount: {self.bad_amount}"

    def test_validate_and_create_thank_you_good_values(self):
        output = mailroom.validate_and_create_thank_you(self.good_name, self.good_amount)
        assert output == f"Hi {self.good_name}\nThank you for your donation of {self.good_amount} to the mailroom!\n"


if __name__ == '__main__':
    unittest.main()
 
