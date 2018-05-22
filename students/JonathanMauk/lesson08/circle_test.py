import unittest
from circle import Circle


class CircleTest(unittest.TestCase):

    def test_radius(self):
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_diameter(self):
        c = Circle(8)
        self.assertEqual(c.diameter, 16)

    def test_diameter2(self):
        c = Circle(6)
        c.diameter = 10
        self.assertEqual(c.radius, 5)


if __name__ == '__main__':
    unittest.main()
