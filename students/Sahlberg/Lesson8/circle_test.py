import unittest as u

from Circle import *

c = Circle(4)

print(c.radius)

class test_circle(u.TestCase):
    from io import StringIO

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

if __name__ == '__main__':
    u.main()
