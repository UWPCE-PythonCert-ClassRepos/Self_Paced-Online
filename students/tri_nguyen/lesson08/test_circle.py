# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  01-Apr-2018
# ------------------------------------------- #

import unittest
from circle import Circle
import math

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle(2)
        self.c2 = Circle(4.5)
        self.c3 = Circle(6)
        self.c4 = Circle.from_diameter(3)
        self.c5 = Circle(6)

    def tearDown(self):
        pass

    def test__init__(self):
        with self.assertRaises(TypeError):
            a_circle = Circle(-1)
            another_circle = Circle('tri')

    def test_diameter(self):
        self.assertEqual(self.c1.diameter, 4)
        self.assertEqual(self.c2.diameter, 4.5*2)
        self.assertEqual(self.c3.diameter, 12)

    def test_area(self):
        self.assertEqual(self.c1.area, round(math.pi * 2**2, 5))
        self.assertEqual(self.c2.area, round(math.pi * 4.5**2, 5))
        self.assertEqual(self.c3.area, round(math.pi * 6**2, 5))

    def test_from_diameter(self):
        self.assertEqual(self.c4.diameter, 3)
        self.assertEqual(self.c4.radius, 3/2)

        with self.assertRaises(TypeError):
            c = Circle.from_diameter('t')

    def test__str__(self):
        test_template = 'Circle with radius: {}'
        self.assertEqual(self.c1.__str__(), test_template.format(2))
        self.assertEqual(self.c2.__str__(), test_template.format(4.5))
        self.assertEqual(self.c3.__str__(), test_template.format(6))

    def test__repr__(self):
        test_template = 'Circle({})'
        self.assertEqual(self.c1.__repr__(), test_template.format(2))
        self.assertEqual(self.c2.__repr__(), test_template.format(4.5))
        self.assertEqual(self.c3.__repr__(), test_template.format(6))

    def test__add__(self):
        self.assertEqual(self.c1 + self.c3, Circle(8))
        self.assertEqual(self.c2 + self.c3, Circle(10.5))

        with self.assertRaises(TypeError):
            self.c1 + 2

    def test__iadd__(self):
        self.assertEqual(self.c1.__iadd__(self.c2), Circle(6.5))

        with self.assertRaises(TypeError):
            self.c1 += 6

    def test__mul__(self):
        self.assertEqual(self.c5 * 2, Circle(12))
        self.assertEqual(self.c2 * 5, Circle(4.5 * 5))

        with self.assertRaises(TypeError):
            self.c3 * self.c5

    def test__rmul__(self):
        self.assertEqual(2 * self.c5, Circle(6 * 2))
        self.assertEqual(5 * self.c2, Circle(4.5 * 5))

    def test__imul__(self):
        self.assertEqual(self.c3.__imul__(3), Circle(18))
        self.assertEqual(self.c2.__imul__(4), Circle(4.5 * 4))

        with self.assertRaises(TypeError):
            self.c3 *= self.c1

    def test__gt__(self):
        self.assertTrue(self.c2.radius > self.c1.radius)
        self.assertTrue(self.c5.radius > self.c1.radius)
        self.assertFalse(self.c2.radius > self.c5.radius)

    def test__lt__(self):
        self.assertTrue(self.c1.radius < self.c5.radius)
        self.assertFalse(self.c2.radius < self.c1.radius)
        self.assertTrue(self.c1.radius < self.c3.radius)

    def test__eq__(self):
        self.assertTrue(self.c3.radius == self.c5.radius)


if __name__ == '__main__':
    unittest.main()
