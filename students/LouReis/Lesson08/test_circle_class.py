#!/usr/bin/env python3.7
# test_circle_class.py
# Coded by LouReis

from circle_class import *
from pytest import raises
from io import StringIO
import sys

# Test that the Circle can be called with a radius 3 resulting in the following:
def test_1():
    test = Circle(3)
    assert test.radius == 3
    assert test.diameter == 6
    assert test.area == 28.274333882308138

# Test that the Circle can be called with a decimal value.
def test_2():
    test = Circle(1.5)
    assert test.radius == 1.5
    assert test.diameter == 3
    assert test.area == 7.0685834705770345

# Test that an existing Circle diameter can be changed.
def test_3():
    test = Circle(1.5)
    test.diameter = 2
    assert test.radius == 1
    assert test.diameter == 2
    assert test.area == 3.141592653589793

# Test that attempting to set the test.area raises an AttributeError
def test_4():
    test = Circle(3)
    with raises(AttributeError):
        test.area = 4.5

# Test that a circle can be created with just the diameter using the classmethod.
def test_5():
    test = Circle.from_diameter(3)
    assert test.radius == 1.5
    assert test.diameter == 3
    assert test.area == 7.0685834705770345

# Test the __str__ functionality.and check the output.
def test_6():
    # Using StringIO from io...
    # Store the reference, in case you want to show things again in standard output
    old_stdout = sys.stdout
    # This variable will store everything that is sent to the standard output
    result = StringIO()
    sys.stdout = result
    # Here we can call anything we like, like external modules, and everything that they will send to standard output will be stored on "result"
    test = Circle(4)
    print(test)
    # Redirect again the std output to screen
    sys.stdout = old_stdout
    # Then, get the stdout like a string and process it!
    result_string = result.getvalue()
    assert "Circle with a radius of: 4" in result_string

# Test the output for __repr__ and check the output
def test_7():
    test = Circle(4)
    assert repr(test) == 'Circle(4)'
