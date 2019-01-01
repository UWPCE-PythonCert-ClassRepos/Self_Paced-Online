import unittest
from math import pi
from math import pow
from circle import Circle


class TestCircle(unittest.TestCase):

    # testing radius and diameter
    def test_accessors(self):
        test_radius = 2.5
        actual_radius = Circle(test_radius).radius
        expected_diameter = test_radius * 2
        actual_diameter = Circle(test_radius).diameter
        self.assertEqual(test_radius, actual_radius)
        self.assertEqual(expected_diameter, actual_diameter)


    def test_area(self):
        test_radius = 4
        expected_area = pi * pow(test_radius, 2)
        actual_area = Circle(test_radius).area
        self.assertEqual(expected_area, actual_area)


    def test_circle_from_diameter(self):
        expected_diameter = 9
        expected_radius = expected_diameter / 2
        # make a circle with diameter of 9, resulting Circle(4.5)
        actual_circle = Circle.circle_from_diameter(expected_diameter)
        #print(actual_circle)
        #print("radius = " , actual_circle.radius)
        #print("diameter = " , actual_circle.diameter)
        self.assertEqual(expected_radius, actual_circle.radius)
        self.assertEqual(expected_diameter, actual_circle.diameter)


    def test_str(self):
        test_radius = 9
        actual_circle = Circle(test_radius)
        #print(actual_circle)
        self.assertEqual(str(actual_circle), 'Circle with radius: 9')


    def test_repr(self):
        test_radius = 9
        actual_circle = Circle(test_radius)
        #print(actual_circle)
        self.assertEqual(repr(actual_circle), 'Circle(9)')


    def test_add(self):
        test_radius_1 = 2
        test_radius_2 = 9
        actual_circle_1_radius = Circle(test_radius_1).radius
        actual_circle_2_radius = Circle(test_radius_2).radius
        self.assertEqual(test_radius_1 + test_radius_2, actual_circle_1_radius + actual_circle_2_radius)


    def test_mul(self):
        test_radius = 9
        multiplier = 2
        expected_radius = test_radius * multiplier
        actual_radius_mul = Circle(test_radius).radius * multiplier
        actual_radius_rmul = multiplier * Circle(test_radius).radius
        self.assertEqual(expected_radius, actual_radius_mul)
        self.assertEqual(expected_radius, actual_radius_rmul)


    def test_eq(self):
        test_radius_1 = 9
        test_radius_2 = test_radius_1
        actual_circle_1_radius = Circle(test_radius_1).radius
        actual_circle_2_radius = Circle(test_radius_2).radius
        self.assertEqual(actual_circle_1_radius, actual_circle_2_radius)


    def test_neq(self):
        test_radius_1 = 9
        test_radius_2 = test_radius_1 + 2
        actual_circle_1_radius = Circle(test_radius_1).radius
        actual_circle_2_radius = Circle(test_radius_2).radius
        self.assertNotEqual(actual_circle_1_radius, actual_circle_2_radius)


    def test_lt(self):
        test_radius_1 = 9
        test_radius_2 = 23
        actual_circle_1_radius = Circle(test_radius_1).radius
        actual_circle_2_radius = Circle(test_radius_2).radius
        self.assertTrue(actual_circle_1_radius < actual_circle_2_radius)


    def test_gt(self):
        test_radius_1 = 9
        test_radius_2 = 23
        actual_circle_1_radius = Circle(test_radius_1).radius
        actual_circle_2_radius = Circle(test_radius_2).radius
        self.assertTrue(actual_circle_2_radius > actual_circle_1_radius)


    def test_sort(self):
        circle_1 = repr(Circle(1))
        circle_2 = repr(Circle(2))
        circle_3 = repr(Circle(3))
        circle_4 = repr(Circle(4))
        circle_5 = repr(Circle(5))
        crop_of_circles = [circle_4, circle_1, circle_3, circle_5, circle_2]
        #print(crop_of_circles)
        crop_of_circles.sort()
        #print(crop_of_circles)
        self.assertEqual(crop_of_circles, ['Circle(1)', 'Circle(2)', 'Circle(3)', 'Circle(4)', 'Circle(5)'])

if __name__ == '__main__':
    unittest.main()
