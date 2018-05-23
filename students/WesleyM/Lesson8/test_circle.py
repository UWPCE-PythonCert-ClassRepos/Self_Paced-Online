import unittest
import circle
import math

class TestCircle(unittest.TestCase):

    def test_radius(self):
        c = circle.Circle(4)
        self.assertEqual(c.radius, 4)
    
    def test_diameter(self):
        c = circle.Circle(4)
        self.assertEqual(c.diameter, 8)

    def test_diameter_set(self):
        c = circle.Circle(4)
        c.diameter = 2
        self.assertEqual(c.radius, 1)
    
    def test_area(self):
        c = circle.Circle(2)
        self.assertEqual(c.area, 2*2*math.pi)
    
    def test_diameter_alternate(self):
        c = circle.Circle(4)
        c.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius, 4)
    
    def test_str(self):
        c = circle.Circle(4)
        self.assertEqual(str(c), 'Circle with radius: 4')
        
    def test_repr(self):
        c = circle.Circle(4)
        self.assertEqual(repr(c), 'Circle(4)')
    
    def test_numeric(self):
        c1 = circle.Circle(2)
        c2 = circle.Circle(4)
        
        x = c1 + c2
        self.assertEqual(x.radius, 6)
        self.assertIsInstance(x, circle.Circle)
        y = c2 * 3
        
        self.assertEqual(y.radius, 12)
        self.assertIsInstance(y, circle.Circle)
    
    def test_comparison(self):
        c1 = circle.Circle(2)
        c2 = circle.Circle(4)
        
        self.assertTrue(c1 < c2)
        self.assertFalse(c1 > c2)
        self.assertNotEqual(c1, c2)
        
        c3 = circle.Circle(4)
        self.assertEqual(c2, c3)
    
    
    def test_sort(self):
        circles = [circle.Circle(6), circle.Circle(7), circle.Circle(8), circle.Circle(4), circle.Circle(0), circle.Circle(2), circle.Circle(3), circle.Circle(5), circle.Circle(9), circle.Circle(1)]
        self.assertEqual(sorted(circles), [circle.Circle(0), circle.Circle(1), circle.Circle(2), circle.Circle(3), circle.Circle(4), circle.Circle(5), circle.Circle(6), circle.Circle(7), circle.Circle(8), circle.Circle(9)])

if __name__ == "__main__":
    unittest.main()
