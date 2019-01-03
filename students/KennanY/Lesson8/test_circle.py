import unittest
import math
import CircleClass

class Test_Circle(unittest.TestCase):

    def test_area_for5(self):
        radius = 5
        actual=math.pi*radius**2
        c=CircleClass.Circle(radius)
        expected=c.area
        self.assertEqual(actual,expected)

    def test_print_Circle(self):
        radius=3
        expected='Circle with radius 3'
        c = CircleClass.Circle(radius)
        actual = c.__str__()
        self.assertEqual(actual, expected)

    def test_add_circles(self):
        c1=CircleClass.Circle(6)
        c2=CircleClass.Circle(3)
        actual=c1+c2
        expected=CircleClass.Circle(9)
        self.assertEqual(actual._radius,actual._radius)

    def test_less_than(self):
        c1 = CircleClass.Circle(6)
        c2 = CircleClass.Circle(9)
        self.assertTrue(c1 < c2)

    def test_greater_than(self):
        c1 = CircleClass.Circle(7)
        c2 = CircleClass.Circle(4)
        self.assertTrue(c1 > c2)

    def test_equal(self):
        c1 = CircleClass.Circle(12)
        c2 = CircleClass.Circle(12)
        self.assertTrue(c1 == c2)

    def test_sort(self):
        actual = [CircleClass.Circle(9), CircleClass.Circle(2), CircleClass.Circle(3)]
        expected = [CircleClass.Circle(2), CircleClass.Circle(3), CircleClass.Circle(9)]
        actual.sort()
        self.assertEqual(actual, expected)

if __name__=="__main__":
    unittest.main()