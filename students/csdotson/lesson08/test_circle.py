#!/usr/bin/env python
"""
Test file used to develop (TDD) and test 'html_render.py'
"""

import circle as c

def test_radius():
    circle = c.Circle(4)
    assert circle.radius == 4

def test_diameter():
    circle = c.Circle(4)
    assert circle.diameter == 8
