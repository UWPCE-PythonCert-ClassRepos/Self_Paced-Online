#!/usr/bin/env python3

import pytest
from circle import *
import math



def test_radius():
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    c = Circle(4)
    assert c.diameter == 8


def test_property():
    c = Circle(4)
    c.diameter = 2
    assert c.radius == 1
    assert c.diameter == 2


def test_area():
    c = Circle(2)
    assert c.area == 12.566370614359172


def test_area_2():
    with pytest.raises(AttributeError):
        c = Circle(2)
        c.area = 42


def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_repr_str():
    c = Circle(4)
    assert c.__repr__() == "Circle(4)"


def test_repr_str_2():
    c= Circle(4)
    assert c.__str__() == "Circle with radius: 4.0"


def test_addition():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3.radius == 6


def test_multiply():
    c1 = Circle(4)
    c2 = c1 * 3
    assert c2.radius == 12


def test_less_than():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 < c2) is True


def test_equal():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 == c2) == False 


def test_more():
    c1 = Circle(4)
    c2 = Circle(2)
    print(c1, c2)
    assert (c1 < c2) is False


def test_not_equal():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 != c2) is True


def test_sort_list():
    c = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    c1 = sorted(c)
    assert c1 == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


def test_reflected_multiplication():
    c1 = Circle(4)
    assert c1*3 == 3 * c1


def test_augmented_addition():
    c1 = Circle(4)
    c2 = Circle(5)
    c1 += c2
    assert c1.radius == 9


def test_augmented_multiplication():
    c1 = Circle(5)
    c1 *= 5
    assert c1.radius == 25


#Testing subclass Sphere
def test_sphere():
    s = Sphere(3)
    assert s.radius == 3


def test_sphere_str():
    s = Sphere(3)
    assert s.__str__() == "Sphere with a radius: 3.0" 


def test_sphere_repr():
    s = Sphere(3)
    assert s.__repr__() == "Sphere(3)"


def test_volume():
    s = Sphere(3)
    assert s.volume == 113.09733552923254


def test_area_sphere():
    s = Sphere(4)
    assert s.area == 201.06192982974676


def test_from_diameter_sphere():
    s = Sphere.from_diameter(4)
    assert s.diameter == 4
    assert s.radius == 2


def test_addition_sphere():
    s1 = Sphere(2)
    s2 = Sphere(4)
    s3 = s1 + s2
    assert s3.radius == 6


def test_multiply_sphere():
    s1 = Sphere(4)
    s2 = s1 * 3
    assert s2.radius == 12


def test_less_than_sphere():
    s1 = Sphere(2)
    s2 = Sphere(4)

    assert (s1 < s2) is True


def test_equal_sphere():
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert (s1 == s2) == False 


def test_more_sphere():
    s1 = Sphere(4)
    s2 = Sphere(2)
    assert (s1 < s2) is False


def test_not_equal_sphere():
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert (s1 != s2) is True


def test_sort_list_sphere():
    s = [Sphere(6), Sphere(7), Sphere(8), Sphere(4), Sphere(0), Sphere(2), Sphere(3), Sphere(5), Sphere(9), Sphere(1)]
    s1 = sorted(s)
    assert s1 == [Sphere(0), Sphere(1), Sphere(2), Sphere(3), Sphere(4), Sphere(5), Sphere(6), Sphere(7), Sphere(8), Sphere(9)]
