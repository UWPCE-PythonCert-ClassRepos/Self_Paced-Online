#!/usr/bin/env python3
"""Unit Tests for Circle"""

import unittest
import math
import random
import sys
import circle

from io import StringIO


def redirect_stdout():
    """Redirect stdout to the returned StringIO object.

    Returns:
        StringIO: Object containing redirected stdout.
    """
    redirect = StringIO()
    sys.stdout = redirect

    return redirect


def reset_stdout():
    """Reset stdout back to default"""
    sys.stdout = sys.__stdout__


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

    def test_print_circle(self):
        captured_print = redirect_stdout()
        print(self.c)
        reset_stdout()

        self.assertTrue(captured_print.getvalue() == (f'Circle with radius: '
                                                      f'{self.test_radius}\n'
                                                      f'            diameter: '
                                                      f'{self.test_diameter}\n'
                                                      f'            area: '
                                                      f'{self.test_area}\n'),
                        msg=captured_print.getvalue())

    def test_repr(self):
        test_repr = repr(self.c)

        self.assertTrue(test_repr == f'Circle({self.test_radius})',
                        msg=test_repr)

    def test_add_number_to_circle(self):
        add_radius = 5
        c2 = self.c + add_radius
        expected_circle = circle.Circle(self.test_radius + add_radius)

        self.assertTrue(c2.radius == expected_circle.radius,
                        msg=(c2.radius, expected_circle.radius))
        self.assertTrue(c2.diameter == expected_circle.diameter,
                        msg=(c2.diameter, expected_circle.diameter))
        self.assertTrue(c2.area == expected_circle.area,
                        msg=(c2.area, expected_circle.area))

    def test_radd_number_to_circle(self):
        add_radius = 5
        c2 = add_radius + self.c
        expected_circle = circle.Circle(self.test_radius + add_radius)

        self.assertTrue(c2.radius == expected_circle.radius,
                        msg=(c2.radius, expected_circle.radius))
        self.assertTrue(c2.diameter == expected_circle.diameter,
                        msg=(c2.diameter, expected_circle.diameter))
        self.assertTrue(c2.area == expected_circle.area,
                        msg=(c2.area, expected_circle.area))

    def test_add_circles(self):
        c2_radius = 5
        c2 = circle.Circle(c2_radius)
        c3 = self.c + c2
        expected_circle = circle.Circle(c2_radius + self.test_radius)

        self.assertTrue(c3.radius == expected_circle.radius,
                        msg=(c3.radius, expected_circle.radius))
        self.assertTrue(c3.diameter == expected_circle.diameter,
                        msg=(c3.diameter, expected_circle.diameter))
        self.assertTrue(c3.area == expected_circle.area,
                        msg=(c3.area, expected_circle.area))

    def test_sub_number_to_circle(self):
        sub_radius = 2
        c2 = self.c - sub_radius
        expected_circle = circle.Circle(self.test_radius - sub_radius)

        self.assertTrue(c2.radius == expected_circle.radius,
                        msg=(c2.radius, expected_circle.radius))
        self.assertTrue(c2.diameter == expected_circle.diameter,
                        msg=(c2.diameter, expected_circle.diameter))
        self.assertTrue(c2.area == expected_circle.area,
                        msg=(c2.area, expected_circle.area))

    def test_rsub_number_to_circle(self):
        sub_radius = 5
        c2 = sub_radius - self.c
        expected_circle = circle.Circle(sub_radius - self.test_radius)

        self.assertTrue(c2.radius == expected_circle.radius,
                        msg=(c2.radius, expected_circle.radius))
        self.assertTrue(c2.diameter == expected_circle.diameter,
                        msg=(c2.diameter, expected_circle.diameter))
        self.assertTrue(c2.area == expected_circle.area,
                        msg=(c2.area, expected_circle.area))

    def test_sub_circles(self):
        c2_radius = 3
        c2 = circle.Circle(c2_radius)
        c3 = self.c - c2
        expected_circle = circle.Circle(self.test_radius - c2_radius)

        self.assertTrue(c3.radius == expected_circle.radius,
                        msg=(c3.radius, expected_circle.radius))
        self.assertTrue(c3.diameter == expected_circle.diameter,
                        msg=(c3.diameter, expected_circle.diameter))
        self.assertTrue(c3.area == expected_circle.area,
                        msg=(c3.area, expected_circle.area))

    def test_sub_circles_negative(self):
        c2_radius = 5
        c2 = circle.Circle(c2_radius)

        with self.assertRaises(ValueError):
            _ = self.c - c2

    def test_mult_number_to_circle(self):
        mult_radius = 3
        c2 = self.c * mult_radius
        expected_circle = circle.Circle(self.test_radius * mult_radius)

        self.assertTrue(c2.radius == expected_circle.radius,
                        msg=(c2.radius, expected_circle.radius))
        self.assertTrue(c2.diameter == expected_circle.diameter,
                        msg=(c2.diameter, expected_circle.diameter))
        self.assertTrue(c2.area == expected_circle.area,
                        msg=(c2.area, expected_circle.area))

    def test_rmult_number_to_circle(self):
        mult_radius = 5
        c2 = mult_radius * self.c
        expected_circle = circle.Circle(self.test_radius * mult_radius)

        self.assertTrue(c2.radius == expected_circle.radius,
                        msg=(c2.radius, expected_circle.radius))
        self.assertTrue(c2.diameter == expected_circle.diameter,
                        msg=(c2.diameter, expected_circle.diameter))
        self.assertTrue(c2.area == expected_circle.area,
                        msg=(c2.area, expected_circle.area))

    def test_mult_circles(self):
        c2_radius = 5
        c2 = circle.Circle(c2_radius)
        c3 = self.c * c2
        expected_circle = circle.Circle(c2_radius * self.test_radius)

        self.assertTrue(c3.radius == expected_circle.radius,
                        msg=(c3.radius, expected_circle.radius))
        self.assertTrue(c3.diameter == expected_circle.diameter,
                        msg=(c3.diameter, expected_circle.diameter))
        self.assertTrue(c3.area == expected_circle.area,
                        msg=(c3.area, expected_circle.area))

    def test_eq_operator(self):
        c2 = circle.Circle(self.test_radius)
        c3 = circle.Circle(self.test_radius + 1)

        self.assertTrue(self.c == c2, msg=(self.c, c2))
        self.assertFalse(self.c == c3, msg=(self.c, c3))
        with self.assertRaises(AttributeError):
            self.c == 5

    def test_ge_operator(self):
        c1 = circle.Circle(self.test_radius - 1)
        c2 = circle.Circle(self.test_radius)
        c3 = circle.Circle(self.test_radius + 1)

        self.assertTrue(self.c >= c1, msg=(self.c, c1))
        self.assertTrue(self.c >= c2, msg=(self.c, c2))
        self.assertFalse(self.c >= c3, msg=(self.c, c3))
        with self.assertRaises(AttributeError):
            self.c >= 5

    def test_gt_operator(self):
        c1 = circle.Circle(self.test_radius - 1)
        c2 = circle.Circle(self.test_radius)
        c3 = circle.Circle(self.test_radius + 1)

        self.assertTrue(self.c > c1, msg=(self.c, c1))
        self.assertFalse(self.c > c2, msg=(self.c, c2))
        self.assertFalse(self.c > c3, msg=(self.c, c3))
        with self.assertRaises(AttributeError):
            self.c > 5

    def test_le_operator(self):
        c1 = circle.Circle(self.test_radius - 1)
        c2 = circle.Circle(self.test_radius)
        c3 = circle.Circle(self.test_radius + 1)

        self.assertFalse(self.c <= c1, msg=(self.c, c1))
        self.assertTrue(self.c <= c2, msg=(self.c, c2))
        self.assertTrue(self.c <= c3, msg=(self.c, c3))
        with self.assertRaises(AttributeError):
            self.c <= 5

    def test_lt_operator(self):
        c1 = circle.Circle(self.test_radius - 1)
        c2 = circle.Circle(self.test_radius)
        c3 = circle.Circle(self.test_radius + 1)

        self.assertFalse(self.c < c1, msg=(self.c, c1))
        self.assertFalse(self.c < c2, msg=(self.c, c2))
        self.assertTrue(self.c < c3, msg=(self.c, c3))
        with self.assertRaises(AttributeError):
            self.c < 5

    def test_sort_circles(self):
        circles = [circle.Circle(random.randint(0, 20)) for _ in range(10)]
        circles.sort()

        for i in range(0, len(circles) - 1):
            self.assertTrue(circles[i].radius <= circles[i + 1].radius)


if __name__ == '__main__':
    unittest.main()
