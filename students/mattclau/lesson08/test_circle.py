import pytest
import math

# import * is often bad form, but makes it easier to test everything in a module.
from circle import *

#Test that a circle is initialized with correct radius
def test_init():
    c = Circle(4)

    assert c.radius == 4

#test that diameter property exists
def test_diameter():
    c = Circle(2)

    assert c.diameter == 4

#test that diameter can be set and that it changes the radius
def test_set_diameter():
    c = Circle(2)

    assert c.diameter == 4
    assert c.radius == 2

    c.diameter = 6

    assert c.diameter == 6
    assert c.radius == 3

#test that area is computed correctly and that it can't be set
def test_area():
    c = Circle(5)

    assert c.area == math.pi * c.radius * 2

    with pytest.raises(AttributeError):
        c.area = 42

#test circle can be created with diameter instead of radius
def test_alt_construct():
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4

#test that string and representation of circle are correct
def test_representation():
    c = Circle(5)

    assert repr(c) == 'Circle(5.0)'
    assert str(c) == 'Circle with radius: 5.0'

#test that circles can be added
def test_add():
    c1 = Circle(5)
    c2 = Circle(3)

    assert c1 + c2 == Circle(8)

#test that circles can be multiplied
def test_mult():
    c = Circle(5)

    assert c * 3 == Circle(15)
    assert 3 * c == Circle(15)


#test that circles can be compared
def test_compare():
    c1 = Circle(5)
    c2 = Circle(3)
    c3 = Circle(3)

    assert c1 > c2
    assert c1 >= c2
    assert c1 != c2
    assert c2 == c3
    assert c2 <= c1
    assert c2 < c1

#test that all instances of circle can be printed and sorted
def test_print_sort():
    Circle.circles = []

    c1 = Circle(5)
    c2 = Circle(3)
    c3 = Circle(3)



    assert Circle.circles == [c1, c2, c3]

    Circle.circles.sort(key=Circle.sort_key)

    assert Circle.circles == [c2, c3, c1]