#!/usr/bin/env python3
import unittest
from Circle import Circle


class circle_tests(unittest.TestCase):

    # Initial setup of test values
    # def setUp(self):

    # Step 1 test - radius assignment
    def test_radius(self):
        c = Circle(5)
        self.assertEqual(5, c.radius)

    # Step 2 test - get circle diameter
    def test_diameter_property(self):
        c = Circle(4)
        self.assertEqual(8, c.diameter)

    # Step 3 test - set diameter property
    def test_diameter_set(self):
        c = Circle(4)
        c.diameter = 2
        self.assertEqual(1, c.radius)

    # Step 4 test - get area property
    def test_area_set(self):
        c = Circle(2)
        self.assertEqual(12.566370, c.area)

    # Step 5 test - test alternate constructor
    def test_alt_const(self):
        c = Circle.from_diameter(8)
        self.assertEqual(4.0, c.radius)
        self.assertEqual(8.0, c.diameter)

    # Step 6 test - test str property
    def test_str(self):
        c = Circle(4)
        test_str = "Circle with radius: 4.000000"
        self.assertEqual(test_str, str(c))

    # Step 6 test - test repr property
    def test_repr(self):
        c = Circle(4)
        test_str = 'Circle(4)'
        self.assertEqual(test_str, repr(c))

    # Step 7 test - test adding two circles
    def test_add(self):
        c1 = Circle(2)
        c2 = Circle(4)
        result = 'Circle(6)'
        self.assertEqual(result, repr(c1 + c2))

    # Step 7 test - test multiply two circles
    def test_multiply(self):
        c = Circle(2)
        self.assertEqual('Circle(8)', repr(c * 4))
        self.assertEqual('Circle(6)', repr(3 * c))

if __name__ == '__main__':
    unittest.main()
