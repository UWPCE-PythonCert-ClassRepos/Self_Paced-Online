#!/usr/bin/env python3

'''
file: test_circle.py
elmar_m / 22e88@mailbox.org
Lesson08: unittests for circle class
'''

import unittest as ut
import circle as ci 

class mytests(ut.TestCase):
    
    def test_Circle(self):
        obj = ci.Circle(4)
        self.assertIsInstance(obj, ci.Circle)
        self.assertTrue(hasattr(obj, 'radius'))
        self.assertTrue(obj.radius 
        self.assertEqual(obj.radius, 4)


if __name__ == '__main__':
    ut.main()

