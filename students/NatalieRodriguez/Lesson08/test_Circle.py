from Circle import *
import pytest
from math import *

a = Circle(10)
b = Circle(5)
c = Circle(2)
d = Circle(1)

def getter_test():
    assert a.radius == 10
    assert b.radius == 5
    assert c.radius == 2
    assert d.radius == 1
    assert a.diameter == 20
    assert b.diameter == 10
    assert c.diameter == 4
    assert d.diameter == 2

def setter_test():
    a.diameter = 10
    assert a.diameter == 10
    assert a.radius == 5
    a.radius = 5
    assert a.diameter == 10
    assert a.radius == 5

def area_test():
    assert a.area == pi*100
    assert b.area == pi*25
    assert c.area == pi*4

def init_diameter_test():
    aa = Circle.from_diameter(8)
    ab = Circle.from_diameter(7)
    ac = Circle.from_diameter(6)
    assert aa.radius == 4
    assert ab.radius == 3.5
    assert ac.radius == 3
    assert aa.diameter == 8
    assert ab.diameter == 7
    assert ac.diameter == 6

def str_repr_test():
    assert str(a) == "Circle with radius: " + str(a.radius)
    assert str(b) == "Circle with radius: " + str(b.radius)
    assert repr(a) == 'Circle(12)'
    assert repr(b) == 'Circle(1)'

def add_multiple_test():
    assert repr(a + b) == "Circle(15)"
    assert repr(a * 3) == "Circle(30)"
    assert repr(3 * a) == "Circle(30)"
    assert a * 3 == 3 * a

def compare_test():
    assert a > b
    assert b < a
    assert a == Circle(10)
    assert b == b
    assert a != b
    assert a >= b
    assert b <= a

def len_circumference_test():
    assert len(a) == round(2 * pi * 10)
    assert a.circumference == 2 * pi * 10
    assert len(a) == round(a.circumference)
    assert len(b) == round(2 * pi)
    assert b.circumference == 2 * pi

def aug_operators_test():
    ba = Circle(16)
    bb = Circle(20)
    ba += bb
    bb *= 2
    assert ba == Circle(42)
    assert bb == Circle(40)
    assert bb/2 == Circle(20)