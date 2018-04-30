import circle
from math import pi
import pytest

test = circle.Circle(5)

def test_radius():
    assert(test.radius == 5)

def test_diameter():
    assert(test.diameter == 10)

def test_set_diameter():
    test.diameter = 20
    assert(test.diameter == 20)
    assert(test.radius == 10)

def test_from_diameter():
    diam_test = circle.Circle.from_diameter(30)
    assert(diam_test.radius == 15)

def test_add_():
    circle1 = circle.Circle(1)
    circle2 = circle.Circle(2)
    assert(circle1 + circle2 == 3)

def test_mult_():
    circle1 = circle.Circle(1)
    circle2 = circle.Circle(2)
    assert(circle1 * circle2 == 2)

def test_comparison():
    circle1 = circle.Circle(1)
    circle2 = circle.Circle(2)
    assert(circle1 != circle2)
    assert(circle1 < circle2)
    assert(circle1 <= circle2)

