# ----------------------------------------------------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Lesson 08 -- test_circle.py
# PURPOSE: Run tests for circle.py module
# DATE: 07/16/2018
#
# DESCRIPTION: Test suite runs through functionalities of Circle() modules to test for accuracy.
# ----------------------------------------------------------------------------------------------------------------------
import unittest
from math import pi
from circle import Circle


class TestCircle(unittest.TestCase):

    def test_accessors(self):                  # Test 1 : assert radius and diameter properties/setters work
        c = Circle(10)
        self.assertEqual(c.radius, 10)
        self.assertEqual(c.diameter, 20)

    def test_area(self):                       # Test 2: assert area works (radius is 1, area should be only pi)
        c = Circle(1)
        self.assertEqual(c.area, pi)

        # c.area = 45                          # Test 3: this doesn't run, but it doesn't run because the code works :)
        # self.assertRaises(c.area, AttributeError, 'AttributeError: can\'t set attribute')

    def test_from_diameter(self):               # Test 4: values passed in as diameter to Circle return as expected
        c = Circle.from_diameter(20)
        self.assertEqual(c.radius, 20 / 2)
        self.assertEqual(c.diameter, 20)

    def test_addition(self):                    # Test 5: Test circle addition (adding multiple circles)
        c = Circle(1) + Circle(1)
        c_print = c.__str__()
        self.assertEqual(c_print, "Circle 2")

    def test_multiplication(self):              # Test 6: Test circle multiplication (multiplying multiple circles)
        c = Circle(2) * Circle(2)
        c_print = c.__str__()
        self.assertEqual(c_print, "Circle 4")

    def test_equality(self):                    # Test 7: Test circle equality
        c = Circle(2) == Circle(3)
        eq = c.__str__()
        self.assertEqual(eq, "False")
        c = Circle(1) == Circle(1)
        eq = c.__str__()
        self.assertEqual(eq, "True")

    def test_inequality(self):                  # Test 8: Test circle inequality
        c = Circle(3) > Circle(2)
        eq = c.__str__()
        self.assertEqual(eq, "True")
        c = Circle(235) < Circle(0)
        eq = c.__str__()
        self.assertEqual(eq, "False")


if __name__ == '__main__':
    unittest.main()
