"""
Author: Alyssa Hong
Date: 11/21/2018
Update:
Lesson6 Assignments > Add a full suite of unit tests.
"""

#!/usr/bin/env python3

import os
import unittest
import mailroom_part4
from mailroom_part4 import list_donation, send_thanks, send_letters, letter_content, create_report


class TestMailroom(unittest.TestCase):
    def test_donors_name(self):
        self.assertEqual(['Fred', 'Alex', 'Henry', 'Alyssa', 'Leo'], list(list_donation))

    def test_letter_content(self):
        donor_name = 'Fred'
        donation = [7000,4500]
        expected = letter_content(donor_name, donation)
        assert expected == 'Dear {},'.format(donor_name) + '\n'*2 + '\t'*1 + 'Thank you for your donation of ${:.2f}.'.format(sum(donation))+'\n' + '\t'*1 + 'It will be put to very good use.\n'+'\t'*5 +'Sincerely,\n' + '\t'*5 +'-The Team'


    def test_send_letters(self):
        mailroom_part4.send_letters()
        assert os.path.isfile('Fred.txt')
        assert os.path.isfile('Alex.txt')
        assert os.path.isfile('Henry.txt')
        assert os.path.isfile('Alyssa.txt')
        assert os.path.isfile('Leo.txt')

    def test_creat_report(self):
        expected = {'Fred':[7000,4500],'Alex':[30000,30000,10000],\
                    'Henry':[5000],'Alyssa':[120000,30000,40000],\
                    'Leo':[107000,53500]}
        mailroom_part4.create_report(expected)
        test_list_donation = mailroom_part4.list_donation
        self.assertEqual(expected, test_list_donation)


if __name__ == '__main__':
    unittest.main()
