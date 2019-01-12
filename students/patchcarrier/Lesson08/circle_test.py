import circle as circle
import pytest as pt
import math
import numpy as np

def test_1():
    """Create a circle with a radius attribute."""
    
    c = circle.Circle(4)
    assert c.radius == 4
    c.radius = 5
    assert c.radius == 5
    
    # Non integer values used to initialize radius
    c1 = circle.Circle("3.14")
    c2 = circle.Circle(4.21)
    c3 = circle.Circle(2.3e6)
    
    # Verify that the circle only accepts radius inputs that can be 
    # converted to floats
    with pt.raises((TypeError, ValueError)):
        c4 = circle.Circle("bologna")
    with pt.raises((TypeError, ValueError)):
        c5 = circle.Circle(2+4j)
    
    
def test_diameter():
    """Check that changing Circle.radius updates Circle.diameter and vice versa."""
    
    # Check that changing Circle.radius updates Circle.diameter
    rad = 3.45
    c = circle.Circle(rad)
    assert c.radius == rad
    assert c.diameter == 2 * c.radius
    
    # Check that changing Circle.diameter updates Circle.radius
    diam = 6.71
    c.diameter = diam
    assert c.diameter == diam
    assert c.radius == c.diameter / 2
    

def test_area():    
    """Test that Circle.area is calculated appropriately."""
    
    # Check that the area is computed appropriately
    rad = 5.82312
    c = circle.Circle(rad)
    assert c.area == math.pi * c.radius**2
    
    rad = 8219.23
    c.radius = rad
    assert c.area == math.pi * c.diameter**2 / 4
    
    # Verify that the area cannot be changed by the user
    with pt.raises(AttributeError):
        c.area = 52
     
        
def test_diameter_constructor():
    """Test the diameter constructor of circle.Circle."""
    
    diam = 8.324
    c = circle.Circle.from_diameter(diam)
    # Verify that an instance object is created from the alternate constructor
    assert isinstance(c, circle.Circle)
    # Verify that the radius and diameter are set correctly
    assert c.radius == diam / 2
    assert c.diameter == diam
    
    
def test_string_representations():
    """Ensure that Circle.__repr__ and Circle.__str__ return the proper strings
    without raising exceptions."""
    
    c1 = circle.Circle(34.34)
    c2 = circle.Circle.from_diameter(34.34)
    str_start = "Circle with radius ="
    repr_start = "Circle("
    
    # Informal string representation:
    assert str(c1)[:len(str_start)] == str_start
    # Check that the radius printed by the informal string is correct:
    assert float(str(c1)[len(str_start):]) == c1.radius
    
    # Formal string representation:
    assert repr(c2)[:len(repr_start)] == repr_start
    assert float(repr(c2)[len(repr_start) : -1]) == c2.radius
    assert repr(c2)[-1] == ")"
    
    
def test_addition_multiplication():
    """Test the addition and multiplication operators are overloaded properly
    for the circle class."""
    
    r1 = 4.2345
    r2 = 345.123
    c1 = circle.Circle(r1)
    c2 = circle.Circle(r2)
    
    # Verify that addition of two circles returns a new instance of Circle
    # and that addition is commutative
    c3 = c1 + c2
    c4 = c2 + c1
    assert isinstance(c3, circle.Circle)
    assert isinstance(c4, circle.Circle)
    assert not (c3 is c1)
    assert not (c3 is c2)
    assert not (c4 is c1)
    assert not (c4 is c2)
    assert c3.radius == (r1 + r2)
    assert c3.radius == c4.radius
    
    # Verify that multiplication of a circle with a scalar returns a new instance
    # of Circle and that multiplication is associative
    c5 = 3.2*c1
    c6 = c1*3.2
    assert not (c5 is c1)
    assert not (c6 is c1)
    assert c5.radius == c6.radius
    
def test_comparison():
    """Test the ability to compare two circles and sort a list of circles."""
    
    c1 = circle.Circle(4)
    c2 = circle.Circle(4.001)
    # c2 and c3 should be equal. Add some other random instance attributes to 
    # c3 just for fun
    c3 = circle.Circle(4.001)
    c3.radius2 = 4.2
    c3.radius3 = 4.05
    
    # Comparison on two unequal circles
    assert c1 < c2
    assert c1 <= c2
    assert c2 > c1
    assert c2 >= c1
    assert c1 != c2
    
    # Comparison on two equal circles
    assert c2 == c3
    assert c2 >= c3
    assert c2 <= c3
    
    # Test sorting just using the less than operator
    clist = [circle.Circle(np.int64(45)), circle.Circle(45), circle.Circle(0.01),
             circle.Circle(1e2), circle.Circle(5.55)]
    clist.sort()
    assert clist[0].radius == 0.01
    assert clist[1].radius == 5.55
    assert clist[2].radius == 45
    assert clist[3].radius == 45
    assert clist[4].radius == 100
    
    # Test sorting using the key method
    clist2 = [circle.Circle(5), circle.Circle(1), circle.Circle(4), 
              circle.Circle(3.5)]
    clist2_sorted = sorted(clist2, key=circle.Circle.sort_key)
    for l_circ, r_circ in zip(clist2_sorted[:-1], clist2_sorted[1:]):
        assert l_circ < r_circ
     