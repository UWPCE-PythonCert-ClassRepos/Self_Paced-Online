#!/usr/bin/env python3

import pytest
import math

import circle

c1 = circle.Circle(5)
c2 = circle.Circle(2)
c3 = circle.Circle(2)

circles = [circle.Circle(2), circle.Circle(1), circle.Circle(4),
    circle.Circle(8), circle.Circle(0.5)]

def test_init():
    assert c1.radius == 5

    with pytest.raises(circle.RadiusError):
        circle.Circle(-5)

    with pytest.raises(circle.RadiusError):
        circle.Circle('not a number')

def test_repr():
    assert c1.__repr__() == 'Circle(5)'

def test_str():
    assert c1.__str__() == 'Circle of radius: 5.000000'

def test_eq():
    assert c2 == c3
    assert c2 != c1

def test_lt():
    assert c2 < c1
    assert c2 <= c3
    assert c2 >= c2
    assert c1 > c3
    circles.sort()
    assert circles == [circle.Circle(0.5), circle.Circle(1), circle.Circle(2),
        circle.Circle(4), circle.Circle(8)]

def test_add():
    assert c1 + c2 == circle.Circle(7)

def test_iadd():
    c4 = circle.Circle(5)
    c5 = circle.Circle(2)
    c4 += c5
    assert c4 == circle.Circle(7)

def test_sub():
    assert c1 - c2 == circle.Circle(3)

    with pytest.raises(circle.RadiusError):
        c2 - c1

def test_isub():
    c4 = circle.Circle(5)
    c5 = circle.Circle(2)
    c4 -= c5
    assert c4 == circle.Circle(3)

    c6 = circle.Circle(5)
    c7 = circle.Circle(2)
    with pytest.raises(circle.RadiusError):
        c7 -= c6
    assert c7 == circle.Circle(2)

def test_mul():
    assert c1*2 == circle.Circle(10)
    assert 3*c2 == circle.Circle(6)
    assert 4*c1 == c1*4

def test_imul():
    c5 = circle.Circle(2)
    c5 *= 2
    assert c5 == circle.Circle(4)

def test_truediv():
    assert c2/2 == circle.Circle(1)

def test_properties():
    assert c1.area == 25*math.pi
    assert c1.diameter == 10
