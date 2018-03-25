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

    def test_add(self):
        c = Circle(3)
        c2 = Circle(5)
        self.assertEqual(c+c2, 8)

    def test_mul(self):
        c = Circle(3)
        self.assertEqual(c*5, 15)

    def test_gt_lt(self):
        c = Circle(3)
        c2 = Circle(4)
        self.assertFalse(c > c2, False)
        self.assertTrue(c < c2, True)

    def test_equals(self):
        c = Circle(3)
        c2 = Circle(3)
        self.assertEqual(c == c2, True)

    def test_sort(self):
        c = Circle(3)
        c2 = Circle(4)
        c3 = Circle(2)

        list1 = [c,c3,c2]
        list1.sort()
        self.assertListEqual(list1, [Circle(2), Circle(3), Circle(4)])