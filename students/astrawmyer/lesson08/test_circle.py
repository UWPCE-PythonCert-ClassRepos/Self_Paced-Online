import pytest
import circle
import math


def test_radius():
    c = circle.Circle(5)
    assert c.radius == 5


def test_diameter():
    c = circle.Circle(5)
    assert c.diameter == 10


def test_input_diameter():
    c = circle.Circle(5)
    c.diameter = 50
    assert c.diameter == 50
    assert c.radius == 25


def test_area():
    c = circle.Circle(5)
    assert c.area == math.pi*25


def test_construct_diameter():
    c = circle.Circle.from_diameter(50)
    assert c.radius == 25


def test_str():
    c = circle.Circle(8)
    assert c.__str__() == "Circle with radius: 8"


def test_repr():
    c = circle.Circle(8)
    assert repr(c) == "Circle(8)"


def test_add():
    c1 = circle.Circle(2)
    c2 = circle.Circle(4)
    c3 = c1 + c2
    assert c3.radius == 6


def test_mult():
    c1 = circle.Circle(2)
    c2 = 3 * c1
    c3 = c1 * 3
    assert c2.radius == 6
    assert c3.radius == 6


def test_lt():
    c1 = circle.Circle(2)
    c2 = circle.Circle(4)
    compare = c1 < c2
    assert compare == True


def test_gt():
    c1 = circle.Circle(2)
    c2 = circle.Circle(4)
    compare = c2 > c1
    assert compare == True


def test_eq():
    c1 = circle.Circle(2)
    c2 = circle.Circle(2)
    compare = (c1 == c2)
    assert compare == True


def test_sort():
    circles = [circle.Circle(8), circle.Circle(2), circle.Circle(10)]
    circles.sort()
    assert circles == [circle.Circle(2), circle.Circle(8), circle.Circle(10)]