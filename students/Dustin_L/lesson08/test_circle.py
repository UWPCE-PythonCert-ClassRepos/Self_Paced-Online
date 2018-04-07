#!/usr/bin/env python3
"""Unit Tests for Circle"""

import unittest
import circle


class TestCircle(unittest.TestCase):
    """Test class containing all unit tests for Circle"""
    test_radius = 4
    test_diameter = 2 * test_radius

    def setUp(self):
        self.c = circle.Circle(self.test_radius)

    def tearDown(self):
        pass

    def test_get_radius(self):
        self.assertTrue(self.c.radius == self.test_radius,
                        msg=self.c.radius)

    def test_get_diameter(self):
        self.assertTrue(self.c.diameter == self.test_diameter,
                        msg=self.c.diameter)


if __name__ == '__main__':
    unittest.main()
