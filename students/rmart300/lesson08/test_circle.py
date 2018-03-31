import unittest
from circle import Circle

class TestCircle(unittest.TestCase):

    def test_get_radius(self):
        c = Circle(50)
        self.assertEqual(c.radius,50)

    def test_set_radius(self):
        c = Circle(50)
        c.radius = 80
        self.assertEqual(c.radius,80)

    def test_get_diameter(self):
        c = Circle(50)
        self.assertEqual(c.diameter,100)

    def test_set_diameter(self):
        c = Circle(50)
        c.diameter = 100
        self.assertEqual(c.diameter,100)
        self.assertEqual(c.radius,50)

    def test_get_area(self):
        c = Circle(2)
        self.assertEqual("%.2f" % c.area,'12.57')

    def test_set_area(self):
        c = Circle(2)
        with self.assertRaises(AttributeError):
            c.area = 10

if __name__ == '__main__':
    unittest.main() 
