
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


def test_mult():
    c1 = Circle(2)
    assert c1*3 == Circle(6)
    assert 3*c1 == Circle(6)
    assert c1*3 == 3 * c1


def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(2)
    assert c1 < c2
    assert c2 > c1
    assert c1 == c3
    assert c1 >= c3
    assert c3 <= c1


def test_sort_circles():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


def test_augmented_oper():
    c1 = Circle(2)
    c2 = Circle(4)
    c1 += c2
    c2 *= 2
    assert c1 == Circle(6)
    assert c2 == Circle(8)








