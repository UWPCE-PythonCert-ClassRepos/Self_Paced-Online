#!/usr/bin/env python3

import unittest
import math
import circle


class TestCircle(unittest.TestCase):
    """Test class containing all unit tests for Circle"""
    def __init__(self, *args, **kwargs):
        super(TestCircle, self).__init__(*args, **kwargs)
        self.test_radius = 5
        self.test_diameter = 2 * self.test_radius
        self.test_area = math.pi * self.test_radius**2

    def setUp(self):
        self.c = circle.Circle(self.test_radius)

    def test_get_diameter(self):
        self.assertTrue(self.c.diameter == self.test_diameter)

    def test_get_area(self):
        self.assertTrue(self.c.area == self.test_area)

    def test_set_radius_negative(self):
        with self.assertRaises(ValueError):
            self.c.radius = -5
        self.assertTrue(self.c.radius == self.test_radius)
        self.assertTrue(self.c.diameter == self.test_diameter)

    def test_diameter_negative(self):
        with self.assertRaises(ValueError):
            self.c.diameter = -5
        self.assertTrue(self.c.radius == self.test_radius)
        self.assertTrue(self.c.diameter == self.test_diameter)

    def test_construct_from_diameter(self):
        diameter = 15
        self.c = circle.Circle.from_diameter(diameter)
        self.assertTrue(self.c.diameter == diameter)

    def test_add_circle(self):
        """ ValueError because is restricted at Circle objects"""
        with self.assertRaises(ValueError):
            add_radius = 5
            c2 = self.c + add_radius
            expected_circle = circle.Circle(self.c.radius + add_radius)
            self.assertTrue(c2.radius == expected_circle.radius)

    def test_mult_number_to_circle(self):
        mult_radius = 3
        c2 = self.c * mult_radius
        expected_circle = circle.Circle(self.test_radius * mult_radius)
        self.assertTrue(c2.radius == expected_circle.radius)

    def test_eq_operator(self):
        c2 = circle.Circle(self.test_radius)
        self.assertTrue(self.c == c2)

    def test_lt_operator(self):
        c1 = circle.Circle(self.test_radius - 1)
        c2 = circle.Circle(self.test_radius)
        self.assertTrue(c1 < c2)

    def test_sorted_circles(self):
        circles = [circle.Circle(7), circle.Circle(6), circle.Circle(8),
                   circle.Circle(1), circle.Circle(0), circle.Circle(2),
                   circle.Circle(3), circle.Circle(5), circle.Circle(4),
                   circle.Circle(9)]
        circles.sort()
        self.assertEqual(circles, [circle.Circle(0), circle.Circle(1),
                         circle.Circle(2), circle.Circle(3), circle.Circle(4),
                         circle.Circle(5), circle.Circle(6), circle.Circle(7),
                         circle.Circle(8), circle.Circle(9)])


if __name__ == '__main__':
    unittest.main()
