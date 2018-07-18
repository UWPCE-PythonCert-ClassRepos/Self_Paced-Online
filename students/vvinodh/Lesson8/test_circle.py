import circle as c
import unittest
import math


class test_circle(unittest.TestCase):

    # step 1
    def test_radius(self):
        test = c.Circle(5)
        self.assertEqual(test.radius, 5)

    # step 2
    def test_diameter(self):
        test = c.Circle(5)
        self.assertEqual(test.diameter, 10)

    # step 3
    def test_set_diameter(self):
        test = c.Circle(5)
        test.diameter = 20
        self.assertEqual(test.diameter, 20)
        self.assertEqual(test.radius, 10)

    # step 4
    def test_area(self):
        test = c.Circle(5)
        self.assertEqual(test.area, math.pi * math.pow(5, 2))

    # step 5
    def test_from_diameter(self):
        test = c.Circle.from_diameter(10)
        self.assertEqual(test.radius, 5)

    # step 6.1
    def test_str(self):
        test = c.Circle(5)
        self.assertEqual(str(test), "Circle with a radius of 5.")

    # step 6.2
    def test_rpr(self):
        test = c.Circle(5)
        self.assertEqual(repr(test), "Circle(5)")

    # step 7.1
    def test_add(self):
        test1 = c.Circle(2)
        test2 = c.Circle(4)
        self.assertEqual(test1 + test2, c.Circle(6))

    # step 7.2
    def test_mult(self):
        test = c.Circle(4)
        num = 3
        self.assertEqual(test * num, c.Circle(12))

    # step 8.1
    def test_gt(self):
        c1 = c.Circle(2)
        c2 = c.Circle(4)
        self.assertFalse(c1 > c2)

    # step 8.2
    def test_ls(self):
        c1 = c.Circle(2)
        c2 = c.Circle(4)
        self.assertTrue(c1 < c2)

    # step 8.3
    def test_eq(self):
        c1 = c.Circle(4)
        c2 = c.Circle(4)
        self.assertEqual(c1, c2)

    # step 8.4
    def test_ne(self):
        c2 = 3
        c3 = 4
        self.assertTrue(c2 != c3)

    # step 8.5
    def test_sort(self):
        circ1 = c.Circle(8)
        circ2 = c.Circle(7)
        circ3 = c.Circle(6)
        circ4 = c.Circle(5)
        circ_list = [circ1, circ3, circ2, circ4]
        circ_list.sort()
        self.assertEqual(str(circ_list),
                         '[Circle(5), Circle(6), Circle(7), Circle(8)]')


if __name__ == '__main__':
    unittest.main()
