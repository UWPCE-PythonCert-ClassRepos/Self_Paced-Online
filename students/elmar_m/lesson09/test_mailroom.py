#!/usr/bin/env python3

'''
file: test_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: unittests for mailroom.py class
'''


import unittest as ut
import mailroom as mr

class Mailroom_Tests(ut.TestCase):
    
    def test_Donor(self):   
        obj = mr.Donor('John', 'Doe')
        self.assertIs(obj.firstname, 'John')
        self.assertIs(obj.lastname, 'Doe')
        self.assertEqual(obj.uid, 'John_Doe')


    #def test_donation(self):
    #    obj = mr.donation(500)
    #    self.assertEqual(obj.amount, 500)
    #    self.assertEqual(obj.currency, 'dollar')
    #    #obj1 = mr.donation('a piece of land')
    #    #self.assertFalse(hasattr, obj1.amount)
    #    #self.assertFalse(hasattr, obj1.currency)
    #    #self.assertTrue(hasattr, obj1.real_value)
    
    def test_Collection(self):
        obj = mr.Collection()
        self.assertTrue(hasattr, obj.add)
        self.assertTrue(hasattr, obj.get)
        self.assertTrue(obj.add('John', '500'))
        
        




if __name__ == '__main__':
    ut.main()

