# Jon Cracolici
# UW- Python Cert
# Lesson 08 - Circle Class Testing Suite


# Import statements
from Circle import Circle
import math
import unittest


class Test_circle(unittest.TestCase):
    """The class of unittests for the Circle Class Exercise."""

    # Property Tests - Tasks 1-3
    def test_init(self):
        """Tests the initialization of the Circle Class.
        """
        c = Circle(4)
        self.assertEqual(c.radius, 4)
        self.assertEqual(c.diameter, 8)


    def test_rd_setters(self):
        """Tests the ability to set radius and diameter."""
        c = Circle(4)
        c.radius = 3
        self.assertEqual(c.radius, 3)
        self.assertEqual(c.diameter, 6)
        c.diameter = 10
        self.assertEqual(c.radius, 5)
        self.assertEqual(c.diameter, 10)
    
    
    def test_area(self):
        """Tests the area property. Task 4."""
        c = Circle(4)
        self.assertEqual(c.area, math.pi * 16)


    def test_alt_init(self):
        """Tests alternative initializer (diameter).
        Task 5."""
        c1 = Circle.from_diameter(4)
        self.assertEqual(c1.radius, 2)
        self.assertEqual(c1.diameter, 4)


    # Printing Tests
    def test_strings(self):
        """Tests the printing behavior. Task 6."""
        c1 = Circle(2)
        c1_repr=  c1.__repr__()
        c1_str = c1.__str__()
        correct_str = 'A circle with radius 2.00.'
        correct_repr = 'Circle (2.00)'
        self.assertEqual(c1_repr, correct_repr)
        self.assertEqual(c1_str, correct_str)


    # Math Functionality Tests - Task 7
    def test_addition(self):
        """Tests addition."""
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = Circle(6)
        c4 = c1 + c2
        self.assertEqual(c3, c4)
    
    
    def test_multiplication(self):
        """"Tests multiplication"""
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = Circle(8)
        c4 = c1 * c2
        self.assertEqual(c3, c4)

    #Comparison Tests - Task 8
    def test_comparisons(self):
        c1 = Circle(2)
        c2 = Circle(3)
        c3 = Circle(2)
        self.assertEqual((c1>c2),False)
        self.assertEqual((c1<c2), True)
        self.assertEqual((c1==c2), False)
        self.assertEqual((c1==c3), True)


    #list sort tests - Task 8
    def test_sorting(self):
        c1 = Circle(1)
        c2 = Circle(2)
        c3 = Circle(3)
        c4 = Circle(4)
        c5 = Circle(5)
        presorted = [c1,c2,c3,c4,c5]
        unsorted = [c3,c5,c1,c2,c4]
        unsorted.sort(reverse=False)
        self.assertEqual(presorted, unsorted)

    
if __name__ == '__main__':
    unittest.main()