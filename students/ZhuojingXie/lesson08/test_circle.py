import unittest
from circle import Circle
from math import pi

class TestCircle(unittest.TestCase):

    def test_Circle_Case(self):
        test = Circle(4)
        self.assertEqual(test.radius, 4)

    def test_diameter(self):
        test = Circle(4)
        self.assertEqual(test.diameter, 8)
        test.diameter =6
        self.assertEqual(test.radius, 3)

    def test_area(self):
        test = Circle(2)
        self.assertEqual(test.area,12.566370614359172)

    def test___repr__(self):
        c = Circle(4)
        self.assertEqual(repr(c), 'Circle(4)')

    def test___str__(self):
        c = Circle(4)
        self.assertEqual(str(c), 'Circle with radius: 4')

    def test___add__(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual(c1 + c2, Circle(6))

    def test___mul__(self):
        c1 = Circle(4)
        t=3
        self.assertEqual(c1 * 3, Circle(12))

    def test___lt__(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertTrue(c1 < c2)

    def test___gt__(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertFalse(c2 < c1)

    def test___eq__(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertNotEqual(c1, c2)

    def test___iadd_(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c1 += c2
        self.assertEqual(c1, Circle(6))



if __name__ == '__main__':
    unittest.main()
