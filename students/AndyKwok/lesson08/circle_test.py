# Description: Circle Properties Tester
# Author: Andy Kwok
# Last Updated: 08/29/2018
# ChangeLog: Initialization

#!/usr/bin/env python3

import unittest
import sys
import math
import pytest
import A_Circle

class Test_A_Circle(unittest.TestCase):
    def setUp(self):
        self.radius = 2

    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys
        
    def test_area(self):
        expected = math.pi * 2 * 2
        c = A_Circle.Circle(self.radius)
        actual = c.area
        self.assertEqual(actual, expected)

    def test_from_diameter(self):
        expected = 4
        c = A_Circle.Circle(self.radius)
        actual = c.diameter
        self.assertEqual(actual, expected)
    
    def test__str__(self):
        actual = A_Circle.Circle(4)
        self.assertEqual(actual.__str__(), 'Circle with radius: 4')
    
    def test__repr__(self):
        actual = A_Circle.Circle(4)
        self.assertEqual(repr(actual), 'Circle(4)')

    def test__add__(self):
        c1 = A_Circle.Circle(1)
        c2 = A_Circle.Circle(3)
        actual = c1 + c2
        expected = A_Circle.Circle(4)
        self.assertEqual(actual, expected)
    
    def test__mul__(self):
        c1 = A_Circle.Circle(3)
        actual = c1 * 3
        expected = A_Circle.Circle(9)
        self.assertEqual(actual, expected)
        
    def test__rmul__(self):
        c1 = A_Circle.Circle(3)
        actual = 3 * c1
        expected = A_Circle.Circle(9)
        self.assertEqual(actual, expected)
    
    def test__lt__(self):
        c1 = A_Circle.Circle(1)
        c2 = A_Circle.Circle(3)    
        self.assertTrue(c1 < c2)
        
    def test__gt__(self):
        c1 = A_Circle.Circle(7)
        c2 = A_Circle.Circle(3)    
        self.assertTrue(c1 > c2)
        
    def test__eq__(self):
        c1 = A_Circle.Circle(3)
        c2 = A_Circle.Circle(3)   
        self.assertTrue(c1 == c2)
    
    def test_sort_key(self):
        actual = [A_Circle.Circle(7), A_Circle.Circle(3), A_Circle.Circle(5)]
        expected = [A_Circle.Circle(3), A_Circle.Circle(5), A_Circle.Circle(7)]
        actual.sort()
        self.assertEqual(actual, expected)
        
        
if __name__=="__main__":
    unittest.main()