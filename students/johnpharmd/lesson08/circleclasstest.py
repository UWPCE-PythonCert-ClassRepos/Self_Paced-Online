import circle_class as cc
import unittest


class CircleTest(unittest.TestCase):
    """tests circle attributes"""

    def setUp(self):
        self.test = cc.Circle(5)

    def test_circle_radius(self):
        self.assertEqual(self.test.radius, 5)

    def test_circle_diameter(self):
        self.assertEqual(self.test.diameter, 10)
        self.test.diameter = 8
        self.assertEqual(self.test.diameter, 8)
        self.assertEqual(self.test.radius, 4)
