#Circle Class Test

import unittest
from circle_class import Circle


class TestCircle(unittest.TestCase):
    """Write a full suite of tests."""
    
    def test_step_1(self):
        """Test step 1."""
        
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_step_2(self):
        """Test step 2."""
        
        c = Circle(4)
        self.assertEqual(c.diameter, 8)
        
    def test_step_3(self):
        """Test step 3."""
        
        c = Circle(4)
        self.assertEqual(c.diameter, 8)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        self.assertEqual(c.radius, 1)
        
    def test_step_4(self):
        """Test step 4."""
        
        c = Circle(2)
        self.assertEqual(c.area, 12.566370614359172)
        
    def test_step_5(self):
        pass

if __name__ == "__main__":
    unittest.main()