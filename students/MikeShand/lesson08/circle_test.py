#!/usr/bin/env python

from circle import Circle

from math import pi


def test_radius():
    c = Circle(2)
    assert c.radius == 2


def test_diameter():
    c = Circle(2)
    assert c.diameter == 4


def test_area():
    c = Circle(2)
    assert c.area == pi*4


def test_str():
    c = Circle(2)
    assert str(c) == 'Circle with radius: 2'


def test_repr():
    c = Circle(2)
    assert repr(c) == "Circle(2)"


def test_add():
    c = Circle(2)
    d = Circle(3)
    assert c + d == Circle(5)


def test_mul():
    c = Circle(2)
    d = Circle(3)
    assert c*d == Circle(6)


def test_eq():
    c = Circle(2)
    e = Circle(2)
    assert c == e


def test_lt():
    c = Circle(2)
    d = Circle(3)
    assert c < d


