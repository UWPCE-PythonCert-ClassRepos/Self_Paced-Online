from unittest import TestCase
from circle_class import Circle


class TestCircle(TestCase):

    def test_radius(self):
        c = Circle(3)
        self.assertEqual(c.radius, 3)

    def test_diameter(self):
        c = Circle(3)
        self.assertEqual(c.diameter, 6)
