#!/usr/bin/env python

from circle import Circle, Sphere
import pytest

def test_cirle():
    c = Circle(4)
    assert c.radius == 4
    assert c.diameter == 8


def test_set_diameter():
    c = Circle(4)
    c.diameter = 4

    assert c.radius == 2

def test_area():
    c = Circle(4)
    assert c.area == pytest.approx(25.13274)

def test_set_area():
    c = Circle(4)
    with pytest.raises(AttributeError):
        c.area = 42    

def test_str_circle():
    c = Circle(5)
    print(c)
    assert str(c) == "Circle with radius: 5.0"
def test_repr_circle():
    c = Circle(5)
    print(c)
    assert repr(c) == "Circle(5.0)"
    
def test_add_circle():
    c1 = Circle(3)
    c2 = Circle(2)
    c3 = c1 + c2

    assert c3.radius == 5
    
def test_multiply_circle():
    c2 = Circle(2)
    c4 = c2 * 3
    c5 = 3 * c2

    assert c4.radius == 6
    assert c5.radius == 6

def test_eq():
    c1 = Circle(3)
    c2 = Circle(3)

    assert c1 == c2

def test_ne():
    c1 = Circle(3)
    c2 = Circle(4)

    assert c1 != c2

def test_gt():
    c1 = Circle(3)
    c2 = Circle(4)

    assert c2 > c1

def test_ge():
    c1 = Circle(3)
    c2 = Circle(4)

    assert c2 >= c1

def test_sort():
    circles = [Circle(5), Circle(4), Circle(3), Circle(2), Circle(1)]
    circles.sort()

    assert circles[0] < circles[1]

def test_iadd():
    c1 = Circle(3)
    c2 = Circle(4)
    c1 += c2

    assert c1.radius == 7

def test_imul():
    c1 = Circle(3)
    c1 *= 4

    assert c1.radius == 12

def test_volume():
    s = Sphere(2)

    assert s.volume == pytest.approx(33.51032)

def test_sphere_sort():
    spheres = [Sphere(5), Sphere(4), Sphere(3), Sphere(2), Sphere(1)]
    spheres.sort()

    assert spheres[0] < spheres[1]
