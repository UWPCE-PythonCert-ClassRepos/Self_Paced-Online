#!/usr/bin/env python3
"""Unit Tests for Circle"""

import unittest
import math
import random
import circle


class TestCircle(unittest.TestCase):
    """Test class containing all unit tests for Circle"""
    def __init__(self, *args, **kwargs):
        super(TestCircle, self).__init__(*args, **kwargs)
        self.test_radius = 4
        self.test_diameter = 2 * self.test_radius
        self.test_area = math.pi * self.test_radius**2

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

    def test_get_area(self):
        self.assertTrue(self.c.area == self.test_area,
                        msg=self.c.area)

    def test_set_radius_positive(self):
        new_radius = 3
        self.c.radius = new_radius

        self.assertTrue(self.c.radius == new_radius,
                        msg=self.c.radius)
        self.assertTrue(self.c.diameter == 2 * new_radius,
                        msg=self.c.diameter)
        self.assertTrue(self.c.area == math.pi * new_radius**2,
                        msg=(self.c.area, math.pi * new_radius**2))

    def test_set_radius_negative(self):
        with self.assertRaises(ValueError):
            self.c.radius = -4

        self.assertTrue(self.c.radius == self.test_radius,
                        msg=self.c.radius)
        self.assertTrue(self.c.diameter == self.test_diameter,
                        msg=self.c.diameter)

    def test_set_radius_zero(self):
        self.c.radius = 0

        self.assertTrue(self.c.radius == 0,
                        msg=self.c.radius)
        self.assertTrue(self.c.diameter == 0,
                        msg=self.c.diameter)

    def test_set_diameter_positive(self):
        new_diameter = 5
        self.c.diameter = new_diameter

        self.assertTrue(self.c.diameter == new_diameter,
                        msg=self.c.diameter)
        self.assertTrue(self.c.radius == new_diameter / 2,
                        msg=self.c.radius)
        self.assertTrue(self.c.area == math.pi * (new_diameter / 2)**2,
                        msg=(self.c.area, math.pi * (new_diameter / 2)**2))

    def test_set_diameter_negative(self):
        with self.assertRaises(ValueError):
            self.c.diameter = -4

        self.assertTrue(self.c.radius == self.test_radius,
                        msg=self.c.radius)
        self.assertTrue(self.c.diameter == self.test_diameter,
                        msg=self.c.diameter)

    def test_set_diameter_zero(self):
        self.c.diameter = 0

        self.assertTrue(self.c.radius == 0,
                        msg=self.c.radius)
        self.assertTrue(self.c.diameter == 0,
                        msg=self.c.diameter)

    def test_set_area(self):
        with self.assertRaises(AttributeError):
            self.c.area = random.randint(-100, 100)

    def test_construct_from_diameter(self):
        diameter = 7
        self.c = circle.Circle.from_diameter(diameter)

        self.assertTrue(self.c.diameter == diameter,
                        msg=self.c.diameter)
        self.assertTrue(self.c.radius == diameter / 2,
                        msg=self.c.radius)
        self.assertTrue(self.c.area == math.pi * (diameter / 2)**2,
                        msg=(self.c.area, math.pi * (diameter / 2)**2))


if __name__ == '__main__':
    unittest.main()
