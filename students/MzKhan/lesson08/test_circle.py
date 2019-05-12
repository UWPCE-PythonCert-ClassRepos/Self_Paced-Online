"""
Name: Muhammad Khan
Date: 04/01/2019
Assignment08

purpose: Test the functionality of circle.py

"""
import circle as c
import math as m
import pytest

def test_Circle():

    C1 = c.Circle(4)
    C2 = c.Circle(3.2)
    assert C1.radius == 4
    assert C2.radius == 3.2
    with pytest.raises(TypeError):
        C3 = c.Circle(-5)

def test_diameter():

    C1 = c.Circle(9)
    assert C1.diameter == 2*C1.radius

    C1.diameter = 0.0056
    assert C1.diameter == 0.0056
    C1.diameter = 8
    assert C1.diameter == 8
    assert C1.radius == 4

def test_area():

    C = c.Circle(4)
    assert C.area == m.pi*C.radius**2
    with pytest.raises(AttributeError):
        C.area = 10

def test_from_diameter():

    C = c.Circle.from_diameter(8)
    assert C.diameter == 8
    assert C.radius == 4

def test_repr():

    C = c.Circle(4)
    assert repr(C) == "Circle(4)"

def test_str():

    C = c.Circle(8)
    assert str(C) == "Circle with radius: {}".format(C.radius)

def test_add():
    c1 = c.Circle(2)
    c2 = c.Circle(4)
    c3 = c1+c2
    assert repr(c3)== 'Circle(6)'
    assert c1.radius+c2.radius == c3.radius

def test_multiply():

    c1 = c.Circle(2)
    c2 = c1*5
    c3 = c.Circle(10)
    assert repr(c2) == repr(c3)
    assert c2.radius == 10
    c4 = 6*c1
    assert c4.radius == 12
    assert c1*10 == 10*c1

def test_lt():

    c1 = c.Circle(10)
    c2 = c.Circle(10.01)

    assert (c1 < c2)
    assert (c1 > c2) is False

def test_eq():

    c1 = c.Circle(10)
    c2 = c.Circle(10.01)
    c3 = c.Circle(10.01)

    assert (c1 == c2) is False
    assert c2 == c3

def test_sort():

    circles=[c.Circle(6), c.Circle(7), c.Circle(8), c.Circle(4), c.Circle(0),
              c.Circle(2), c.Circle(3), c.Circle(5), c.Circle(9), c.Circle(1)]
    circles.sort()
    for i in range(9):
        c1 = circles[i]
        c2 = circles[i+1]
        assert c1 < c2

def test_optional():

    c1 = c.Circle(10)
    c2 = c.Circle(9.5)
    c1 += c2
    assert c1.radius == 19.5
    c2 *= 4
    assert c2.radius == 38
