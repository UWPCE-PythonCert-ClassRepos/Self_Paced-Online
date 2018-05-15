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
            del c

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
            del c
        
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

    def test_add_100(self):
        c1 = Circle(4)
        c2 = Circle.from_diameter(10)
        c3 = c1 + c2
        self.assertIsInstance(c3, Circle)
        self.assertEqual(c3.radius, 9)
        self.assertEqual(c3.diameter, 18)
        self.assertLess(abs(c3.area-254.469), 0.1)

    def test_add_101(self):
        c1 = Circle(6)
        c2 = c1 + 2
        self.assertIsInstance(c2, Circle)
        self.assertEqual(c2.radius, 8)
        self.assertEqual(c2.diameter, 16)
        self.assertLess(abs(c2.area-201.062), 0.1)

    def test_add_102(self):
        c1 = Circle.from_diameter(14)
        c2 = 3 + c1
        self.assertIsInstance(c2, Circle)
        self.assertEqual(c2.radius, 10)
        self.assertEqual(c2.diameter, 20)
        self.assertLess(abs(c2.area-314.159), 0.1)

    def test_add_103(self):
        c1 = Circle.from_diameter(8)
        c2 = c1 + 0.75
        self.assertIsInstance(c2, Circle)
        self.assertEqual(c2.radius, 4.75)
        self.assertEqual(c2.diameter, 9.5)
        self.assertLess(abs(c2.area-70.882), 0.1)

    def test_add_110(self):
        c1 = Circle(5)
        with self.assertRaises(ValueError):
            c2 = c1 + (-6)
            del c2

    def test_add_111(self):
        c1 = Circle(5)
        with self.assertRaises(TypeError):
            c2 = c1 + "86"
            del c2

    def test_multiply_100(self):
        c1 = Circle(5)
        c2 = Circle.from_diameter(6)
        c3 = c1 * c2
        self.assertIsInstance(c3, Circle)
        self.assertEqual(c3.radius, 15)
        self.assertEqual(c3.diameter, 30)
        self.assertLess(abs(c3.area-706.858), 0.1)

    def test_multiply_101(self):
        c1 = Circle(6)
        c2 = c1 * 4
        self.assertIsInstance(c2, Circle)
        self.assertEqual(c2.radius, 24)
        self.assertEqual(c2.diameter, 48)
        self.assertLess(abs(c2.area-1809.557), 0.1)

    def test_multiply_102(self):
        c1 = Circle.from_diameter(14)
        c2 = 3 * c1
        self.assertIsInstance(c2, Circle)
        self.assertEqual(c2.radius, 21)
        self.assertEqual(c2.diameter, 42)
        self.assertLess(abs(c2.area-1385.442), 0.1)

    def test_multiply_103(self):
        c1 = Circle.from_diameter(8)
        c2 = c1 * 0.75
        self.assertIsInstance(c2, Circle)
        self.assertEqual(c2.radius, 3.0)
        self.assertEqual(c2.diameter, 6.0)
        self.assertLess(abs(c2.area-28.274), 0.1)

    def test_multiply_110(self):
        c1 = Circle(6)
        with self.assertRaises(ValueError):
            c2 = c1 * -4
            del c2

    def test_multiply_111(self):
        c1 = Circle(6)
        with self.assertRaises(TypeError):
            c2 = c1 * "54"
            del c2

    def test_comps_100(self):
        c1 = Circle(7)
        c2 = Circle(8)
        self.assertTrue(c1 < c2)
        self.assertTrue(c1 <= c2)
        self.assertFalse(c1 == c2)
        self.assertFalse(c1 > c2)
        self.assertFalse(c1 >= c2)
        self.assertTrue(c1 != c2)
        
    def test_comps_101(self):
        c1 = Circle(8)
        c2 = Circle(8)
        self.assertFalse(c1 < c2)
        self.assertTrue(c1 <= c2)
        self.assertTrue(c1 == c2)
        self.assertFalse(c1 > c2)
        self.assertTrue(c1 >= c2)
        self.assertFalse(c1 != c2)
        
    def test_comps_102(self):
        c1 = Circle(9)
        c2 = Circle(8)
        self.assertFalse(c1 < c2)
        self.assertFalse(c1 <= c2)
        self.assertFalse(c1 == c2)
        self.assertTrue(c1 > c2)
        self.assertTrue(c1 >= c2)
        self.assertTrue(c1 != c2)
        


if __name__ == "__main__":
    unittest.main()