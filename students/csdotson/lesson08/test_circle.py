#!/usr/bin/env python
"""
Test file used to develop (TDD) and test 'circle.py'
"""

import circle as c
import math

def test_radius():
    circle = c.Circle(4)
    assert circle.radius == 4

def test_diameter():
    circle = c.Circle(4)
    assert circle.diameter == 8

def test_diameter_change():
    circle = c.Circle(4)
    circle.diameter = 3
    assert circle.diameter == 3

def test_radius_changes_diameter():
    circle = c.Circle(4)
    circle.radius = 5
    assert circle.diameter == 10

def test_diameter_changes_radius():
    circle = c.Circle(4)
    circle.diameter = 4
    assert circle.radius == 2

def test_area():
    circle = c.Circle(2)
    assert circle.area == (math.pi * math.pow(circle.radius, 2))

def test_circle_creation_from_diameter():
    circle = c.Circle.from_diameter(8)
    assert circle.diameter == 8
    assert circle.radius == 4

# def test_str_method():
#     circle = c.Circle(4)
#     # str = print(circle)
#     # assert str == "Circle with radius: {}".format(circle.radius)
#
# def test_repr_method():
#     circle = c.Circle(4)
#     # assert repr(c) == 'Circle(4)'
#
# def test_eval_repr_method():
#     circle = c.Circle(4)
#     d = eval(repr(circle))
#     assert d == Circle(4)

# def test_add_circles():
#     c1 = c.Circle(2)
#     c2 = c.Circle(4)
#     assert c1 + c2 == c.Circle(6)

def test_mul_circles():
    pass

def test_rmul_circles():
    pass
