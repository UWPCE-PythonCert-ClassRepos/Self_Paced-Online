#!/usr/bin/env python3
"""execute 'pytest' to initate test"""

from circle_class import (Circle)


def test_s1():
    c = Circle(2)
    assert c._radius == 2
    assert c.radius == 2
    assert type(c) == Circle


def test_s2():
    c = Circle(2)
    assert c._diameter == 4
    assert c.diameter == 4


def test_s3():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1


def test_s4():
    c = Circle(2)
    assert c.area == 12.566370614359172
    try:
        c.area = 40
    except AttributeError:
        pass


def test_s5():
    c = Circle.from_diameter(8)
    assert c.radius == 4


def test_s6():
    c = Circle(2)
    assert repr(c) == 'Circle(2)'


def test_s7():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 + c2 == Circle(6))
    assert c1*3 == Circle(6)
    assert 3*c1 == Circle(6)


def test_s8():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 < c2
    assert c2 > c1
    c3 = Circle(2)
    assert c1 == c3
