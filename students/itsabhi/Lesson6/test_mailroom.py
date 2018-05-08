import mailroom4v1
import unittest
from unittest.mock import patch
import os


class DonationsTestCases(unittest.TestCase):

    def setUp(self):
    #Invoked before each test method
        self.test_donors_dict = {
        'A G': [10, 20, 30],
        'N D': [40, 50]
    }
    def test_list_donors(self):
    #Test donor list when the option "list" is selected under the Sending Thanks menu
        result = mailroom4v1.list_of_donors(self.test_donors_dict)
        self.assertEqual(list(self.test_donors_dict.keys()), result)  # Convert to list and assert against result

    @patch('mailroom4v1.input', side_effect = ['PJ Mask', 200])
    def test_sending_thanks_add_donor(self, test_donors_dict):
    #Test dictionary update for a new donor
        mailroom4v1.sending_thanksv2(self.test_donors_dict)
        self.assertDictEqual(self.test_donors_dict, {'A G': [10, 20, 30], 'N D': [40, 50], 'PJ Mask': [200]})

    @patch('mailroom4v1.input', side_effect = ['N D', 60])
    def test_sending_thanks_existing_donor(self, test_donors_dict):
    #Test dictionary update for an existing donor
        mailroom4v1.sending_thanksv2(self.test_donors_dict)
        self.assertDictEqual(self.test_donors_dict, {'A G': [10, 20, 30], 'N D': [40, 50, 60]})

    def test_create_report(self):
    #Test donor summary is created for test object
        result = mailroom4v1.create_donor_summary_list(self.test_donors_dict)
        self.test_donors_summary_list = [['N D', 90, 2, 45], ['A G', 60, 3, 20]]
        self.assertListEqual(self.test_donors_summary_list, result)

    def test_sending_letters(self):
    #Test files are created in current working directory
        mailroom4v1.sending_letters(self.test_donors_dict)
        self.assertIn('A G.txt', os.listdir())
        self.assertIn('N D.txt', os.listdir())

if __name__ == '__main__':
    unittest.main()
