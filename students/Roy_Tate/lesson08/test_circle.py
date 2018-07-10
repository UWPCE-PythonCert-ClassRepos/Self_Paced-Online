#!/usr/bin/python3

## Student/Author:  Roy Tate (githubtater)


import unittest
import circle
import math


class CircleTest(unittest.TestCase):

    def setUp(self):
        self.radius = 5

    def test_radius_returns_correct_value(self):
        c = circle.Circle(self.radius)
        self.assertEqual(c.radius, self.radius)

    def test_diameter_calculates_properly(self):
        c = circle.Circle(self.radius)
        self.assertEqual(c.diameter, self.radius * 2)

    def test_diameter_can_be_modified_and_radius_is_updated_correctly(self):
        # Create an initial circle with radius 10
        c = circle.Circle(10)
        self.assertEqual(c.radius, c.diameter / 2)
        c.diameter = 50
        self.assertEqual(c.diameter, c.radius * 2)
        self.assertEqual(c.radius, c.diameter / 2)

    def test_area_of_circle_calculated_properly(self):
        c = circle.Circle(self.radius)
        self.assertEqual(c.area, self.radius ** 2 * math.pi)

    def test_circle_created_by_invoking_diameter(self):
        c = circle.Circle.from_diameter(10)
        self.assertEqual(c.diameter, 10)


    def test_add_circles(self):
        c1 = circle.Circle(10)
        c2 = circle.Circle(12)
        c3 = c1 + c2
        self.assertEqual(c3.radius, (c1.radius + c2.radius))

    def test_multiply_circles(self):
        multiplier = 3
        c1 = circle.Circle(10)
        c2 = c1 * multiplier
        # c3 = multiplier * c1
        self.assertEqual(c2.radius, c1.radius*multiplier)

    def test_lt_(self):
        c1 = circle.Circle(10)
        c2 = circle.Circle(20)
        self.assertLess(c1.radius, c2.radius)

    def test_le_(self):
        c1 = circle.Circle(10)
        c2 = circle.Circle(20)
        self.assertLess(c1.radius, c2.radius)
        c1 *= 2
        self.assertLessEqual(c1.radius, c2.radius)

    def test_gt_(self):
        c1 = circle.Circle(10)
        c2 = circle.Circle(20)
        self.assertGreater(c2.radius, c1.radius)

    def test_eq__(self):
        c1 = circle.Circle(10)
        c2 = circle.Circle(10)
        self.assertEqual(c1.radius, c2.radius)

    def test_ge_(self):
        c1 = circle.Circle(10)
        c2 = circle.Circle(20)
        self.assertGreaterEqual(c2.radius, c1.radius)

    def test_ne_(self):
        c1 = circle.Circle(10)
        c2 = circle.Circle(20)
        self.assertNotEqual(c1.radius, c2.radius)

    def test_circle_sort(self):
        a = circle.Circle(10)
        b = circle.Circle(22)
        c = circle.Circle(15)
        circles = [a, b, c]
        circles.sort(key=circle.Circle.sort_key)
        self.assertEqual(circles, [a, c, b])

if __name__ == "__main__":
    unittest.main()