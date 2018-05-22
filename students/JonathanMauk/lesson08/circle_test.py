import unittest
from circle import Circle
from math import pi


class CircleTest(unittest.TestCase):

    def test_radius(self):
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_diameter1(self):
        c = Circle(8)
        self.assertEqual(c.diameter, 16)

    def test_diameter2(self):
        c = Circle(6)
        c.diameter = 10
        self.assertEqual(c.radius, 5)

    def test_area(self):
        c = Circle(3)
        self.assertEqual(c.area, pi * 3 ** 2)

    def test_area_error(self):
        c = Circle(5)
        with self.assertRaises(AttributeError):
            c.area = 12

    def test_from_diameter(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.radius, 4)

    def test_str(self):
        c = Circle(12)
        self.assertEqual(str(c), "Circle with radius: 12")

    def test_repr(self):
        c = Circle(24)
        self.assertEqual(repr(c), "Circle(24)")

    def test_numeric1(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = c1 + c2
        self.assertEqual(c3.radius, 6)

    def test_numeric2(self):
        c1 = Circle(5)
        c2 = c1 * 3
        self.assertEqual(c2.radius, 15)


if __name__ == '__main__':
    unittest.main()
