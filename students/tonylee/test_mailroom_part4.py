import unittest
import os.path

from mailroom_part4 import donation_history, thank_you_message, send_letter

class TestMailroomPart4(unittest.TestCase):
    def test_all_donor_names(self):
        self.assertEqual(['Tony Lee', 'Michelle Cao', 'Andy Arko', 'Tom Ludwinski'], list(donation_history.keys()))

    def test_thankyou_message(self):
        message = thank_you_message('Tony Lee')
        self.assertEqual('Thank you Tony Lee for your donation of 100.0', message)

    def test_send_letter(self):
        send_letter()
        assert os.path.isfile("Tony Lee.txt")
        assert os.path.isfile("Michelle Cao.txt")
        assert os.path.isfile("Andy Arko.txt")
        assert os.path.isfile("Tom Ludwinski.txt")

if __name__ == '__main__':
    unittest.main()
