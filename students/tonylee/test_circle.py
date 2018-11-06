import unittest
from circle import Circle
from math import pi

class TestCircle(unittest.TestCase):

    def test_step1(self):
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_step2(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)

    def test_step3(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)
        c.diameter = 2
        self.assertEqual(c.radius, 1)

    def test_step4(self):
        c = Circle(2)
        self.assertAlmostEqual(c.area, round(2**2*pi,6))
        with self.assertRaises(AttributeError):
            c.area = 42
            print("The user cannot set the area")

    def test_step5(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius, 4)

    def test_step6_str(self):
        c = Circle(4)
        self.assertEqual(str(c), 'Circle with radius: 4.000000')

    def test_step6_repr(self):
        c = Circle(4)
        self.assertEqual(repr(c), 'Circle(4)')

    def test_step7(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual(c1 + c2, Circle(6))
        self.assertEqual(c2 * 3, Circle(12))

    def test_step8(self):
        c1 = Circle(2)
        c2 = Circle(3)
        self.assertFalse(c1 > c2)
        self.assertTrue(c1 < c2)
        c3 = Circle(3)
        self.assertEqual(c2, c3)

    def test_iadd(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c1 += c2
        self.assertEqual(c1, Circle(6))

    def test_imul(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c1 *= c2
        self.assertEqual(c1, Circle(8))

if __name__ == '__main__':
    unittest.main()
