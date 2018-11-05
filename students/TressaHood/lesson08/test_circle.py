#!/usr/bin/env python3

"""
Lesson 08, Test file for circle class assignment, created test cases that were used through the creation
of the circle program
"""
import unittest
import numpy as np

# import all the functions
from circle import *


class TestingCircle(unittest.TestCase):

    def test_init(self):
        """Test initialization"""

        # test the default radius
        c = Circle()
        assert c.radius == 6

        # test giving it a radius
        c = Circle(4)
        assert c.radius == 4

    def test_diameter(self):
        """Function to test calculating the diameter of a circle"""

        # test the default diameter
        c = Circle()
        assert c.diameter == 12

        # test the diameter when passing radius
        c = Circle(4)
        assert c.diameter == 8

        # test when from radius
        c.diameter = 2
        assert c.radius == 1

    def test_area(self):
        """Function to test the calculation of the area of a circle"""

        # test giving it an area
        c = Circle(2)

        assert(np.allclose(c.area, 12.566370))

        # test that the user can't set the area
        c = Circle(2)
        with self.assertRaises(AttributeError):
            c.area = 42

    def test_print(self):
        """Function to test the printing methods"""

        # test print
        c = Circle(4)
        print(c)
        self.assertTrue(c)

        # repr function
        print(repr(c))
        self.assertTrue(repr(c))

    def test_addCircles(self):
        """Function to test the adding methods"""
        c1 = Circle(2)
        c2 = Circle(4)

        # add
        both = c1 + c2
        self.assertEqual(both.radius, 6)

        # multiply
        mul_both = c2 * 3
        self.assertEqual(mul_both.radius, 12)

        # multiply other way!
        mul_both = 3 * c2
        self.assertEqual(mul_both.radius, 12)

    def test_equals(self):
        """Function to test the less than, greater, equals"""
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = Circle(4)

        self.assertFalse(c1 > c2)
        self.assertTrue(c1 < c2)
        self.assertEqual(c2, c3)

    def test_sort(self):
        """Function to test sorting of circles"""
        circles = [
            Circle(6),
            Circle(7),
            Circle(8),
            Circle(4),
            Circle(0),
            Circle(2),
            Circle(3),
            Circle(5),
            Circle(9),
            Circle(1)]

        sort_circles = sorted(circles, key=Circle.sort_key)
        self.assertEqual(sort_circles, [Circle(0), Circle(1), Circle(2), Circle(
            3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)])

    def test_alternate(self):
        """Function to test alternate constructor"""
        c = Circle.from_diameter(8)
        # print(c.diameter)
        # print(c.radius)

        self.assertEqual(c.diameter, 8.0)
        self.assertEqual(c.radius, 4.0)

if __name__ == '__main__':

    # call the main testing function
    unittest.main()
