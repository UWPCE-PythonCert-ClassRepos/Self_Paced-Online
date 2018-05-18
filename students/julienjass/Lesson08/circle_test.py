import circle
from math import pi
import pytest

def test_for_radius():
    circle_1 = circle.Circle(10)
    assert(circle_1.radius == 10)

def test_for_diameter():
    circle_1 = circle.Circle(5)
    assert(circle_1.diameter == 10)

def test_set_diameter():
    circle_1 = circle.Circle(5)
    circle_1.diameter = 10
    assert(circle_1.diameter == 10)
    assert(circle_1.radius == 5)

def test_from_diameter():
    diam_test = circle.Circle.from_diameter(20)
    assert(diam_test.radius == 10)

def test_add():
    circle_1 = circle.Circle(1)
    circle_2 = circle.Circle(2)
    assert(circle_1 + circle_2 == 3)

def test_multiplication():
    circle_1 = circle.Circle(1)
    assert(circle_1 * 2 == 2)

def test_comparison():
    circle_1 = circle.Circle(1)
    circle_2 = circle.Circle(2)
    assert(circle_1 != circle_2)
    assert(circle_1 < circle_2)
    assert(circle_1 <= circle_2)
