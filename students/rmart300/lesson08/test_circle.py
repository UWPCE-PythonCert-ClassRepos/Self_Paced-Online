import unittest
from circle import Circle

class TestCircle(unittest.TestCase):

    def test_get_radius(self):
        c = Circle(50)
        assert c.radius == 50

    def test_set_radius(self):
        c = Circle(50)
        c.radius = 80
        assert c.radius == 80

    def test_get_diameter(self):
        c = Circle(50)
        assert c.diameter == 100

    def test_set_diameter(self):
        c = Circle(50)
        c.diameter = 100
        assert c.diameter == 100
        assert c.radius == 50

if __name__ == '__main__':
    unittest.main() 
