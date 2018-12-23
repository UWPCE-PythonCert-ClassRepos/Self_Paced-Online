
# Test Suite for circle.py
# Alejandro Guardia

from circle import Circle
import pytest


def test_initialization():
    e = Circle(5)
    assert e.radius == 5


def test_diameter():
    e = Circle(4)
    assert e.diameter == 8


def test_diameter_setter():
    e = Circle(4)
    e.diameter = 2
    assert e.radius == 1
    assert e.diameter == 2


def test_circle_area():
    e = Circle(2)
    assert round(e.area,3) == 12.566


def test_change_area():
    e = Circle(2)
    with pytest.raises(AttributeError):
        e.area = 10


def test_alternate_constructor():
    e = Circle.from_diameter(8)
    assert e.diameter == 8
    assert e.radius == 4


def test_str():
    e = Circle(4)
    assert str(e) == "Circle with radius: 4"


def test_repr():
    e = Circle(4)
    assert repr(e) == "Circle(4)"


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3.radius == 6


def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(2)
    assert c1 < c2
    assert c2 > c1
    assert c1 == c3
    assert c1 >- c3
    assert c3 <= c1





