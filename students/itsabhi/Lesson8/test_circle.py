import circle
import unittest
from unittest.mock import patch
import math
import os


class CircleTestCases(unittest.TestCase):

    def setUp(self):
        self.test_circle= circle.Circle(2)
        #self.radius = 0

    def setUp_other(other):
        other.test_circle= circle.Circle(4)

    def test_init(self):
        # Tests that circle is initiated with a value greater than 0
        result = self.test_circle.radius
        self.assertGreater(result, 0)

    def test_diameter(self):
        # Test Step 2
        result = self.test_circle.diameter
        self.assertEqual(4, result)

    def test_diameter_setter(self):
        # Test Step 3
        diam = 3
        self.test_circle.radius = diam/2
        result_radius = self.test_circle.radius
        self.assertEqual(1.5, result_radius)
        self.assertEqual(3, diam)

    def test_area_setter(self):
        # Test Step 4: area cannot be set
        circle_area = 20
        with self.assertRaises(AttributeError):
            self.test_circle.area = circle_area

    def test_area_calc(self):
        # Test Step 4: Test area calculation
        result = (self.test_circle.radius**2)*math.pi
        self.assertAlmostEqual(result, 12.5663706, 4) # Tests to 4 places

    def test_class_method(cls):
        # Test Step 5: Tests class method from_diameter returns a Circle class object
        result = circle.Circle.from_diameter(10)
        cls.assertIsInstance(result, circle.Circle)

    def test_dunder_str_method(self):
        self.assertEqual("Circle with radius: 2", circle.Circle.__str__(self.test_circle))

    def test_dunder_repr_method(self):
        self.assertEqual("Circle(2)", circle.Circle.__repr__(self.test_circle))

    def test_dunder_add_method(self):
        test_circle2 = circle.Circle(4)
        result = self.test_circle + test_circle2
        self.assertEqual("Circle(6)", result)

    def test_dunder_mul_method(self):
        result = self.test_circle*3
        self.assertEqual("Circle(6)", result)

    def test_dunder_gt_method(self):
        test_circle2 = circle.Circle(4)
        self.assertEqual(False, self.test_circle > test_circle2)

    def test_dunder_lt_method(self):
        test_circle2 = circle.Circle(4)
        self.assertEqual(True, self.test_circle < test_circle2)

    def test_dunder_eq_method(self):
        test_circle2 = circle.Circle(2)
        self.assertEqual(True, self.test_circle == test_circle2)

    def test_sort_key_method(self):
        circles =[circle.Circle(1), circle.Circle(3), circle.Circle(2), circle.Circle(1.99)]
        circles.sort(key=circle.Circle.sort_key)
        self.assertListEqual([circle.Circle(1), circle.Circle(1.99), circle.Circle(2), circle.Circle(3)], circles)


if __name__ == '__main__':
    unittest.main()
