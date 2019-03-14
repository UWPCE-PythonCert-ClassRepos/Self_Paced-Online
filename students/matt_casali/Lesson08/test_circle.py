#!/usr/bin/env python3

import unittest
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_radious(self):
        test = Circle(4)
        self.assertEqual(test.radius, 4)

    def test_diameter(self):
        test = Circle(4)
        self.assertEqual(test.diameter, 8)

    def test_area(self):
        test = Circle(4)
        self.assertEqual(test.area, "50.27")

    def test_from_diameter(self):
        test = Circle.from_diameter(8)
        self.assertEqual(str(test), "Circle with radius: 4.0")

    def test_str(self):
        test = Circle(4)
        self.assertEqual(str(test), "Circle with radius: 4")

    def test_repr(self):
        test = repr(Circle(4))
        self.assertEqual(test, "Circle(4)")

    def test_add(self):
        c1 = Circle(4)
        c2 = Circle(2)
        c3 = c1 + c2
        self.assertEqual(c3.radius, 6)

    def test_multiply(self):
        c1 = Circle(4)
        c2 = c1 * 2
        self.assertEqual(c2.radius, 8)

    def test_equal(self):
        c1 = Circle(4)
        c2 = Circle(4)
        self.assertEqual(c1 == c2, True)

    def test_not_equal(self):
        c1 = Circle(4)
        c2 = Circle(8)
        self.assertEqual(c1 != c2, True)

    def test_less_than(self):
        c1 = Circle(4)
        c2 = Circle(8)
        self.assertEqual(c1 < c2, True)

    def test_greater_than(self):
        c1 = Circle(8)
        c2 = Circle(4)
        self.assertEqual(c1 > c2, True)


if __name__ == "__main__":
    unittest.main()

