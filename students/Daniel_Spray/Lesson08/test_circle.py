import unittest
import circle
import math
from circle import Circle

class TestCircle(unittest.TestCase):

    def test_step1(self):
    """Run a test to show the circle has a radius attribute"""
        c = Circle(4)
        actual = c.radius
        expected = 4
        self.assertEqual(expected, actual)

    def test_step2(self):
    """Run a test to show the user can get the diameter of the circle"""
        c = Circle(4)
        actual = c.diameter
        expected = 8
        self.assertEqual(expected, actual)

    def test_step3(self):
    """Run a test to show the diameter can be set"""
        c = Circle(4)
        c.diameter = 2
        actual = c.radius
        expected = 1
        self.assertEqual(expected, actual)

    def test_step4(self):
    """Run a test to show the area calculation works"""
        c = Circle(2)
        expected =  math.pi*2**2
        actual = c.area
        self.assertEqual(expected, actual)

    def test_step5(self):
    """Run a test to show you can set the radius from the diameter"""
        c = Circle.from_diameter(8)
        actual = c.radius
        expected = 4
        self.assertEqual(expected, actual)

    def test_step6(self):
    """Run a test to show string printing works"""
        c = Circle(4)
        expected = 'Circle(4)'
        actual = repr(c)
        self.assertEqual(expected, actual)

    def test_step7(self):
    """Run a test to show addition works"""
        c1 = Circle(2)
        c2 = Circle(4)
        actual = c1+c2
        expected = Circle(6)
        self.assertEqual(expected, actual)
        actual2 = c2*3
        expected2 = Circle(12)
        self.assertEqual(expected2, actual2)

    def test_step8(self):
    """Run a test to show comparisons work"""
        c1 = Circle(2)
        c2 = Circle(4)
        actual = c1>c2
        expected = False
        self.assertEqual(expected, actual)
        actual2 = c1<c2
        expected2 = True
        self.assertEqual(expected2, actual2)
        c3 = Circle(4)
        actual3 = c2==c3
        expected3 = True
        self.assertEqual(expected3, actual3)
        circles = [Circle(3),Circle(4),Circle(2)]
        circles.sort()
        expected4 = [Circle(2),Circle(3),Circle(4)]
        self.assertEqual(expected4, circles)