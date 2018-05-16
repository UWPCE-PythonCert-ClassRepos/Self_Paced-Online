import unittest
from Circle import Circle
from math import pi


class CircleTest(unittest.TestCase):
    # Tests for Circle.py
    def test_radius(self):
        # Step 1
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_diameter(self):
        # Step 2
        c = Circle(6)
        self.assertEqual(c.diameter, 12)

    def test_set_diameter(self):
        # Step 3
        c = Circle(4)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        self.assertEqual(c.radius, 1)

    def test_area(self):
        # Step 4
        c = Circle(2)
        area = round(c.area, 3)
        self.assertEqual(area, 12.566)

    def test_from_diameter(self):
        # Step 5
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius, 4)

    def test_str_repr(self):
        # Step 6
        c = Circle(4)
        self.assertEqual(str(c), "Circle with radius: 4")
        self.assertEqual(repr(c), 'Circle(4)')

    def test_add(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual(c1+c2, Circle(6))

    def test_mul(self):
        c1 = Circle(2)
        c2 = 4
        self.assertEqual(c1*c2, Circle(8))

    def test_eq(self):
        c1 = Circle(2)
        c2 = Circle(5)
        self.assertNotEqual(c1, c2)

    def test_lt(self):
        c1 = Circle(3)
        c2 = Circle(4)
        self.assertTrue(c1 < c2)

    def test_gt(self):
        c1 = Circle(10)
        c2 = Circle(5)
        self.assertTrue(c1 > c2)

    def test_ge(self):
        c1 = Circle(3)
        c2 = Circle(3)
        c3 = Circle(4)
        self.assertTrue(c1 >= c2)
        self.assertTrue(c3 >= c2)

    def test_le(self):
        c1 = Circle(3)
        c2 = Circle(3)
        c3 = Circle(4)
        self.assertTrue(c1 <= c2)
        self.assertTrue(c2 <= c3)

    def test_eq(self):
        c1 = Circle(20)
        c2 = Circle(20)
        self.assertTrue(c1 == c2)

if __name__ == '__main__':
    unittest.main()

