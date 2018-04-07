#!/usr/bin/env python3
"""Unit Tests for Circle"""

import unittest
import math
import circle


class TestCircle(unittest.TestCase):
    """Test class containing all unit tests for Circle"""
    def __init__(self, *args, **kwargs):
        super(TestCircle, self).__init__(*args, **kwargs)
        self.test_radius = 4
        self.test_diameter = 2 * self.test_radius

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

    def test_radius_property_positive(self):
        new_radius = 3
        self.c.radius = new_radius

        self.assertTrue(self.c.radius == new_radius,
                        msg=self.c.radius)
        self.assertTrue(self.c.diameter == 2 * new_radius,
                        msg=self.c.diameter)

    def test_diameter_property_positive(self):
        new_diameter = 5
        self.c.diameter = new_diameter

        self.assertTrue(self.c.diameter == new_diameter,
                        msg=self.c.diameter)
        self.assertTrue(self.c.radius == new_diameter / 2,
                        msg=self.c.radius)

    def test_radius_property_negative(self):
        with self.assertRaises(ValueError):
            self.c.radius = -4

        self.assertTrue(self.c.radius == self.test_radius,
                        msg=self.c.radius)
        self.assertTrue(self.c.diameter == self.test_diameter,
                        msg=self.c.diameter)

    def test_diameter_property_negative(self):
        with self.assertRaises(ValueError):
            self.c.diameter = -4

        self.assertTrue(self.c.radius == self.test_radius,
                        msg=self.c.radius)
        self.assertTrue(self.c.diameter == self.test_diameter,
                        msg=self.c.diameter)

    def test_radius_property_zero(self):
        self.c.radius = 0

        self.assertTrue(self.c.radius == 0,
                        msg=self.c.radius)
        self.assertTrue(self.c.diameter == 0,
                        msg=self.c.diameter)

    def test_diameter_property_zero(self):
        self.c.diameter = 0

        self.assertTrue(self.c.radius == 0,
                        msg=self.c.radius)
        self.assertTrue(self.c.diameter == 0,
                        msg=self.c.diameter)


if __name__ == '__main__':
    unittest.main()
