import pytest
from Circle import *


def test_radius():
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 10
    assert c.diameter == 10
    assert c.radius == 5


def test_area():
    c = Circle(4)
    assert c.area == 50.26548245743669
    with pytest.raises(AttributeError):
        c.area = 100


def test_from_diameter():
    c = Circle.from_diameter(20)
    assert c.diameter == 20
    assert c.radius == 10


def test__repr__():
    c = Circle(4)
    assert repr(c) == "Circle(4)"


def test__str__():
    c = Circle(4)
    print(c)
    assert str(c) == "Circle with radius: 4"


def test__add__():
    c1 = Circle(2)
    c2 = Circle(4)
    # print(repr(c1 + c2))
    assert repr(c1 + c2) == "Circle(6)"


def test__mul__():
    c1 = Circle(2)
    c2 = Circle(4)
    # print(repr(c1 * c2))
    assert repr(c1 * c2) == "Circle(8)"
    assert repr(c1 * 3) == "Circle(6)"
    assert repr(3 * c1) == "Circle(6)"


def test__lt__():
    c1 = Circle(2)
    c2 = Circle(4)
    tf1 = c1 < c2
    tf2 = c2 < c1
    assert tf1 is True
    assert tf2 is False


def test__gt__():
    c1 = Circle(2)
    c2 = Circle(4)
    tf1 = c1 > c2
    tf2 = c2 > c1
    assert tf1 is False
    assert tf2 is True


def test__eq__():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    tf1 = c1 == c2
    tf2 = c2 == c3
    assert tf1 is False
    assert tf2 is True


def test_sort():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(9)
    circles = [c2, c3, c1]
    circles.sort()
    assert circles == [c1, c2, c3]
