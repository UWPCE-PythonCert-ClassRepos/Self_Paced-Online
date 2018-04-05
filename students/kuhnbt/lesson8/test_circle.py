import unittest
import circle_class as cc
import numpy as np


class CircleTest(unittest.TestCase):
    def setUp(self):
        self.c = cc.Circle(4)

    def test_radius(self):
        self.assertEqual(self.c.radius, 4)
        with self.assertRaises(ValueError):
            f = cc.Circle(-2)

    def test_diameter(self):
        self.assertEqual(self.c.diameter, 8)
        self.c.diameter = 3
        self.assertEqual(self.c.radius, 1.5)
        self.c.radius = 5
        self.assertEqual(self.c.diameter, 10)

    def test_area(self):
        self.assertEqual(self.c.area, 16*np.pi)
        with self.assertRaises(AttributeError):
            self.c.area = 10

    def test_from_diameter(self):
        g = cc.Circle.from_diameter(4)
        self.assertEqual(g.radius, 2)
        self.assertEqual(g.diameter, 4)

    def test_print(self):
        self.assertEqual(str(self.c), "A Circle with radius 4.00")

    def test_repr(self):
        self.assertEqual(repr(self.c), "Circle (4)")

    def test_addition(self):
        d = self.c + cc.Circle(5)
        self.assertEqual(d, cc.Circle(9))

    def test_multiplication(self):
        f = self.c*4
        g = 5*self.c
        self.assertEqual(f, cc.Circle(16))
        self.assertEqual(g, cc.Circle(20))

    def test_comparison(self):
        h = cc.Circle(9)
        self.assertGreater(h, self.c)
        self.assertLess(self.c, h)

    def test_equality(self):
        self.assertEqual(self.c, cc.Circle(4))

    def test_sort(self):
        b = [cc.Circle(5), cc.Circle(8), cc.Circle(2), cc.Circle(6)]
        b.sort()
        self.assertEqual(b, [cc.Circle(2), cc.Circle(5), cc.Circle(6),
                             cc.Circle(8)])

    def test_augmented(self):
        self.c += cc.Circle(3)
        self.assertEqual(self.c, cc.Circle(7))
        self.c -= cc.Circle(2)
        self.assertEqual(self.c, cc.Circle(5))
        self.c *= 3
        self.assertEqual(self.c, cc.Circle(15))
        self.c /= 4
        self.assertEqual(self.c, cc.Circle(15/4))

    def test_power(self):
        r = self.c**3
        self.assertEqual(r, cc.Circle(64))
