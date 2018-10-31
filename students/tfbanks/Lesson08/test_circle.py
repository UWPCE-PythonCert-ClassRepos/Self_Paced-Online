# test code for circle.py by tfbanks
# !/usr/bin/env python3

from unittest import TestCase
from circle import Circle


class TestCircle(TestCase):
    # Radius test
    def test_radius(self):
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    # Diameter test
    def test_diameter(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)

    # Area test
    def test_area(self):
        c = Circle(2)
        self.assertEqual(round(c.area, 5), 12.566370)

    # Set Diameter test
    def test_set_diameter(self):
        c = Circle(4)
        c.diameter = 6
        self.assertTrue(c.diameter, 6)
        self.assertTrue(c.radius, 3)

    # Circle from Diameter test
    def test_from_diameter(self):
        c = Circle.from_diameter(8)
        self.assertTrue(c.diameter, 8)
        self.assertTrue(c.radius, 4)

    # Circle String Tests
    def test_circle_strings(self):
        c = Circle(4)
        self.assertEqual(str(c), 'Circle with radius: 4')
        self.assertEqual(repr(c), 'Circle(4)')

    # Add Circles Test
    def test_add(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual((c1 + c2), Circle(6))
        
    def test_mul(self):
        c1 = Circle(4)        
        c2 = c1 * 3   
        self.assertEqual(c2.radius, 12)
        self.assertEqual(repr(c2), 'Circle(12)')

    # GreaterThan Test
    def test_gt(self):
        c1 = Circle(3)
        c2 = Circle(4)
        self.assertTrue(c2 > c1)

    # GreaterThanEqual Test
    def test_ge(self):
        c1 = Circle(3)
        c2 = Circle(5)
        c3 = Circle(3)
        self.assertTrue(c2 >= c1)
        self.assertTrue(c1 >= c3)

    # LessThan Test
    def test_lt(self):
        c1 = Circle(5)
        c2 = Circle(3)
        self.assertTrue(c1 > c2)

    # LessThanEqual Test
    def test_le(self):
        c1 = Circle(8)
        c2 = Circle(5)
        c3 = Circle(5)
        self.assertTrue(c2 <= c1)
        self.assertTrue(c2 <= c3)

    # Equals Test
    def test_eq(self):
        c1 = Circle(6)
        c2 = Circle(6)
        self.assertTrue(c1 == c2)

    # NotEquals Test
    def test_ne(self):
        c1 = Circle(2)
        c2 = Circle(2)
        self.assertTrue(c1 != c2)

    # Sort Key Test
    def test_sort(self):
        circl = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), 
                 Circle(3), Circle(5), Circle(9), Circle(1)]
        circl.sort()
        self.assertTrue(circl == [Circle(0), Circle(1), Circle(2), Circle(3),
                        Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)])
