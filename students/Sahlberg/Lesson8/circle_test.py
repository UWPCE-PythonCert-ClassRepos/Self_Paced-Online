import unittest as u
from Circle import *
from io import StringIO
c = Circle(4)

print(c.radius)

class test_circle(u.TestCase):

    def test_radius(self):
        c = Circle(4)
        self.assertEqual(4,c.radius)

    def test_diam(self):
        c = Circle(4)
        self.assertEqual(8,c.diameter)

    def test_area(self):
        c = Circle(4)
        self.assertEqual(50.2655, c.area)


    def test_diameter_set(self):
        d = Circle.from_diameter(10)
        self.assertEqual(10,d.diameter)
        self.assertEqual(5,d.radius)

    def test_string(self):
        self.assertEqual(f'Circle with radius: {6:.6f}', str(Circle(6)))

    def test_rep(self):
        self.assertEqual(f'Circle({6:.0f})', repr(Circle(6)))

    def test_addition(self):
        self.assertEqual(Circle(6), Circle(2) + Circle(4))

    def test_multiply(self):
        self.assertEqual((Circle(6) * 2), Circle(12))
        self.assertEqual((2 * Circle(6)), Circle(12))

    def test_less_than(self):
        self.assertEqual(Circle(2) < Circle(66), True)
        self.assertEqual(Circle(2) > Circle(66), False)

    def test_great_than(self):
        self.assertEqual(Circle(22) > Circle(6), True)
        self.assertEqual(Circle(22) > Circle(66), False)
    def test_equality(self):
        self.assertEqual(True, True)
        self.assertEqual(Circle(6), Circle(6))
        self.assertEqual(Circle(6), (Circle(2) + Circle(4)))

if __name__ == '__main__':
    u.main()
