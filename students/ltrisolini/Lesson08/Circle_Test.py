#!/usr/bin/env python

import Circle
import unittest

class Test_Circle(unittest.TestCase):
    def test_radius(self):
        c = Circle.Circle(4)
        self.assertEqual( c.radius,4)
				
    def test_diameter(self):
        c = Circle.Circle(4)
        self.assertEqual(c.diameter,8)
				
    def test_diameter_setter(self):
        c = Circle.Circle(4)
        c.diameter = 2
        self.assertEqual(c.diameter,2)
        self.assertEqual(c.radius,1)
				
    def test_area(self):
        c = Circle.Circle(2)
        self.assertEqual (c.area,12.566370)
				
    def test_from_diameter(self):
        c = Circle.Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius,4)
				
    def test_repr(self):
        c1 = Circle.Circle(4)
        repr_c1=c1.__repr__()
        res_repr1 = "'Circle (4)'"
        self.assertEqual(repr_c1, res_repr1)
				
    def test_str(self):
        c1 = Circle.Circle(4)
        str_c1= c1.__str__()
        res_str1 = 'Circle with radius 4'
        self.assertEqual(str_c1, res_str1)
				
    def test_mul(self): 
        c2= Circle.Circle(4)
        c12 = c2*3
        expected_c = Circle.Circle(12)
        self.assertEqual(c12, expected_c)
				
    def test_rmul(self): 
        c2= Circle.Circle(4)
        c2_res = 3*c2
        expected_c = Circle.Circle(12)
        self.assertEqual(c2_res, expected_c)
				
    def test_add(self):
        c1= Circle.Circle(2)
        c2= Circle.Circle(4)
        c3= c1+c2
        expected_c = Circle.Circle(6)
        self.assertEqual(c3, expected_c)
				
    def test_iadd(self):
        c1= Circle.Circle(1)
        c1 +=1
        expected_c = Circle.Circle(2)
        self.assertEqual(c1, expected_c)
				
    def test_comparison(self):
        c1 = Circle.Circle(1)
        c2 = Circle.Circle(2)
        c1a = Circle.Circle(1)
        self.assertEqual((c1>c2),False)
        self.assertEqual((c1<c2),True)
        self.assertEqual((c1==c2),False)
        self.assertEqual((c1==c1a),True)
				
    def test_sort_key(self):
        c5 = Circle.Circle(5)
        va = 5
        self.assertEqual(c5.radius, 5)
        
if __name__=="__main__":
    unittest.main()

