#!/usr/bin/env python3

from Circle import Circle
from math import pi


def test_radius():
    a = Circle(5)
    assert a.radius == 5


def test_diameter():
    a = Circle(5)
    assert a.diameter == 10


def test_diameter_update_d():
    a = Circle(5)
    a.diameter = 20
    assert a.diameter == 20


def test_diameter_update_r():
    a = Circle(5)
    a.diameter = 20
    assert a.radius == 10


def test_area():
    a = Circle(5)
    assert a.area == 25 * pi


def test_alt_construct_diameter():
    a = Circle.from_diameter(10)
    assert a.diameter == 10


def test_str_function():
    a = Circle(5)
    assert a.__str__() == "Cirle with Radius: {}".format(a.radius)


def test_repr_function():
    a = Circle(5)
    assert a.__repr__() == "Circle(5)"


def test_addition():
    a = Circle(5)
    b = Circle(5)
    c = a + b
    assert c.radius == 10


def test_multiplication():
    a = Circle(5)
    b = a * 2
    assert b.radius == 10


def test_rev_mult():
    a = Circle(5)
    b = 2 * a
    assert b.radius == 10


def test_lt():
    a = Circle(10)
    b = Circle(20)
    assert (a < b) is True


def test_gt():
    a = Circle(10)
    b = Circle(20)
    assert (a > b) is False


def test_equal_to():
    a = Circle(10)
    b = Circle(20)
    assert (a == b) is False


def test_not_equal_to():
    a = Circle(10)
    b = Circle(20)
    assert (a != b) is True


def test_sort():
    x = [Circle(7), Circle(30), Circle(12), Circle(4)]
    x.sort()
    assert x == [Circle(4), Circle(7), Circle(12), Circle(30)]
