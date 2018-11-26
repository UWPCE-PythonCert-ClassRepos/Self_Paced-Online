# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 22:23:29 2018

@author: Laura.Fiorentino
"""


from Circle import Circle
from math import pi


def test_radius():
    c = Circle(5)
    assert c.radius == 5


def test_diameter():
    c = Circle(5)
    assert c.diameter == 10


def test_area():
    c = Circle(5)
    assert c.area == 5 * 5 * pi


def test_from_diameter():
    c = Circle.from_diameter(10)
    assert c.radius == 5
    assert c.diameter == 10


def test_repr():
    c = Circle(5)
    assert repr(c) == 'Circle(5)'


def test_str():
    c = Circle(5)
    assert str(c) == 'Circle with radius: 5'


def test_add():
    c1 = Circle(5)
    c2 = Circle(10)
    assert repr(c1 + c2) == 'Circle(15)'


def test_mul():
    c1 = Circle(5)
    assert repr(c1 * 2) == 'Circle(10)'
    assert repr(2 * c1) == 'Circle(10)'


def test_comparisons():
    c1 = Circle(5)
    c2 = Circle(10)
    c3 = Circle(5)
    a1 = c1 > c2
    assert a1 is False
    a2 = c1 < c2
    assert a2 is True
    a3 = c1 == c3
    assert a3 is True
    a4 = c1 <= c3
    assert a4 is True
    a5 = c1 >= c3
    assert a5 is True


def test_sort():
    circles = [Circle(1), Circle(10), Circle(5), Circle(4)]
    circles.sort()
    assert circles == [Circle(1), Circle(4), Circle(5), Circle(10)]


def test_div():
    c1 = Circle(5)
    c2 = Circle(10)
    assert repr(c1 / c2) == 'Circle(0.5)'
    assert repr(c2 / c1) == 'Circle(2.0)'
