"""test code for circle.py"""
# NEIMA SCHAFI, LESSON 8 Assignment - Circle Class

import pytest
import math
from circle import *

########
# Step 1 & 2
########


def test_init():
    """
    This tests if a proper numeric circle isinstance
    is created and then checks for correct
    radius and diameters
    """
    c = Circle(4)
    assert(c.radius == 4)
    assert(c.diameter == 8)

    c = Circle(4.5)
    assert(c.radius == 4.5)
    assert(c.diameter == 9)


########
# Step 3
########
"""tests if diameter setter properly works"""


def test_diameter():
    c = Circle(5)
    c.diameter = 6

    assert(c.radius == 3)
    assert(c.diameter == 6)

    c.diameter = 'string'


########
# Step 4
########
"""tests if area setter properly works"""


def test_area():
    c = Circle(5)

    assert(round(c.area, 2) == 78.54)

########
# Step 5
########
"""tests if alternate constuctor works properly"""


def test_from_diameter():
    c = Circle.from_diameter(8)

    assert(c.radius == 4)
    assert(c.diameter == 8)


########
# Step 6
########


def test_str():
    """Test proper string output of a circle"""
    c = Circle(4)

    assert(c.radius == 4)
    assert(c.diameter == 8)
    assert('Circle with radius: 4.000000' == c.__str__())


def test_repr():
    """Test representative value"""
    c = Circle(4)

    assert(c.radius == 4)
    assert(c.diameter == 8)
    assert('Circle(4)' == c.__repr__())


########
# Step 7
########

def test_add():
    """Test addition of circle radii"""
    c1 = Circle(2)
    c2 = Circle(4)

    assert(c1 + c2 == Circle(6))
    assert(c2 + c1 == Circle(6))


def test_mul():
    """Test multiplication of circle radius"""
    c1 = Circle(2)
    c2 = Circle(4)

    assert((c1 * 3) == Circle(6))
    assert((c2 * 3) != Circle(6))
    assert((c2 * 3) == Circle(12))


def test_imul():
    """Test multiplication when object is on right hand side"""
    c1 = Circle(2)
    c2 = Circle(4)

    assert((3 * c1) == Circle(6))
    assert((3 * c2) != Circle(6))
    assert((3 * c2) == Circle(12))


########
# Step 8
########

def test_gt():
    """Test > operator"""
    c1 = Circle(2)
    c2 = Circle(4)

    assert(c2 > c1)
    assert not(c1 > c2)


def test_lt():
    """Test < operator"""
    c1 = Circle(2)
    c2 = Circle(4)

    assert(c1 < c2)
    assert not(c2 < c1)


def test_eq():
    """Test < operator"""
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(2)

    assert(c1 == c3)
    assert(c1 * 3 == 3 * c1)
    assert not(c2 == c1)


def test_sort():
    """Test to see if Circle class is sortable"""
    circles = [Circle(3), Circle(6), Circle(2), Circle(1), Circle(8)]
    circles.sort()

    assert(circles == [Circle(1), Circle(2), Circle(3), Circle(6), Circle(8)])


def test_iadd():
    """Test augmented adding"""
    c1 = Circle(2)
    c2 = Circle(4)
    c1 += c2

    assert(c1.radius == 6)


def test_imul():
    """Test augmented multiplication"""
    c1 = Circle(2)
    c1 *= 2

    assert(c1.radius == 4)
