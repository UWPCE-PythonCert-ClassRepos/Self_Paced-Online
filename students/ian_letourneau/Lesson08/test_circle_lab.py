#!/usr/bin/env python3
# Ian Letourneau
# 6/4/2018

import math
import circle_lab as cr

# Test Step One


def test_circle_creation():
    c = cr.Circle(5)
    assert c.radius == (5)

    new_c = cr.Circle(23)
    assert new_c.radius == (23)

# Test Step Two


def test_diamter_creation():
    c = cr.Circle(5)
    assert c.diameter == (10)

    new_c = cr.Circle(23)
    assert new_c.diameter == (46)

# Test Step Three


def test_diameter_setter():
    c = cr.Circle(5)
    assert c.diameter == (10)

    c.radius = 15
    assert c.diameter == (30)

    c.diameter = 20
    assert c.radius == (10)

# Test Step Four


def test_area():
    c = cr.Circle(5)
    assert c.area == ((math.pi*5)*2)

    c.radius = 10
    assert c.area == ((math.pi*10)*2)

    c.diameter = 30
    assert c.area == ((math.pi*15)*2)

# Test Step Five


def test_from_diameter():
    c = cr.Circle.from_diameter(10)
    assert c.diameter == (10)
    assert c.radius == (5)

# Test Step Six


def test_str_repr():
    c = cr.Circle(5)
    print (c)
    assert repr(c) == ("'Circle(5.0)'")

    d = eval(repr(c))
    assert d == ('Circle(5.0)')

# Test Step Seven


def test_numeric_protocol():
    c1 = cr.Circle(2)
    c2 = cr.Circle(4)

    c3 = c1 + c2
    assert eval(repr(c3)) == ('Circle(6.0)')

    c4 = c2*3
    assert eval(repr(c4)) == ('Circle(12.0)')

    c5 = 3*c2
    assert eval(repr(c5)) == ('Circle(12.0)')

# Test Step Eight


def test_comparison_overrides():
    c1 = cr.Circle(2)
    c2 = cr.Circle(4)

    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c1 == c2) == False

    c3 = cr.Circle(4)
    assert (c2 == c3) == True

    c4 = cr.Circle(15)
    c5 = cr.Circle(9)
    c6 = cr.Circle(6)
    c7 = cr.Circle(5)
    c8 = cr.Circle(1)

    circles = [c1, c2, c3, c4, c5, c6, c7, c8]
    circles.sort(key=cr.Circle.sort_key)

    print (circles)
    assert eval(repr(circles[0])) == ('Circle(1.0)')
    assert eval(repr(circles[-1])) == ('Circle(15.0)')
