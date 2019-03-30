from circle import Circle

import unittest


class test_circle(unittest.TestCase):

    c1 = Circle(2)
    c2 = Circle(4)

    def test_diameter(self):
        result = self.c1.diameter
        assert result == 4

    def test_area(self):
        result = self.c1.area
        assert result == 12.566370614359172

    def test_circle_repre(self):
        result = repr(self.c1)
        assert result == "Circle(2)"

    def test_circle_str(self):
        result = self.c1
        assert str(result) == "Circle with radius: 2"

    def test_circles_add(self):
        tc1 = Circle(3)
        tc2 = Circle(4)
        result =  tc1 + tc2
        assert result == "Circle(7)"

    def test_circle_less(self):
        tc1 = Circle(3)
        tc2 = Circle(4)
        assert tc1 < tc2

    def test_circle_grt(self):
        tc1 = Circle(3)
        tc2 = Circle(4)
        assert tc2 > tc1

    def test_circle_eq(self):
        tc3 = Circle(5)
        tc4 = Circle(5)
        assert tc3 == tc4












