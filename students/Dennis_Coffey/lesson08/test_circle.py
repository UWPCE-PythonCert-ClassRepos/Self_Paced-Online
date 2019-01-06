# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 22:06:28 2018

@author: dennis

"""
import pytest

# importing the circle code.
from circle import Circle

# Test circle radius set and get - Step 1
def test_circle_radius():
    c = Circle(4)
    assert c.radius == 4

# Test circle diameter get - Step 2
def test_circle_diameter_get():
    c = Circle(4)
    assert c.diameter == 8
    assert c.diameter == c.radius * 2
    
# Test circle diameter set - Step 3
def test_circle_diameter_set():
    c = Circle(4)
    c.diameter = 4
    assert c.diameter == 4.0
    assert c.radius == 2.0

# Test area get - Step 4
def test_circle_area_get():
    c = Circle(2)
    assert c.area == 12.566371
    
# Test alternate constructor from_diameter - Step 5
def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8.0
    assert c.radius == 4.0

# Test __str__ method - Step 6
def test_str_method():
    c = Circle(4)
    assert c.__str__() == 'Circle with radius: 4.000000'

# Test __repr__ method - Step 6
def test_repr_method():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'
    
# Test eval of __repr__ method - Step 6
def test_eval_repr_method():
    c = Circle(4)
    d = eval(repr(c))
    assert d.__str__() == 'Circle with radius: 4.000000'
    assert d.radius == 4.0

# Test add override method - Step 7
def test_add_override_method():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 + c2).radius == 6.0

# Test multiplication override method - Step 7
def test_mul_override_method():
    c1 = Circle(4)
    c1 * 3
    assert c1.radius == 12.0

# Test comparison methods - Step 8
def test_comparison_methods():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(2)
    assert(c1 < c2) # Test less than
    assert(c1 <= c2) # Test less than equal
    assert(c1 <= c3) # Test less than equal
    assert(c2 > c3) # Test greater than
    assert(c2 >= c3) # Test greater than equal
    assert(c1 == c3) # Test equal
    
# Test comparison methods by sorting circle list - Step 8
def test_sort_circle_list():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
