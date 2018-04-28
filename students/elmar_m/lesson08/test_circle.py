#!/usr/bin/env python3

'''
file: test_circle.py
elmar_m / 22e88@mailbox.org
Lesson08: unittests for circle class
'''

import unittest as ut
import circle as ci 

class mytests(ut.TestCase):
    
    def test_Circle_basic(self):
        '''
        Tests the following:
        - possibility to create an object from class ci.Circle
        - if the resulting object has an attribute 'radius'
        - is the value of 'radius' according to the argument given at initialization
        TODO:
        - test if initialization with something else than a numerical value (int, float)
          raises an exception
        '''
        obj = ci.Circle(4)
        self.assertIsInstance(obj, ci.Circle)
        self.assertTrue(hasattr(obj, 'radius'))
        self.assertEqual(obj.radius, 4)

        # obj = ci.Circle('abc')
        


if __name__ == '__main__':
    ut.main()

