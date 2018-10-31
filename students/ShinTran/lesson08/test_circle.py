'''
Shin Tran
Python 210
Assignment 8
'''

from circle import *
import unittest
import math


class TestCircle(unittest.TestCase):

    def test_initializaation(self):
        """Initialize the circle to have a radius of 5"""
        c1 = Circle(5)
        self.assertEqual(c1.radius, 5)
        self.assertEqual(c1.diameter, 10)
        
        
    def test_update_diameter(self):
        """Updating the diameter to 8"""
        c2 = Circle(5)
        self.assertEqual(c2.diameter, 10)
        self.assertEqual(c2.radius, 5)
        c2.diameter = 8
        self.assertEqual(c2.diameter, 8)
        self.assertEqual(c2.radius, 4)


    def test_area(self):
        """"Test the area function should return pi*r^2"""
        c3 = Circle(3)
        self.assertEqual(c3.area, math.pi * math.pow(3,2))


    def test_initialize_diameter(self):
        """Initializing a circle using diameter of 12"""
        c4 = Circle.from_diameter(12)
        self.assertEqual(c4.diameter, 12)
        self.assertEqual(c4.radius, 6)


    def test_string_func(self):
        """Test the string fuctions str and repr"""
        c5 = Circle(7)
        self.assertEqual(str(c5), "Circle with raidus: 7")
        self.assertEqual(repr(c5), "'Circle(7)'")

    def test_addition(self):
        """Ensure that two circles can be added together, also tests if a
        circle can be incremented with another circle via operator shortcut"""
        c6 = Circle(4)
        c7 = Circle(6)
        c8 = c6 + c7
        self.assertEqual(c8.radius, 10)
        self.assertEqual(str(c8), "Circle with raidus: 10")
        self.assertEqual(repr(c8), "'Circle(10)'")
        c8 += c7
        self.assertEqual(c8.radius, 16)

    def test_multiplication(self):
        """Ensure that a circle can be multiplied by a number, also tests
        if a circle can be incremented with number via operator shortcut"""
        c9 = Circle(3)
        c10 = c9 * 3
        self.assertEqual(repr(c10), "'Circle(9)'")
        c10 *= 2
        self.assertEqual(repr(c10), "'Circle(18)'")

    def test_equality(self):
        """Test the comparison methods lt, le, gt, ge, eq, ne"""
        c11 = Circle(11)
        c12 = Circle(12)
        c13 = Circle(12)
        c14 = Circle(13)
        self.assertEqual(c11 < c12, True)
        self.assertEqual(c12 > c11, True)
        self.assertEqual(c12 == c13, True)
        self.assertEqual(c14 < c13, False)
        self.assertEqual(c13 >= c12, True)
        self.assertEqual(c13 <= c12, True)
        self.assertEqual(c11 != c14, True)
        self.assertEqual(c13 == c14, False)

    def test_sorted(self):
        """"Tests the sorting of a list of circles"""
        clist = [Circle(2), Circle(4), Circle(3), Circle(1)]
        sclist = sorted(clist, key=lambda x: x.radius)
        self.assertEqual(sclist, [Circle(1), Circle(2), Circle(3), Circle(4)])

    def test_subtraction(self):
        """Ensure that two circles can be subtracted from one another"""
        c15 = Circle(9)
        c16 = Circle(7)
        c17 = c15 - c16
        self.assertEqual(c17.radius, 2)
        self.assertEqual(str(c17), "Circle with raidus: 2")
        self.assertEqual(repr(c17), "'Circle(2)'")

    def test_division(self):
        """Ensure that a circle can be divided by a number"""
        c18 = Circle(15)
        c19 = c18 / 3
        self.assertEqual(c19.radius, 5.0)
        self.assertEqual(str(c19), "Circle with raidus: 5.0")
        self.assertEqual(repr(c19), "'Circle(5.0)'")

    def test_circumference(self):
        """"Test the circumference function should return pi*d or 2*pi*r"""
        c20 = Circle(10)
        self.assertEqual(c20.circumference, math.pi * 20)

# Main method so the program would run
if __name__ == '__main__':
    unittest.main()
