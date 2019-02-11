#!/usr/bin/env python3
"""
pytest for circle.py
Author: JohnR
Version: .9
Last Updated: 2/10/19
Notes:
"""

import pytest
import circle as c


def test_circle():
    circle = c.Circle()
    assert circle.radius == 5
    assert circle.diameter == 10
    assert circle.area == 79
    assert circle.circumference() == 31


def test_sort():
    pass


def test_add():
    c1 = c.Circle(5)
    c2 = c.Circle(10)
    c3 = c1 + c2
    assert c3 == 15


def test_equality():
    c1 = c.Circle(5)
    c2 = c.Circle(5)
    assert c1.radius == c2.radius
    assert c1.circumference() == c2.circumference()

