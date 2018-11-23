# ------------------------------------------------- #
# Title: Lesson 8, pt 2/2 Circle Test
# Dev:   Craig Morton
# Date:  9/24/2018
# Change Log: CraigM, 9/24/2018, Circle Test
# ------------------------------------------------- #

from math import pi
from Circle import Circle
import random
import unittest


class CircleTest(unittest.TestCase):
    """Circle unit tests"""

    def test_constructor(self):
        for i in range(100):
            c = Circle(i)
            self.assertEqual(c.radius, i)
            self.assertEqual(c.diameter, i * 2)

    def test_properties(self):
        for i in range(100):
            c = Circle(i)
            c.radius = c.radius + 1
            self.assertEqual(c.radius, i + 1)
            self.assertEqual(c.diameter, c.radius * 2)

            new_diameter = c.diameter * 2
            c.diameter = new_diameter
            self.assertEqual(c.radius, new_diameter / 2)
            self.assertEqual(c.diameter, new_diameter)

    def test_area(self):
        pi2 = pi * 2
        for i in range(100):
            c = Circle(i)
            area = pi2 * i
            self.assertEqual(c.area, area)

    def test_from_diameter(self):
        for i in range(100):
            c = Circle.from_diameter(i)
            self.assertEqual(c.radius, i / 2)
            self.assertEqual(c.diameter, i)

    def test_equal(self):
        for i in range(100):
            c1 = Circle(i)
            c2 = Circle(i)
            c3 = Circle(i + 1)
            self.assertEqual(c1, c2)
            self.assertNotEqual(c1, c3)

    def test_repr(self):
        for i in range(100):
            c1 = Circle(i)
            repr_c1 = repr(c1)
            c2 = eval(repr_c1)
            self.assertEqual(c1, c2)

    def test_addition(self):
        for i in range(100):
            # Addition
            c1 = Circle(i)
            c2 = Circle(i * 2)
            self.assertEqual(c2, c1 + c1)
            c1 += c1
            self.assertEqual(c2, c1)

    def test_multiply(self):
        for i in range(100):
            # Addition
            c1 = Circle(i)
            c2 = Circle(i * 2)
            self.assertEqual(c2, c1 * 2)
            self.assertEqual(c2, 2 * c1)
            c1 *= 2
            self.assertEqual(c2, c1)

    def test_less_than(self):
        for i in range(100):
            c1 = Circle(i)
            c2 = Circle(i + 1)
            self.assertTrue(c1 < c2)
            self.assertFalse(c2 < c1)
            self.assertFalse(c1 < c1)

    def test_sort(self):
        circle_list = [Circle(random.randint(0, 10000)) for i in range(100)]
        circle_list_s1 = sorted(circle_list)
        circle_list_s2 = sorted(circle_list, key=Circle.sort_key)
        self.assertEqual(circle_list_s1, circle_list_s2)
        for i in range(99):
            self.assertTrue(circle_list_s1[i] < circle_list_s1[i + 1])


if __name__ == "__main__":
    unittest.main()

