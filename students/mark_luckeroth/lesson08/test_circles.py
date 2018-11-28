"""
test code for circles.py

"""

import pytest
import math
from random import shuffle

from circles import *

# Step 1&2
def test_init():
    the_radius = 10
    c = Circle(the_radius)
    assert c.radius == the_radius
    assert c.diameter == 2*the_radius

# Step 3

def test_properties():
    r_set = 10
    d_set = 5
    c = Circle(r_set)
    assert c.radius == r_set
    assert c.diameter == r_set*2
    c.diameter = d_set
    assert c.diameter == d_set
    assert c.radius == d_set/2
    c.radius = r_set
    assert c.radius == r_set
    assert c.diameter == r_set*2


# Step 4

def test_area():
    c = Circle(2)
    assert c.area == math.pi*2*2
    with pytest.raises(AttributeError):
        c.area = 42

# Step 5

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


# Step 6
def test_repr():
    c = Circle(2)
    assert repr(c) == 'Circle(2)'


def test_str():
    c = Circle(4)
    print(c)
    #assert False

# step 7

def test_numerics():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)
    assert c2*3 == Circle(12)
    assert c2 > c1
    assert c2 >= c1
    assert c2 != c1
    assert c1 < c2
    assert c1 <= c2

# Step 8

def test_sort():
    x = [Circle(i) for i in range(10)]
    y = x[:]
    shuffle(x)
    x.sort()
    assert x == y

