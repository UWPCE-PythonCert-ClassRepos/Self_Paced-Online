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

    def test_diameter_property(self):
        c = Circle(4)
        self.assertEqual(8, c.diameter)


if __name__ == '__main__':
    unittest.main()
