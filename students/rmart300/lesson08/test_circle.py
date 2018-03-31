import unittest
from circle import Circle

class TestCircle(unittest.TestCase):

    def test_get(self):
        c = Circle(50)
        assert c.radius == 50

    def test_set(self):
        c = Circle(50)
        c.radius = 80
        assert c.radius == 80


if __name__ == '__main__':
    unittest.main() 
