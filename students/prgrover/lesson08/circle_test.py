#!/usr/bin/env python3

import unittest
import math
import random
from circle import Circle

class CircleTest(unittest.TestCase):

    def test_init_radius(self):
        my_radius = 10
        c1 = Circle(10)
        self.assertEqual(my_radius, c1.radius)

    def test_diameter_getter(self):
        c1 = Circle(10)
        my_diameter = (c1.radius * 2)
        self.assertEqual(my_diameter, c1.diameter)

    def test_diameter_setter(self):
        c1 = Circle(2)
        my_diameter = 6
        c1.diameter = 6
        self.assertEqual(my_diameter, c1.diameter)
        self.assertEqual(c1.radius, (c1.diameter / 2))

    def test_area_getter(self):
        my_area = (5**2 * math.pi)
        c1 = Circle(5)
        self.assertEqual(my_area, c1.area)

    def test_str_dunder(self):
        my_string = "Circle with radius: 4.00"
        c1 = Circle(4)
        self.assertEqual(my_string, str(c1))

    def test_repr_dunder(self):
        my_string = "Circle(8)"
        c1 = Circle(8)
        self.assertEqual(my_string, repr(c1))

    def test_add_dunder(self):
        c1 = Circle(8)
        c2 = Circle(7)
        c3 = Circle(15)
        self.assertEqual(c1 + c2, c3)

    def test_mul_dunder(self):
        c1 = Circle(2)
        c2 = Circle(6)
        self.assertEqual(c1 * 3, c2)

    def test_comparison_dunder(self):
        c1 = Circle(10)
        c2 = Circle(20)
        c3 = Circle(10)
        self.assertTrue(c1 < c2)
        self.assertTrue(c2 > c1)
        self.assertTrue(c1 == c3)

    def test_sort(self):
        c1 = Circle(5)
        c2 = Circle(10)
        c3 = Circle(20)
        c4 = Circle(40)
        c5 = Circle(80)
        list1 = [c1, c2, c3, c4, c5]
        list2 = list1[:]
        random.shuffle(list2)
        self.assertFalse(list1 == list2)
        list2.sort()
        self.assertTrue(list1 == list2)



if __name__ == '__main__': 
    unittest.main()