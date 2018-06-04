#!/usr/bin/env python3
import unittest
from circle import Circle

class MyTestCase(unittest.TestCase):
    def test_radius(self):
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_diameter(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)

    def test_diameter_set(self):
        c = Circle(4)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        self.assertEqual(c.radius, 1)

    def test_area(self):
        c = Circle(2)
        self.assertEqual(c.area, 12.57)

    def test_area_set(self):
        with self.assertRaises(AttributeError):
            c = Circle(2)
            c.area = 42

    def test_dimater_constructor(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius, 4)

    def test_str(self):
        c = Circle(4)
        self.assertMultiLineEqual(str(c), "Circle with radius: 4.00.")

    def test_repr(self):
        c = Circle(4)
        self.assertMultiLineEqual(repr(c), "Circle(4)")

    def test_add(self):
        c1 = Circle(2)
        c2 = Circle(4)
        sum = c1 + c2
        self.assertEqual(sum, 6)

    def test_mul(self):
        c2 = Circle(4)
        multiply = c2 * 3
        self.assertEqual(multiply, 12)

    def test_conditional_statements(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = Circle(4)
        self.assertFalse(c1 > c2)
        self.assertTrue(c1 < c2)
        self.assertFalse(c1 == c2)
        self.assertTrue(c2 == c3)

    def test_radius_sort(self):
        c = Circle(2)
        c1 = Circle(9)
        c2 = Circle(1)
        c3 = Circle(11)
        lst_radius = [c2,c,c1,c3]
        lst_radius.sort(key=Circle.sort_key)
        self.assertTrue(lst_radius, [Circle(1),Circle(2),Circle(9),Circle(11)])


if __name__ == '__main__':
    unittest.main()
