#!/usr/bin/env python3

# Lesson_8 Activity 1 Testing The Circle Class

from circle import *
import unittest
import math

# make some circles
a = Circle(20)
b = Circle(3)
c = Circle()
d = Circle(10)


class TestCircle(unittest.TestCase):

    def test_radius(self):
        self.assertEqual(a.radius, 20)
        self.assertEqual(b.radius, 3)
        self.assertEqual(c.radius, 1)

    def test_diameter(self):
        self.assertEqual(a.diameter, 40)
        self.assertEqual(b.diameter, 6)
        self.assertEqual(c.diameter, 2)
        # testing circle from diameter
        d.diameter = 24
        self.assertEqual(d.diameter, 24)
        self.assertEqual(d.radius, 12)

    def test_area(self):
        self.assertEqual(c.area, c.radius ** 2 * math.pi)
        # test that area is read only
        with self.assertRaises(AttributeError):
            c.area = 42

    def test_circumference(self):
        self.assertEqual(c.circumference, 2 * math.pi * c.radius)
        # test that area is read only
        with self.assertRaises(AttributeError):
            c.circumference = 42

    def test_str(self):
        self.assertEqual(str(c), f'Circle with radius: {str(c.radius)}')

    def test_repr(self):
        self.assertEqual(repr(c), f'Circle({str(c.radius)})')

    def test_operators(self):
        self.assertTrue(a > b)
        self.assertTrue(b < a)
        self.assertTrue(a == Circle(20))
        self.assertTrue(b == b)
        self.assertTrue(a != b)
        self.assertTrue(a >= b)
        self.assertTrue(b <= a)
        self.assertTrue(a + b == Circle(23))
        self.assertTrue(a - b == Circle(17))
        self.assertTrue(a * b == Circle(60))
        self.assertTrue(a / b == Circle(20/3))
        # reverse
        self.assertTrue(b * a == Circle(60))
        self.assertTrue(b / a == Circle(3/20))
        self.assertTrue(b + a == Circle(23))
        # what on earth is a negative radius?
        # should i just throw an error for a negtive radius?
        self.assertTrue(b - a == Circle(-17))
        # scalars
        self.assertTrue(a * 4 == Circle(80))
        self.assertTrue(a / 4 == Circle(5))

        # += and *= combine test circles
        testa = Circle(10)
        testb = Circle(5)
        testc = Circle(2)
        testa += testb
        testb *= testc
        testc *= 4
        self.assertTrue(testa == Circle(15))
        self.assertTrue(testb == Circle(10))
        self.assertTrue(testc == Circle(8))

    def test_sorting(self):
        circles = [a, b, c, d]  # note d was changed in 'test_diameter'
        sorted_circles = sorted(circles)
        self.assertTrue(sorted_circles == [c, b, d, a])
