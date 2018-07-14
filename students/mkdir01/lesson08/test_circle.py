#!/usr/bin/env python

from io import StringIO
from circle import *
from math import pi
import pytest
import io
from contextlib import redirect_stdout


def test_1():
    with pytest.raises(TypeError):
        testdata = Circle()
    #assert TypeError  # : __init__() missing 1 required positional argument: 'radius'
def test_set_area():
    c = Circle(4)
    with pytest.raises(AttributeError):
        c.area = 4

# Step 1
def test_get_radius_int():
    c = Circle(4)
    testdata = c.radius
    assert testdata == 4


def test_get_radius_float():
    c = Circle(3.14)
    testdata = c.radius
    assert testdata == 3.14


# Step 2
def test_get_diameter_int():
    c = Circle(4)
    testdata = c.diameter
    assert testdata == 8


def test_get_diameter_float():
    c = Circle(3.14)
    testdata = c.diameter
    assert testdata == 6.28


# Step 3
def test_set_diameter():
    c = Circle(4)
    c.diameter = 2
    testdata = c.diameter
    assert testdata == 2


def test_set_diameter_2():
    c = Circle(4)
    c.diameter = 2
    testdata = c.radius
    assert testdata == 1


# Step 4
def test_get_area():
    c = Circle(4)
    testdata = c.area
    assert testdata == pi * 16


def test_set_area():
    c = Circle(4)
    with pytest.raises(AttributeError):
        c.area = 4


# Step 5
def test_make_diameter():
    c = Circle.from_diameter(8)
    testdata = c.diameter
    assert testdata == 8


def test_make_diameter_2():
    c = Circle.from_diameter(8)
    testdata = c.radius
    assert testdata == 4


# Step 6
def test_str_method():
    c = Circle(4)
    f = io.StringIO()
    with redirect_stdout(f):
        print(c)
    assert f.getvalue() == "Circle with radius: 4.000000\n"


def test_repr_method():
    c = Circle(4)
    testdata = repr(c)
    assert testdata == "Circle(4)"


def test_eval_method():
    c = Circle(4)
    testdata = eval(repr(c))
    assert testdata.radius == 4


# Step 7
def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c1 + c2
    assert testdata.radius == 6


def test_mul():
    c = Circle(4)
    testdata = c * 3
    assert testdata.radius == 12

def test_rmul():
    c = Circle(4)
    testdata = 3 * c
    assert testdata.radius == 12


# Step 8
def test_gt():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c1 > c2
    assert testdata == False


def test_lt():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c1 < c2
    assert testdata == True


def test_eq():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c1 == c2
    assert testdata == False


def test_eq_2():
    c2 = Circle(4)
    c3 = Circle(4)
    testdata = c2 == c3
    assert testdata == True


def test_sorted():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    testdata = sorted(circles)
    assert testdata == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    testdata = circles
    assert testdata == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


# Step 8: Optional Features
def test_radd():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c2 + c1
    assert testdata.radius == 6


def test_sub():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c2 - c1
    assert testdata.radius == 2


def test_rsub():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c1 - c2
    assert testdata.radius == -2


def test_div():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c1 / c2
    assert testdata.radius == .5


def test_rdiv():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c2 / c1
    assert testdata.radius == 2


def test_iadd():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c1
    testdata += c2
    assert testdata.radius == 6


def test_isub():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c2
    testdata -= c1
    assert testdata.radius == 2


def test_imul():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c1
    testdata *= c2
    assert testdata.radius == 8


def test_idiv():
    c1 = Circle(2)
    c2 = Circle(4)
    testdata = c2
    testdata /= c1
    assert testdata.radius == 2


