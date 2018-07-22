import unittest
from circle import Circle
import math


class TestCircle(unittest.TestCase):

    def test_1_circle(self):
        c = Circle(10)
        self.assertEqual(c.radius, 10)

    def test_2_diameter(self):
        c = Circle(6)
        self.assertEqual(c.diameter, 12)

    def test_3_diameter_radius(self):
        c = Circle(8)
        c.diameter = 8
        self.assertEqual(c.radius, 4)

    def test_4_area(self):
        c = Circle(10)
        self.assertEqual(c.area, math.pi * 10 ** 2)

    def test_5_circle_diameter(self):
        c1 = Circle(5)
        c2 = Circle.from_diameter(10)
        self.assertEqual(c1, c2)

    def test_6_repr(self):
        c = Circle(10)
        self.assertEqual(repr(c), 'Circle(10)')

    def test_7_num_protocol(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual(c1 + c2, Circle(6))

    def test_8_compare(self):
        c1 = Circle(1)
        c2 = Circle(2)
        c3 = Circle(3)
        self.assertEqual(c1 + c2, c3)
        self.assertEqual(c1 < c2, True)
        self.assertEqual(c3 > c2, True)
        self.assertEqual(c1 + c2 == c3, True)

    def test_9_magic(self):
        circles = [Circle(10) for i in range(0, 9)]
        c = Circle(10)
        for j in circles:
            c += j
        self.assertEqual(c, Circle(100))
        c = Circle(10)
        for j in circles[0:3]:
            c *= j
        self.assertEqual(c, Circle(10000))

    def test_10_set_area(self):
        c = Circle(10)
        try:
            c.area = 11
        except AttributeError:
            caught = 'AttributeError'
        self.assertEqual(caught, 'AttributeError')


if __name__ == '__main__':
    unittest.main()
