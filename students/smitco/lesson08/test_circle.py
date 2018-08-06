# lesson 08 circle test file
# !/usr/bin/env python3
# utilizes pytest


import pytest
from circle import *

def test_circle_class():
    c = Circle(4)
    assert c.radius == 4

def test_no_radius():
    with pytest.raises(TypeError):
        c = Circle()

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_change_radius():
    c = Circle(4)
    c.radius = 9
    assert c.diameter == 18

def test_change_diameter():
    c = Circle(4)
    c.diameter = 14
    assert c.radius == 7

def test_zero_limit():
    with pytest.raises(ValueError):
        c = Circle(0)
    with pytest.raises(ValueError):
        c = Circle(4)
        c.diameter = -10
    with pytest.raises(ValueError):
        c = Circle(4)
        c.radius = -8

def test_area():
    c = Circle(4)
    assert round(c.area, 1) == 50.3
    with pytest.raises(AttributeError):
        c.area = 35

def test_alt_constr():
    c = Circle.from_diameter(14)
    assert c.radius == 7

def test_repr():
    c = Circle(6)
    assert repr(c) == "Circle(6.0)"

def test_str():
    c = Circle(6)
    assert "r = 6.0" and "d = 12.0" in str(c) 

def test_add_circles():
    c1 = Circle(4)
    c2 = Circle(6)
    c1 += c2
    assert c1.radius == 10


def test_mult_circle():
    c = Circle(5)
    c *= 3
    assert c.radius == 15

    
def test_circle_comp():
    c1 = Circle(4)
    c2 = Circle(6)
    c3 = Circle(6)
    assert (c1 < c2) == True
    assert (c1 > c2) == False
    assert (c1 == c2) == False
    assert (c2 == c3) == True

def test_sorted_list():
    c1 = Circle(5)
    c2 = Circle(6)
    c3 = Circle(2)
    c4 = Circle(3)
    c5 = Circle(7)
    circles = [c1, c2, c3, c4, c5]
    circles.sort()
    assert circles == [c3, c4, c1, c2, c5]

def test_bckwrd_mult():
    c = Circle(5)
    c = 3 * c
    assert c.radius == 15

def test_div_circle():
    c = Circle(6)
    c = c / 3
    assert c.radius == 2

def test_sub_circles():
    c1 = Circle(6)
    c2 = Circle(4)
    c1 -= c2
    assert c1.radius == 2
    with pytest.raises(ValueError):
        c1 = Circle(4)
        c2 = Circle(6)
        c1 -= c2
    