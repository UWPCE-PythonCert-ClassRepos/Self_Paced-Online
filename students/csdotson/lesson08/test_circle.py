#!/usr/bin/env python
"""
Test file used to develop (TDD) and test 'circle.py'
"""

import circle as c

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
