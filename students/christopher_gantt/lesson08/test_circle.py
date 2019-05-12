'''
test code for circle.py
'''

import pytest, math
from circle import Circle, Sphere

def test_init():
    c = Circle(4)
    assert c.radius == 4
    assert c.diameter == 8


def test_diameter():
    c = Circle(4)
    c.diameter = 10
    assert c.diameter == 10
    assert c.radius == 5


def test_area():
    c = Circle(2)
    assert c.area == math.pi * 2 ** 2


def test_str_repr():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4'
    assert repr(c) == 'Circle(4)'


def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.radius == 4
    assert c.diameter == 8


def test_add():
    c = Circle(4)
    d = Circle(2)
    e = c + d
    assert e.radius == 6
    assert e.diameter == 12


def test_multiply():
    c = Circle(4)
    c = c * 2
    assert c.radius == 8
    assert c.diameter == 16


def test_rmul():
    c = Circle(4)
    c = 2 * c
    assert c.radius == 8
    assert c.diameter == 16


def test_gt():
    c = Circle(4)
    d = Circle(2)
    assert c > d


def test_lt():
    c = Circle(4)
    d = Circle(2)
    assert d < c


def test_eq():
    c = Circle(4)
    d = Circle(4)
    assert d == c


def test_sort():
    circles = [Circle(3), Circle(2), Circle(4), Circle(1)]
    circles.sort()
    assert circles == [Circle(1), Circle(2), Circle(3), Circle(4)]


def test_sphere_str_repr():
    s = Sphere(4)
    assert str(s) == 'Sphere with radius: 4'
    assert repr(s) == 'Sphere(4)'

def test_sphere_volume():
    s = Sphere(4)
    assert s.volume == (4/3) * math.pi * (s.radius ** 3)


def test_sphere_area():
    s = Sphere(4)
    assert s.area == 4 * math.pi * (s.radius ** 2)


def test_sphere_from_diameter():
    s = Sphere.from_diameter(8)
    assert s == Sphere(4.0)
    assert s.radius == 4
    assert s.diameter == 8