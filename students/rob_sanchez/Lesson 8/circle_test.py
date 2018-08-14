#!/usr/bin/env python3
import unittest
from Circle import Circle


class circle_tests(unittest.TestCase):

    # Initial setup of test values
    # def setUp(self):

    # Test step 1 - radius assignment
    def test_radius(self):
        c = Circle(5)
        self.assertEqual(5, c.radius)

    # Test step 2 - get circle diameter
    def test_diameter_property(self):
        c = Circle(4)
        self.assertEqual(8, c.diameter)

    # Test step 3 - set diameter property
    def test_diameter_set(self):
        c = Circle(4)
        c.diameter = 2
        self.assertEqual(1, c.radius)

    # Test step 4 - get area property
    def test_area_set(self):
        c = Circle(2)
        self.assertEqual(12.566370, c.area)

    def test_str(self):
        c = Circle(4)
        test_str = "Circle with radius: 4.000000"
        self.assertEqual(test_str, str(c))

    def test_repr(self):
        c = Circle(4)
        test_str = 'Circle(4)'
        self.assertEqual(test_str, repr(c))


if __name__ == '__main__':
    unittest.main()
