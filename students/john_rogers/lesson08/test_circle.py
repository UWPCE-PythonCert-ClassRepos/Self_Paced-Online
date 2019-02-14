#!/usr/bin/env python3
"""
pytest for circle.py
Author: JohnR
Version: 1.0
Last Updated: 2/11/19
Notes:
"""

import pytest
import circle as c


@pytest.fixture
def circles():
    list_of_circles = [
        c.Circle(4),
        c.Circle(5),
        c.Circle(3),
        c.Circle(9),
        c.Circle(2),
    ]
    return list_of_circles


def test_circle():
    circle = c.Circle()
    assert circle.radius == 5
    assert circle.diameter == 10
    assert circle.area == 79
    assert circle.circumference() == 31


def test_sort(circles):
    foo = sorted(circles)
    assert foo[0].radius == 2
    assert foo[4].radius == 9
    foo_reverse = sorted(circles, reverse=True)
    assert foo_reverse[0].radius == 9
    assert foo_reverse[4].radius == 2


def test_from_diameter():
    c1 = c.Circle.from_diameter(10)
    assert c1.radius == 5


def test_add():
    c1 = c.Circle(5)
    c2 = c.Circle(10)
    c3 = c1 + c2
    assert c3 == 15


def test_equality():
    c1 = c.Circle()
    c2 = c.Circle(5)
    assert c1.radius == c2.radius
    assert c1.circumference() == c2.circumference()
    assert c1.area == c2.area


def test_multiply():
    c1 = c.Circle(10)
    c2 = c.Circle(10)
    c3 = c1 * c2
    assert c3 == 100
    c4 = c3 * 2
    assert c4 == 200
    c5 = 2 * c4
    assert c5 == 400


def test_other():
    c1 = c.Circle(4)
    c2 = c.Circle(5)
    assert c1 < c2
    assert c2 > c1
    assert c1 != c2
    assert c1.radius * 2 == 2 * c1.radius

