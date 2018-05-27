""" unit test circle.py """

import circle as c
import unittest
import math

class test_circle(unittest.TestCase):

    # step 1
    def test_radius(self):
        test = c.Circle(5)
        self.assertEqual(test.radius, 5)

    # step 2
    def test_diameter(self):
        test = c.Circle(5)
        self.assertEqual(test.diameter, 10)


    # step 3
    def test_set_diameter(self):
        test = c.Circle(5)
        test.diameter = 20
        self.assertEqual(test.diameter, 20)
        self.assertEqual(test.radius, 10)
    
    # step 4
    def test_area(self):
        test = c.Circle(5)
        self.assertEqual(test.area, math.pi * math.pow(5, 2))
        
    # step 5
    def test_from_diameter(self):
        test = c.Circle.from_diameter(10)
        self.assertEqual(test.radius, 5)
    
    # step 6.1
    def test_str(self):
        test = c.Circle (5)
        self.assertEqual(str(test), "Circle with a radius of 5.")
        
    # step 6.2
    def test_rpr(self):
        test = c.Circle(5)
        self.assertEqual(repr(test), "Circle(5)")
    
    # step 7
    def test_add(self):
        test1 = c.Circle(2)
        test2 = c.Circle(4)
        self.assertEqual(test1 + test2, c.Circle(6))
    

    
        
if __name__ == '__main__':
    unittest.main()