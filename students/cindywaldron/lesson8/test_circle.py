#!/usr/bin/env python3

import pytest
from circle import Circle

def test_diameter():
    c = Circle(2)
    assert c.diameter == 4

def test_area():
    c = Circle(1)
    a = round(c.area, 2)
    assert a == 3.14

def test_from_diameter():
    c = Circle.from_diameter(4)
    assert c.radius == 2

def test_str():
    c = Circle(5)
    assert c.__str__() == "Circle with radius: 5.00"

def test_repr():
    c = Circle(10)
    assert c.__repr__() == "Circle(10)"

def test_add():
    c1 = Circle(2)
    c2 = Circle(3)
    sum = c1 + c2
    c = Circle(5)
    assert c.radius == sum.radius

def test_radd():
    c1 = Circle(2)
    c2 = Circle(3)
    sum = c2 + c1
    c = Circle(5)
    assert c.radius == sum.radius

def test_mul():
    c = Circle(2)
    result = c*10
    c1 = Circle(20)
    assert c1.radius == result.radius

def test_rmul():
    c = Circle(2)
    result = 30*c
    c1 = Circle(60)
    assert c1.radius == result.radius

def test_lt():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1.__lt__(c2) == True

def test_gt():
    c1 = Circle(4)
    c2 = Circle(2)
    assert c1.__gt__(c2) == True

def test_eq():
    c1 = Circle(2)
    c2 = Circle(2)
    assert c1.__eq__(c2) == True

def test_iadd():
    c1 = Circle(2)
    c2 = Circle(3)
    c1 += c2
    c = c1
    assert c is c1
    assert c.radius == c1.radius