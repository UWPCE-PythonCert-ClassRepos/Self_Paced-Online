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

    def test_from_diameter(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.radius, 4)
        self.assertEqual(c.diameter, 8)

    def test_str(self):
        c = Circle(4)
        self.assertEqual(str(c), "Circle with radius: 4")

    def test_repr(self):
        c = Circle(4)
        self.assertEqual(repr(c), "Circle(4)")
        self.assertEqual(type(eval(repr(c))),type(Circle(4)))

    def test_add(self):
        c = Circle(4)
        d = Circle(6)
        e = c + d
        self.assertEqual(e.radius, 10)

    def test_mul(self):
        c = Circle(4)
        d = c * 3
        self.assertEqual(d.radius,12)

    def test_rmul(self):
        c = Circle(4)
        d = 3 * c
        self.assertEqual(d.radius,12)

    def test_gt_lt(self):
        c1 = Circle(4)
        c2 = Circle(5)
        self.assertEqual(c1 > c2,False)    
        self.assertEqual(c1 < c2, True)
        self.assertEqual(c1 == c2, False)

        c3 = Circle(4)
        self.assertEqual(c1 == c3, True)

    def test_sort(self):
        circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
        circles.sort()
        self.assertEqual(circles,[Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)])

    def test_reflected(self):
        c = Circle(2)
        self.assertEqual(c * 3,3 * c)

    def test_div(self):
        c = Circle(4)
        d = c / 2
        self.assertEqual(d.radius, 2)

    def test_aug_add(self):
        c = Circle(4)
        c += 6
        self.assertEqual(c.radius, 10)

    def test_aug_subtract(self):
        c = Circle(4)
        c -= 2
        self.assertEqual(c.radius,2)

    def test_aug_mul(self):
        c = Circle(9)
        c *= 2
        self.assertEqual(c.radius, 18)

if __name__ == '__main__':
    unittest.main() 
