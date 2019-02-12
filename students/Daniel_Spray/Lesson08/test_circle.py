import unittest
import circle
from circle import *

class TestCircle(unittest.TestCase):

    def test_step1(self):
        c = circle.Circle(4)
        actual = c.radius
        expected = 4
        self.assertEqual(expected, actual)

    def test_step2(self):
        c = circle.Circle(4)
        actual = c.diameter
        expected = 8
        self.assertEqual(expected, actual)

    def test_step3(self):
        c = circle.Circle(4)
        c.diameter = 2
        actual = c.radius
        expected = 1
        self.assertEqual(expected, actual)

    def test_step4(self):
        c = circle.Circle(2)
        expected =  math.pi*2**2
        self.assertEqual(expected, c.area)

    def test_step5(self):
        c = circle.Circle.from_diameter(8)
        actual = c.radius
        expected = 4
        self.assertEqual(expected, actual)

    def test_step6(self):
        c = circle.Circle(4)
        actual = eval(repr(c))
        expected = 'Circle(4)'
        self.assertEqual(expected, actual)

    def test_step7(self):
        c1 = circle.Circle(2)
        c2 = circle.Circle(4)
        actual = c1+c2
        expected = circle.Circle(6)
        self.assertEqual(expected, actual)
        actual2 = c2*3
        expected2 = circle.Circle(12)
        self.assertEqual(expected2, actual2)

    def test_step8(self):
        c1 = circle.Circle(2)
        c2 = circle.Circle(4)
        actual = c1>c2
        expected = False
        self.assertEqual(expected, actual)
        actual2 = c1<c2
        expected2 = True
        self.assertEqual(expected, actual)
        c3 = Circle(4)
        actual3 = c2==c3
        expected3 = True
        self.assertEqual(expected, actual)
        circles = [c2,c1]
        actual4 = circles.sort()
        expected = [c1,c2]
        self.assertEqual(expected, actual)