#!/usr/bin/env python3
"""
File Name: test_circle.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/16/2018
Python Version: 3.6.4
"""
from circle_class import Circle
import pytest


def test_radius_constructor():
    c = Circle(4)
    assert c.radius == 4


def test_radius_setter():
    c = Circle(4)
    c.radius = 2
    assert c.radius == 2
    with pytest.raises(ValueError):
        c.radius = -2


def test_diameter():
    c = Circle(7.5)
    assert c.diameter == 15


def test_diameter_setter():
    c = Circle(5)
    c.diameter = 12
    assert c.radius == 6
    with pytest.raises(ValueError):
        c.diameter = -5


def test_area():
    c = Circle(2)
    assert c.area == 12.566370614359172
    with pytest.raises(AttributeError):
        c.area = 12


def test_from_diameter():
    c = Circle.from_diameter(10)
    assert c.radius == 5
    with pytest.raises(ValueError):
        d = Circle.from_diameter(-10)


def test_str_method():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4'


def test_rper_method():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'


def test_add():
    d = Circle(4) + Circle(2)
    assert d.radius == 6


def test_add2():
    with pytest.raises(ValueError):
        Circle(4) + 5


def test_mult():
    c = Circle(3)
    d = c * 3
    assert d.radius == 9


def test_mult2():
    c = Circle(3)
    d = 3 * c
    assert d.radius == 9


def test_mult3():
    with pytest.raises(ValueError):
        Circle(2) * -3


def test_eq():
    assert Circle(4) == Circle(2) * 2


def test_lt():
    assert Circle(4) < Circle(5)
    assert Circle(5) > Circle(4)


def test_sort():
    circ = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circ.sort()
    assert circ == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


def test_reflection():
    assert Circle(2) * 3 == 3 * Circle(2)


def test_augmented_add():
    a = Circle(2)
    a += Circle(4)
    assert a == Circle(6)


def test_augmented_mult():
    a = Circle(2)
    a *= 3
    assert a == Circle(6)
