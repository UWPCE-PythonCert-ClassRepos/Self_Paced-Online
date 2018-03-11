import unittest
from circle import Circle
from math import pi

class TestCircle(unittest.TestCase):

    def test_radius(self):
        c = Circle(2)
        self.assertEqual(c.radius, 2)

    def test_diameter(self):
        c = Circle(2)
        self.assertEqual(c.diameter, 4)

    def test_return_radius(self):
        c = Circle(6)
        self.assertEqual(c.diameter, 12)
        c.diameter = 4
        self.assertEqual(c.radius, 2.0)

    def test_area(self):
        c = Circle(2)
        self.assertAlmostEqual(c.area, 2**2*pi)
        with self.assertRaises(AttributeError):
            c.area = 42
            print("You can't set the area.  This is Read-Only.")

    def test_from_diameter(self):
        c = Circle(4)
        c.from_diameter(8)
        self.assertEqual(c.diameter, 8.0)
        self.assertEqual(c.radius, 4)

    def test_str(self):
        c = Circle(4)
        self.assertEqual(str(c), 'Circle with radius: 4')

    def test_repr(self):
        c = Circle(4)
        self.assertEqual(repr(c), 'Circle(4)')

    def test_operator(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual(c1 + c2, 'Circle(6)')
        self.assertEqual(c1 * 4, 'Circle(8)')

    def test_compare(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertTrue(c1 < c2)
        self.assertFalse(c2 < c1)
        self.assertNotEqual(c1, c2)

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
