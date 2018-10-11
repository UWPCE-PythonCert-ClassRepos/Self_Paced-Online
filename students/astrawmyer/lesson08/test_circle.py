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