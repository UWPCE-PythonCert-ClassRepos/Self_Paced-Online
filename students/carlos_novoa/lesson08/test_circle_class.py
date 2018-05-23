#!/usr/bin/env python3

import pytest
from circle_class import Circle
from circle_class import circles

"""
Lesson8 - Circle Class Unit Tests
"""

circles_s = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
             Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


def test_circle_non_type():
    with pytest.raises(ValueError):
        Circle()


def test_radius_positive(capsys):
    Circle(-1)
    captured = capsys.readouterr()
    assert captured.out == 'Radius must be positive.\n'


def test_diameter_positive(capsys):
    Circle(None, -1)
    captured = capsys.readouterr()
    assert captured.out == 'Diameter must be positive.\n'


def test_radius_get():
    c = Circle(2)
    assert c.radius == 2
    assert c.diameter == 4


def test_radius_set():
    c = Circle(999)
    c.radius = 4
    assert c.radius == 4
    assert c.diameter == 8


def test_diameter_get():
    c = Circle(None, 4)
    assert c.diameter == 4
    assert c.radius == 2


def test_diameter_set():
    c = Circle(999)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1


def test_area_get():
    c1 = Circle(2)
    c2 = Circle(None, 4)
    assert c1.area == 12.566371
    assert c2.area == 12.566371


def test_area_set():
    with pytest.raises(AttributeError):
        c = Circle(4)
        c.area = 4


def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test__str__(capsys):
    c = Circle(2)
    print(c)
    captured = capsys.readouterr()
    assert captured.out == 'Circle with radius: 2\n'


def test__repr__(capsys):
    c = Circle(2)
    assert repr(c) == "Circle(2)"


def test__add__():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)


def test__mul__():
    c2 = Circle(4)
    assert c2 * 3 == Circle(12)


def test__rmul__():
    c2 = Circle(4)
    assert 3 * c2 == Circle(12)


def test_comparisons():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert (c1 > c2) is False
    assert (c1 < c2) is True
    assert (c1 == c2) is False
    assert (c2 == c3) is True


def test_object_sorting():
    circles.sort()
    assert circles == circles_s
