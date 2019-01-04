"""Code to test circle class"""

#step 1: create as class called circle with an instance attribute
#for the radius

import sys
import io
import pytest
import math
#sys.path.append("C:\\Users\\Jared\\Documents\\IntroToPython\\Self_Paced-Online\\students\\jared_mulholland\\lesson_8")
from circle_class import *

def test_radius_circle():
    """Test that radius entered will be reflected in new instance"""
    c = Circle_1(4)
    assert c.radius == 4

    c.radius = 6
    assert c.radius == 6

#step 2: create property for diameter
def test_diameter():
    """tests that diameter can be set as a property"""
    c = Circle_2(4)
    assert c.diameter == 8

#step 3: create property that allows you to set diameter and change radius
def test_diameter_radius():
    """test that changing diameter value will also change radius"""
    c = Circle_3(4)
    c.diameter = 6
    assert c.radius == 3


#Step 4:
"""Add an area property so the user can get the area of the circle"""

def test_area():
    """test that correct area made"""
    c = Circle_4(4)
    assert c.area == math.pi * 4**2
    with pytest.raises(AttributeError):
        c.area = 42
        
#Step 5:
"""Add an alternate constructor that lets 
the user create a Circle directly with the diameter:"""

def test_area_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

#Step 6:
"""add __str__ and __repr__ method to circle class"""
def test_rep_str():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'
    assert str(c) == 'Circle with radius: 4'

    



