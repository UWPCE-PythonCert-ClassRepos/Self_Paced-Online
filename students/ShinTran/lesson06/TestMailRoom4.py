'''
Shin Tran
Python 210
Lesson 6 Assignment
'''

import unittest
import mailroom4
from io import StringIO

class TestMailRoom4(unittest.TestCase):

    # User types 'list' as the input, so the dictionary/list of names is unmodified
    def test_donor_list(self):
        name_list = ['Jennifer Miller','William Rodriguez','Patricia Brown']
        self.assertEqual(mailroom4.generate_name_list(), name_list)

    # User enters "John Smith" and a donation of $67,890, method outputs a string email
    def test_email_text(self):
        list1 = ['John Smith', 67890]
        message_string = "Dear {:s},\n\
        Thank you for the generous donation of ${:,.2f}.\n\
        Sincerely,\n\
        Your Local Charity".format(*list1)
        self.assertEqual(mailroom4.get_email_text(list1), message_string)

    # Compares the report that gets generate based on the preloaded donor list
    def test_print_report(self):
        s1 = "Donor Name          |   Total Given  |  Num Gifts |  Average Gift\n\
-----------------------------------------------------------------\n\
William Rodriguez    $   161,585.16             3  $    53,861.72\n\
Jennifer Miller      $   145,076.19             2  $    72,538.10\n\
Patricia Brown       $   100,863.96             2  $    50,431.98\n\
"
        self.assertEqual(mailroom4.generate_report(), s1)

    # Compares the thank you letter (txt file) output with the preloaded donor list
    def test_file_output(self):
        donor_list = [["Jennifer Miller",145076.19],["William Rodriguez", 161585.16],["Patricia Brown",100863.96]]
        message = "Dear {:s},\n\
    Thank you for donating ${:,.2f}.\n\
    Sincerely,\n\
    Your Local Charity"
        comp_dict = {}
        for item in donor_list:
            comp_dict[item[0]] = message.format(*item)
        for k, v in comp_dict.items():
            with open (k+".txt", 'r') as f:
                contents = f.read()
                self.assertEqual(contents, v)

# Main method so the program would run
if __name__ == '__main__':
    unittest.main()
