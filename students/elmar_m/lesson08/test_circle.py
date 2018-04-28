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
        - if initialization with something else than a numerical value (int, float,
          complex) raises a TypeError exception
        '''
        obj = ci.Circle(4)
        self.assertIsInstance(obj, ci.Circle)
        self.assertTrue(hasattr(obj, 'radius'))
        self.assertRaises(TypeError, ci.Circle, 'abc')
        self.assertTrue(hasattr(obj, 'diameter'))
        self.assertTrue(hasattr(obj, 'area'))
        
    
    def test_Circle_calculate(self):
        obj = ci.Circle(4)
        self.assertEqual(obj.radius, 4)
        self.assertEqual(obj.diameter, 8)
        self.assertEqual(obj.area, 50.26548245743669)
        


if __name__ == '__main__':
    ut.main()

