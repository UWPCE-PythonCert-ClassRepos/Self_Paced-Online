#!/usr/bin/env python3

import unittest
from circle_class import Circle

class CircleTestCase(unittest.TestCase):

    def test_radius_100(self):
        c = Circle(5)
        self.assertEqual(c.radius, 5)

    def test_radius_101(self):
        c = Circle(70)
        self.assertEqual(c.radius, 70)
        c.radius = 60
        self.assertEqual(c.radius, 60)

    def test_radius_102(self):
        with self.assertRaises(ValueError):
            c = Circle(-4)

    def test_diameter_100(self):
        c = Circle(20)
        self.assertEqual(c.diameter, 40)
        self.assertEqual(c.radius, 20)

    def test_diameter_101(self):
        c = Circle(100)
        c.radius = 14
        self.assertEqual(c.diameter, 28)
        self.assertEqual(c.radius, 14)

    def test_diameter_102(self):
        c = Circle(50)
        c.diameter = 80
        self.assertEqual(c.diameter, 80)
        self.assertEqual(c.radius, 40)

    def test_diameter_103(self):
        c = Circle(72)
        c.diameter += 6
        self.assertEqual(c.diameter, 150)
        self.assertEqual(c.radius, 75)
                
    def test_diameter_104(self):
        c = Circle(48)
        with self.assertRaises(ValueError):
            c.diameter = -2

    def test_area_100(self):
        c = Circle(8)
        self.assertLess(abs(c.area-201.062), 0.1)
        
    def test_area_101(self):
        c = Circle(12)
        with self.assertRaises(AttributeError):
            c.area = 58

    def test_diameter_constructor_100(self):
        c = Circle.from_diameter(18)
        self.assertEqual(c.diameter, 18)
        self.assertEqual(c.radius, 9)
        self.assertLess(abs(c.area-254.469), 0.1)

    def test_diameter_constructor_101(self):
        with self.assertRaises(ValueError):
            c = Circle.from_diameter(-6)
        
    def test_repr_100(self):
        c = Circle(200)
        self.assertEqual(repr(c), 'Circle(200)')

    def test_repr_101(self):
        c = Circle.from_diameter(500)
        self.assertEqual(repr(c), 'Circle(250.0)')

    def test_repr_102(self):
        c = Circle(10)
        d = eval(repr(c))
        self.assertIsInstance(d, Circle)
        self.assertEqual(d.radius, 10)
        self.assertEqual(d.diameter, 20)
        self.assertLess(abs(d.area-314.159), 0.1)

    def test_str_100(self):
        c = Circle(4.555)
        self.assertTrue("Circle with radius: 4.55" in str(c))


if __name__ == "__main__":
    unittest.main()