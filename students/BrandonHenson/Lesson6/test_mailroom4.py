# Brandon Henson
# 4/27/18
# Lesson 06 mailroom_4.py
# Testing

import unittest
import Mailroom_4
import os

class MailroomTest(unittest.TestCase):

    def setUp(self):
        Mailroom_4.donor_history = {'Brandon Henson': [1005.49, 3116.72, 5200]}
    def test_donor_history(self):
        self.assertEqual(Mailroom_4.donor_history,{'Brandon Henson': [1005.49, 3116.72, 5200]})
        Mailroom_4.donor_history['test']=45
        self.assertEqual(Mailroom_4.donor_history,{'Brandon Henson': [1005.49, 3116.72, 5200], 'test': 45})

    def test_menu_1(self):
        self.assertEqual(Mailroom_4.names(),['Brandon Henson'])
        Mailroom_4.donor_history ['Brandon Henson'] = 61.90
        self.assertEqual(Mailroom_4.donor_history,{'Brandon Henson': 61.90})


    def test_report(self):
        report = Mailroom_4.menu_2()


    def test_email_all(self):
        Mailroom_4.email_all()
        assert os.path.isfile('Brandon Henson.txt')

if __name__ == '__main__':
    unittest.main()