#!/usr/bin/env python

import math
import unittest

import circle as c


class CircleTests(unittest.TestCase):

    def test_instance_attributes(self):
        o = c.Circle(5)
        self.assertEqual(o.radius, 5)
        self.assertEqual(o.diameter, 10)

    def test_setting_diameter(self):
        o = c.Circle(5)
        o.diameter = 20
        self.assertEqual(o.diameter, 20)
        self.assertEqual(o.radius, 10)

    def test_area(self):
        o = c.Circle(5)
        self.assertEqual(o.area, math.pi * 5**2)
        with self.assertRaises(AttributeError):
            o.area = 42

    def test_alternate_constructor(self):
        o = c.Circle.from_diameter(20)
        self.assertEqual(o.diameter, 20)
        self.assertEqual(o.radius, 10)
        self.assertEqual(o.area, math.pi * 10**2)
    
    def test_repr_and_str(self):
        o = c.Circle(5)
        self.assertEqual(str(o), 'Circle with radius: 5')
        self.assertEqual(repr(o), 'Circle(5)')

    def test_add(self):
        o1 = c.Circle(5)
        o2 = c.Circle(10)
        o3 = o1 + o2
        self.assertEqual(repr(o1 + o2), repr(o3))
        self.assertEqual(o3.radius, 15)

    def test_multiply(self):
        o1 = c.Circle(5)
        o2 = o1 * 3
        o3 = 3 * o2
        self.assertEqual(o2.radius, 15)
        self.assertEqual(o3.radius, 45)

    def test_operator(self):
        o1 = c.Circle(5)
        o2 = o1 * 3
        self.assertLess(o1, o2)
        self.assertLessEqual(o1, o2)
        self.assertGreater(o2, o1)
        self.assertGreaterEqual(o2, o1)
        self.assertNotEqual(o1, o2)
        o1 = o2
        self.assertEqual(o1, o2)

    def test_sort_circles(self):
        cirs = [c.Circle(6),
                c.Circle(7),
                c.Circle(8),
                c.Circle(4),
                c.Circle(0),
                c.Circle(2),
                c.Circle(3),
                c.Circle(5),
                c.Circle(9),
                c.Circle(1)
                ]
        cirs.sort()
        self.assertEqual(cirs[0], c.Circle(0))
        self.assertEqual(cirs[-1], c.Circle(9))


if __name__ == "__main__":
    unittest.main()
