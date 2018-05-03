#!/usr/bin/env python3

'''
file: test_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: unittests for mailroom.py class
'''


import unittest as ut
import mailroom as mr

class mailroom_tests(ut.TestCase):
    
    # 
    def test_donor(self):   
        obj = mr.donor('John', 'Doe')
        self.assertIs(obj.firstname, 'John')
        self.assertIs(obj.lastname, 'Doe')
        self.assertEqual(obj.uid, 'John_Doe')


    def test_donation(self):
        #obj = mr.donation(250)
        #self.assertEqual(obj.amount, 250)
        obj = mr.donation(500, 'dollar')
        self.assertEqual(obj.amount, 500)
        self.assertEqual(obj.currency, 'dollar')




if __name__ == '__main__':
    ut.main()

