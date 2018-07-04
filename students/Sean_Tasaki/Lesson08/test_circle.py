

import pytest
from circle import *
from math import pi

"""
Sean Tasaki
6/24/2018
Lesson08.test_circle
"""

def test_radius():
    c = Circle(34)
    assert c.radius ==34

def test_diameter():
    c = Circle(50)
    assert c.radius == 50
    assert c.diameter == 100

def test_setter_diameter():
    c = Circle(50)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def test_area():
    c = Circle(2)
    assert c.area == 12.566370614359172

def test_alt_constructor_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius ==4

def test__str__(capsys):
    # Test both __str__ and __repr__ and eval(repr)) functions
    # Test  __str__
    c = Circle(100)
    print(c)
    printed = capsys.readouterr()
    assert printed.out == 'Circle with radius: 100\n'

    # Test __repr__
    assert repr(c) == 'Circle(100)'

    # Test eval(repr())
    d = eval(repr(c))
    assert d.diameter == 200
    assert d.radius ==100

def test__add__():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert 6 == (c1 + c2).radius 
    assert repr(c3) == 'Circle(6)'

def test__mul__():
    c1 = Circle(4)
    c12 = c1 * 3
    assert 12 == (c1 * 3).radius
    assert repr(c12) == 'Circle(12)'

def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert c1 < c2 
    assert c2 > c1
    assert c3 == c2

def test_sort():
    c1 = Circle(100)
    circlis = [c1, Circle(5), Circle(20), Circle(1)]
    circlis.sort() == [Circle(1), Circle(5), Circle(20), c1]

