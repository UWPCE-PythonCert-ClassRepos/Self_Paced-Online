# !/usr/bin/env python3
# Test Code for circle Build/Sort ptfbanks

import math
from pfcircle import Circle
from unittest import TestCase

class TestCircle(TestCase):

    def test_radius(self):
        c = Circle(4)
        print(c.radius)
        assert c.radius == 4

    def test_diameter(self):
        c = Circle(4)
        print(c.diameter)
        self.assertEqual(c.diameter, 8)

    def test_diameter(self):
        c = Circle(2)
        print(c.diameter)
        assert c.diameter == 4

    def test_from_diameter(self):
        c = Circle.from_diameter(6)
        assert round(c.circum, 4) == 18.8496        
        self.assertEqual(c.radius, 3)

    def test_area(self):
        c = Circle(2)
        assert round(c.area, 3) == 12.566

#    def test_area(self):         # Confirmed instruction statement
#        c = Circle.from_area(42)
#        assert AttributeError

    # Circle String Tests
    def test_circle_strings(self):
        c = Circle(4)
        self.assertEqual(str(c), 'Circle of radius: 4')
        self.assertEqual(repr(c), 'Circle(4)')

# Test Numerics
    def test_add(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual((c1 + c2), Circle(6))
        
    def test_mul(self):
        c1 = Circle(4)        
        c2 = c1 * 3   
        self.assertEqual(c2.radius, 12)
        self.assertEqual(repr(c2), 'Circle(12)')

# Test Comparisons
    def test_gt(self):
        c1 = Circle(3)
        c2 = Circle(4)
        self.assertFalse(c1 > c2)

    def test_ge(self):
        c1 = Circle(3)
        c2 = Circle(5)
        c3 = Circle(3)
        self.assertFalse(c1 >= c2)
        self.assertTrue(c2 >= c3)

    def test_lt(self):
        c1 = Circle(5)
        c2 = Circle(3)
        self.assertTrue(c1 > c2)

    def test_le(self):
        c1 = Circle(8)
        c2 = Circle(5)
        c3 = Circle(5)
        self.assertTrue(c2 <= c1)
        self.assertTrue(c2 <= c3)

    def test_eq(self):
        c1 = Circle(6)
        c2 = Circle(6)
        self.assertTrue(c1 == c2)

    def test_ne(self):
        c1 = Circle(2.1)
        c2 = Circle(1.2)
        self.assertTrue(c1 != c2)

# Circle Sort-----------------
    def test_sort(self):
        circles = [Circle(2), Circle(5.2), Circle(9), Circle(7), Circle(3.1), Circle(2.5), 
                 Circle(5), Circle(4), Circle(6), Circle(4.1)]
        circles.sort()
        self.assertTrue(circles== [Circle(2), Circle(2.5), Circle(3.1), Circle(4),
                        Circle(4.1), Circle(5), Circle(5.2), Circle(6), Circle(7), Circle(9)])
