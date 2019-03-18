# Lesson 8 Assignment 1
# Circle Class pytest
# Jason Virtue 03/09/2019

from circle import circle

# Test Step 1

def test_init():
    test_circle = circle(4)
    assert (test_circle.radius == 4) is True

# Test Step 2


def test_diameter():
    test_circle = circle(4)
    assert (test_circle.diameter == 8) is True
    assert (test_circle.radius == 4) is True
# Test Step 3
    test_circle.diameter = 16
    assert (test_circle.diameter == 16) is True
    assert (test_circle.radius == 8) is True

# Test Step 4


def test_area():
    test_circle = circle(2)
    assert test_circle.area == 12.566370614359172
    test_circle.area == 42 is AttributeError

# Test Step 5


def test_from_diameter():
    test_circle = circle.from_diameter(8)
    assert (test_circle.diameter == 8) is True
    assert (test_circle.radius == 4) is True

# Test Step 6


def test_str_():
    test_circle = circle(4)
    assert (str(test_circle) == 'Circle with radius: 4') is True


def test_repr_():
    test_circle = circle(4)
    assert (repr(test_circle) == 'Circle(4)') is True

# Test Step 7


def test_add_():
    test_circle1 = circle(2)
    test_circle2 = circle(4)
    assert (test_circle1 + test_circle2 == circle(6)) is True


def test_mul_():
    test_circle2 = circle(4)
    assert (test_circle2*3 == circle(12)) is True

# Test Step 8


def test_ls_():
    test_circle1 = circle(2)
    test_circle2 = circle(4)
    assert ((test_circle1 > test_circle2) is False) is True
    assert ((test_circle1 < test_circle2) is True) is True
    assert ((test_circle1 == test_circle2) is False) is True
    test_circle3 = circle(4)
    assert ((test_circle3 == test_circle2) is True) is True
    