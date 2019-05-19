import pytest
from circle import *
import math


def test_circle_radius():
    assert(4 == Circle(4).radius)
    assert(2 == Circle(2).radius)
    with pytest.raises(ValueError):
        Circle(-1)

def test_circle_diameter():
    assert(8 == Circle(4).diameter)
    assert(4 == Circle(2).diameter)

def test_set_diameter():
    c = Circle(4)
    c.diameter = 12
    assert(c.diameter == 12)

def test_area():
    c = Circle(4)
    assert(c.area == math.pi*4*4)


def test_set_area():
    c = Circle(4)
    with pytest.raises(AttributeError):
        c.area = 5

def test_circle_from_diameter():
    c = Circle.from_diameter(8)
    assert(c.radius == 4)

def test_repr():
    assert(eval( repr( Circle(4))) == Circle(4))

def test_str():
    c = Circle(4)
    assert(str(c) == "Circle with radius: 4.000000")

def test_add():
    assert(Circle(4) == Circle(4))
    assert(Circle(4)+Circle(2) == Circle(6))

def test_multiply():
    assert(Circle(4)*2 == Circle(8))

def test_reverse_multiple():
    assert(2*Circle(4) == Circle(8))
