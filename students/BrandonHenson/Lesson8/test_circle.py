# Brandon Henson
# 5\11\18
# Lesson 8
# Circles Test

import unittest
import circle
from circle import Circle
import math


class TestCircle(unittest.TestCase):

    def test_get_radius_and_diameter(self):
        test_circle = Circle(4)
        self.assertEqual(test_circle.radius, 4)
        self.assertEqual(test_circle.diameter, 8)

    def test_set_radius_and_diameter(self):
        test_circle = Circle(6)
        test_circle.radius = 100
        self.assertEqual(test_circle.radius, 100)
        self.assertEqual(test_circle.diameter, 200)

    def test_area(self):
        test_circle = Circle(5)
        self.assertEqual(test_circle.area, 78.53981633974483)

    def test_circle_from_diameter(self):
        test_circle = Circle.circle_from_diameter(20)
        self.assertEqual(test_circle.radius, 10)
        self.assertEqual(test_circle.area, 314.1592653589793)

    def test_str(self):
        test_circle = Circle(8)
        self.assertEqual(str(test_circle), "Circle with Radius: 8")

    def test_add(self):
        test_circle1 = Circle(6)
        test_circle2 = Circle(4)
        self.assertEqual(test_circle1 + test_circle2, str('Circle(10)'))

    def test_mul(self):
        test_circle1 = Circle(6)
        test_number = 4
        self.assertEqual(test_circle1 * test_number, str('Circle(24)'))

    def test_less_than(self):
        test_circle1 = Circle(20)
        test_circle2 = Circle(21)
        self.assertTrue(test_circle1 < test_circle2)

    def test_greater_than(self):
        test_circle1 = Circle(20)
        test_circle2 = Circle(21)
        self.assertFalse(test_circle1 > test_circle2)

    def test_not_equal(self):
        test_circle1 = Circle(20)
        test_circle2 = Circle(21)
        self.assertNotEqual(test_circle1, test_circle2)

    def test_equal(self):
        test_circle1 = Circle(20)
        test_circle2 = Circle(20)
        self.assertEqual(test_circle1, test_circle2)

if __name__ == '__main__':
    unittest.main()
