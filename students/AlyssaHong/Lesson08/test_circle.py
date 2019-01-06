"""
Author: Alyssa Hong
Date: 12/18/2018
Update:
Lesson8 Assignments > Test circle.py
"""



#!/usr/bin/env python3

import unittest
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_radiusr(self):
        c = Circle(4)
        self.assertEqual(c.radius, 4)
        self.assertEqual(c.diameter, 8)

    def test_diamter(self):
        c = Circle(4)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        self.assertEqual(c.radius,1)

    def test_area(self):
        c = Circle(2)
        self.assertEqual(c.area, '12.56637')
        with self.assertRaises(AttributeError):
            c.area = 42

    def test_from_diameter(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.radius, 4)
        self.assertEqual(c.diameter, 8)

    def test_str(self):
        c = Circle(4)
        self.assertEqual(str(c), "Circle with radius: 4.0")

    def test_repr(self):
        c = Circle(4)
        self.assertEqual(repr(c), 'Circle(4)')

    def test_add(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = c1 + c2
        self.assertEqual(c3.radius, 6)

    def test_multi(self):
        c1 = Circle(2)
        c2 = Circle(4)
        with self.assertRaises(TypeError):
            c3 = c2 * 3
            del c3

    def test_comparsion(self):
        c1 = Circle(1)
        c2 = Circle(2)
        c3 = Circle(2)
        c4 = Circle(3)
        self.assertEqual(c1 < c2, True)
        self.assertEqual(c2 > c1, True)
        self.assertEqual(c2 == c3, True)
        self.assertEqual(c4 < c3, False)
        self.assertEqual(c1 != c4, True)
        self.assertEqual(c3 == c4, False)




if __name__ == "__main__":
    unittest.main()
