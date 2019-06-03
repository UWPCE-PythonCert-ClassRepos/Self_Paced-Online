#Circle Class Test

import unittest
from circle_class import Circle
from circle_class import Sphere

class TestCircle(unittest.TestCase):
    """Write a full suite of tests."""
    
    def test_step_1(self):
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_step_2(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)
        
    def test_step_3(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        self.assertEqual(c.radius, 1)
        
    def test_step_4(self): 
        c = Circle(2)
        self.assertEqual(c.area, 12.566370614359172)
        
    def test_step_5(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius, 4)

    def test_step_6(self):
        c = Circle(4)
        self.assertEqual(str(c), "Circle with radius: 4")
        self.assertEqual(repr(c), "Circle(4)")
    
    def test_step_7(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual(c1 + c2, Circle(6))
        self.assertEqual(c2 * 3, Circle(12))
        self.assertEqual(3 * c2, Circle(12))
    
    def test_step_8(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = Circle(4)
        self.assertEqual(c1 > c2, False)
        self.assertEqual(c1 < c2, True)
        self.assertEqual(c1 == c2, False)
        self.assertEqual(c2 == c3, True)
        circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
        circles.sort()
        expected = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
        self.assertEqual(circles, expected)
    
    def test_step_8_optional(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c1 += c2
        c2 *= 2
        self.assertEqual(c1, Circle(6))
        self.assertEqual(c2, Circle(8))
    
    def test_step_9(self):
        s1 = Sphere(4)
        s2 = Sphere(5)
        s3 = Sphere.from_diameter(8)
        
        self.assertEqual(s1.radius, 4)
        self.assertEqual(s1.diameter, 8)
        
        self.assertEqual(s3.diameter, 8)
        self.assertEqual(s3.radius, 4)
        
        self.assertEqual(s1.area, 201.06192982974676)
        self.assertEqual(s1.volume, 268.082573106329)
        
        self.assertEqual(str(s1), "Sphere with radius: 4")
        self.assertEqual(repr(s1), "Sphere(4)")
        
        self.assertEqual(s1 + s2, Sphere(9))
        self.assertEqual(s2 * 3, Sphere(15))
        self.assertEqual(3 * s2, Sphere(15))
        
        self.assertEqual(s1 > s2, False)
        self.assertEqual(s1 < s2, True)
        self.assertEqual(s1 == s2, False)
        self.assertEqual(s1 != s2, True)
        
        spheres = [Sphere(3), Sphere(0), Sphere(2), Sphere(1)]
        spheres.sort()
        expected = [Sphere(0), Sphere(1), Sphere(2), Sphere(3)]
        self.assertEqual(spheres, expected)
        
        s1 += s2
        s2 *= 2
        self.assertEqual(s1, Sphere(9))
        self.assertEqual(s2, Circle(10))
        
if __name__ == "__main__":
    unittest.main()