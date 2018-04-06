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



if __name__ == "__main__":
    unittest.main()
