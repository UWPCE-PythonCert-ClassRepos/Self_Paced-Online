#!/usr/bin/env python3
"""Lesson 08 Unit Tests for Circle CLass Assignment - """

import unittest
from math import pi
import circle


class TestCircle(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCircle, self).__init__(*args, **kwargs)
        self.t_radius = 4
        self.t_diameter = 2 * self.t_radius
        self.t_area = pi * self.t_radius**2
        self.t_perimeter = 2 * self.t_radius * pi

    def setUp(self):
        """set up test circle to be used in tests"""
        self.c = circle.Circle(self.t_radius)

    def test_radius(self):
        """test radius"""
        # self.assertTrue(self.c.radius, self.t_radius, msg=self.c.radius)
        self.assertEqual(self.c.radius, self.t_radius)
        self. assertTrue(self.c.radius == self.t_radius, msg=self.c.radius)

    def test_area(self):
        """test area"""
        self.assertEqual(self.c.area, self.t_area)

    def test_perimeter(self):
        """test perimeter"""
        self.assertEqual(self.c.perimeter, self.t_perimeter)

    def test_diameter(self):
        """test diameter"""
        self.assertEqual(self.c.diameter, self.t_diameter)

    def test_negative_radius_change(self):
        """Test the setting of a negative radius"""
        with self.assertRaises(ValueError):
            self.c.radius = -8
        self.assertEqual(self.c.radius, self.t_radius)
        self.assertEqual(self.c.diameter, self.t_diameter)
        self.assertTrue(self.c.radius == self.t_radius,
                        msg=self.c.radius)

    def test_positive_radius_change(self):
        """Test the setting of a positive radius"""
        rad = 8
        self.c.radius = rad

        self.assertTrue(self.c.radius == rad, msg=self.c.radius)
        self.assertTrue(self.c.diameter == rad * 2, msg=self.c.diameter)
        self.assertTrue(self.c.area == pi * rad**2, msg=self.c.area)
        self.assertTrue(self.c.perimeter == 2 * pi * rad, msg=self.c.perimeter)

    def test_pos_from_diameter(self):
        """testing positive entry from_diameter"""
        diameter = 8
        self.c.from_diameter(diameter)

        self.assertTrue(self.c.diameter == diameter, msg=self.c.diameter)
        self.assertTrue(self.c.radius == diameter/2, msg=self.c.radius)

    def test_neg_from_diameter(self):
        """testing negative entry from_diameter"""
        with self.assertRaises(ValueError):
            self.c.from_diameter(-8)

        self.assertTrue(self.c.diameter == self.t_diameter,
                        msg=self.c.diameter)
        self.assertTrue(self.c.radius == self.t_radius, msg=self.c.radius)

    def test_print_string(self):
        """test print string output"""
        self.assertEqual(str(self.c), f"Circle with radius: {self.c.radius}")

    def test_repr(self):
        """test repr output"""
        self.assertEqual(repr(self.c), f"Circle({self.c.radius})")

    def test_add_circle(self):
        """testing adding circles"""
        c2 = circle.Circle(5)
        c3 = self.c + c2

        new_circle = circle.Circle(c2.radius + self.c.radius)

        self.assertTrue(c3.radius == new_circle.radius,
                        msg=(c3.radius, new_circle.radius))
        self.assertTrue(c3.area == new_circle.area,
                        msg=(c3.area, new_circle.area))
        self.assertTrue(c3.diameter == new_circle.diameter,
                        msg=(c3.diameter, new_circle.diameter))

    def test_sub_circle(self):
        """testing subtracting circles"""
        c2 = circle.Circle(2)
        c3 = self.c - c2

        new_circle = circle.Circle(self.c.radius - c2.radius)

        self.assertTrue(c3.radius == new_circle.radius,
                        msg=(c3.radius, new_circle.radius))
        self.assertTrue(c3.area == new_circle.area,
                        msg=(c3.area, new_circle.area))
        self.assertTrue(c3.diameter == new_circle.diameter,
                        msg=(c3.diameter, new_circle.diameter))

    def test_multiply_circle(self):
        """testing multiplying circles"""
        c2 = circle.Circle(5)
        c3 = self.c * c2

        new_circle = circle.Circle(c2.radius * self.c.radius)

        self.assertTrue(c3.radius == new_circle.radius,
                        msg=(c3.radius, new_circle.radius))
        self.assertTrue(c3.area == new_circle.area,
                        msg=(c3.area, new_circle.area))
        self.assertTrue(c3.diameter == new_circle.diameter,
                        msg=(c3.diameter, new_circle.diameter))

    def test_rmultiply(self):
        """testing multiplying by number first followed by circle"""
        number = 3
        c2 = number * self.c
        new_circle = circle.Circle(self.c.radius * number)

        self.assertTrue(c2.radius == new_circle.radius,
                        msg=(c2.radius, new_circle.radius))
        self.assertTrue(c2.area == new_circle.area,
                        msg=(c2.area, new_circle.area))
        self.assertTrue(c2.diameter == new_circle.diameter,
                        msg=(c2.diameter, new_circle.diameter))

    def test_equalto_comparison(self):
        """testing equal to comparison"""
        circle2 = circle.Circle(self.t_radius)
        circle3 = circle.Circle(self.t_radius+1)

        self.assertTrue(self.c == circle2, msg=(self.c, circle2))
        self.assertFalse(self.c == circle3, msg=(self.c, circle3))
        with self.assertRaises(AttributeError):
            self.c == 5

    def test_greater_equal_to_comparisons(self):
        """testing greater than or equal to comparison"""
        circle2 = circle.Circle(self.t_radius)
        circle3 = circle.Circle(self.t_radius-1)
        circle4 = circle.Circle(self.t_radius+1)

        self.assertTrue(self.c >= circle2, msg=(self.c, circle2))
        self.assertTrue(self.c >= circle3, msg=(self.c, circle3))
        self.assertFalse(self.c >= circle4, msg=(self.c, circle4))
        with self.assertRaises(AttributeError):
            self.c >= 5

    def test_less_than_equal_to_comparisons(self):
        """testing less than or equal to comparison"""
        circle2 = circle.Circle(self.t_radius)
        circle3 = circle.Circle(self.t_radius-1)
        circle4 = circle.Circle(self.t_radius+1)

        self.assertTrue(self.c <= circle2, msg=(self.c, circle2))
        self.assertFalse(self.c <= circle3, msg=(self.c, circle3))
        self.assertTrue(self.c <= circle4, msg=(self.c, circle4))
        with self.assertRaises(AttributeError):
            self.c <= 5

    def test_greater_than_comparisons(self):
        """testing greater than comparison"""
        circle2 = circle.Circle(self.t_radius)
        circle3 = circle.Circle(self.t_radius-1)
        circle4 = circle.Circle(self.t_radius+1)

        self.assertFalse(self.c > circle2, msg=(self.c, circle2))
        self.assertTrue(self.c > circle3, msg=(self.c, circle3))
        self.assertFalse(self.c > circle4, msg=(self.c, circle4))
        with self.assertRaises(AttributeError):
            self.c >= 5

    def test_less_than_comparisons(self):
        """testing less than comparison"""
        circle2 = circle.Circle(self.t_radius)
        circle3 = circle.Circle(self.t_radius-1)
        circle4 = circle.Circle(self.t_radius+1)

        self.assertFalse(self.c < circle2, msg=(self.c, circle2))
        self.assertFalse(self.c < circle3, msg=(self.c, circle3))
        self.assertTrue(self.c < circle4, msg=(self.c, circle4))
        with self.assertRaises(AttributeError):
            self.c <= 5

    def test_sorted_circles(self):
        """testing sorting circles"""
        circles = [circle.Circle(6), circle.Circle(7), circle.Circle(8), circle.Circle(4), circle.Circle(
            0), circle.Circle(2), circle.Circle(3), circle.Circle(5), circle.Circle(9), circle.Circle(1)]
        circles.sort()
        self.assertEqual(circles, [circle.Circle(0), circle.Circle(1), circle.Circle(2), circle.Circle(3), circle.Circle(
            4), circle.Circle(5), circle.Circle(6), circle.Circle(7), circle.Circle(8), circle.Circle(9)])


if __name__ == '__main__':
    unittest.main()
