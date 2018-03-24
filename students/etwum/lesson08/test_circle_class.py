from unittest import TestCase
from circle_class import Circle


class TestCircle(TestCase):

    def test_radius(self):
        c = Circle(3)
        self.assertEqual(c.radius, 3)

    def test_diameter(self):
        c = Circle(3)
        self.assertEqual(c.diameter, 6)

    def test_area(self):
        c = Circle(3)
        self.assertEqual(c.area, 28.274333882308138)

    def test_alternate_diameter(self):
        c = Circle.get_diameter(6)
        self.assertEqual(c.radius, 3)
        self.assertEqual(c.diameter, 6)

    def test_repr(self):
        c = Circle(3)
        self.assertEqual(repr(c), 'Circle(3)')

    def test_str(self):
        c = Circle(3)
        self.assertEqual(str(c), "Circle with radius: 3.0")