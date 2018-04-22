from circle import *
from pytest import *
from math import *

#Init Test
a = Circle(12)
b = Circle()
c = Circle(3)
d = Circle(5)

def test_getters():
    assert a.radius == 12
    assert b.radius == 1
    assert c.radius == 3
    assert d.radius == 5
    assert a.diameter == 24
    assert b.diameter == 2 
    assert c.diameter == 6
    assert d.diameter == 10

def test_setters():
    d.diameter = 14
    assert d.diameter == 14
    assert d.radius == 7
    d.radius = 14
    assert d.diameter == 28
    assert d.radius == 14

def test_area():
    assert a.area == pi*144
    assert b.area == pi*1
    assert c.area == pi*9

def test_init_from_diameter():
    aa = Circle.from_diameter(8)
    ab = Circle.from_diameter(7)
    ac = Circle.from_diameter(6)
    assert aa.radius == 4
    assert ab.radius == 3.5
    assert ac.radius == 3
    assert aa.diameter == 8
    assert ab.diameter == 7
    assert ac.diameter == 6

def test_str_repr():
    assert str(a) == "Circle with radius: " + str(a.radius)
    assert str(b) == "Circle with radius: " + str(b.radius)
    assert repr(a) == 'Circle(12)'
    assert repr(b) == 'Circle(1)'

def test_add_mult():
    assert repr(a + b) == "Circle(13)"
    assert repr(a * 3) == "Circle(36)"
    assert repr(3 * a) == "Circle(36)"
    assert a * 3 == 3 * a

def test_compare():
    assert a > b
    assert b < a
    assert a == Circle(12)
    assert b == b
    assert a != b
    assert a >= b
    assert b <= a

def test_len_circumference():
    assert len(a) == round(2 * pi * 12)
    assert a.circumference == 2 * pi * 12
    assert len(a) == round(a.circumference)
    assert len(b) == round(2 * pi)
    assert b.circumference == 2 * pi

def test_aug_operators():
    ba = Circle(21)
    bb = Circle(22)
    ba += bb
    bb *= 2
    assert ba == Circle(43)
    assert bb == Circle(44)
    assert bb/2 == Circle(22)
