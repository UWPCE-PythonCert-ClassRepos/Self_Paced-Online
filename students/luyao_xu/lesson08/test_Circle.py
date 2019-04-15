#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from Circle import Circle
from math import pi
import unittest

class CircleTest(unittest.TestCase):
    def test_step_1(self):
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_step_2(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)

    def test_test_3(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)
        c = Circle(1)
        self.assertEqual(c.diameter, 2)

    def test_step_4(self):
        c = Circle(2)
        self.assertEqual(c.area, 4*pi)

    def test_step_5(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius, 4)

    def test_step_6(self):
        c = Circle(4)
        self.assertEqual(repr(c), "Circle(4)")
        self.assertEqual(str(c), "Circle with radius of 4")

    def test_step_7(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = Circle(4)
        self.assertEqual(c1+c2, 6)
        self.assertEqual(c2 * 3, 12)
        self.assertEqual(c1 > c2, False)
        self.assertEqual(c1 < c2, True)
        self.assertEqual(c1 == c2, False)
        self.assertEqual(c2 == c3, True)

    def test_step_8(self):
        circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9),
                   Circle(1)]
        sorted_circles = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7),
                          Circle(8), Circle(9)]
        circles.sort()
        self.assertListEqual(circles, sorted_circles)















