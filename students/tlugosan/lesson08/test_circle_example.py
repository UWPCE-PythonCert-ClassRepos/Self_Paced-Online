#!/usr/bin/env python3

import pytest
import circle_example as cr


def test_init():
    c1 = cr.Circle(3)


def test_constructor_requires_parameter():
    with pytest.raises(TypeError):
        c2 = cr.Circle()


def test_radius_0():
    # with pytest.raises(ValueError):
    c1 = cr.Circle(0)


def test_radius():
    c1 = cr.Circle(4)
    assert c1.radius == 4


def test_diameter():
    c1 = cr.Circle(4)
    assert c1.diameter == 8


def test_set_diameter():
    c1 = cr.Circle(7)
    assert c1.diameter == 14
    c1.diameter = 10
    assert c1.radius == 5


def test_area():
    c1 = cr.Circle(2)
    assert c1.area == 12.566370614359172


def test_fail_to_set_area():
    c1 = cr.Circle(2)
    with pytest.raises(AttributeError):
        c1.area = 56


def test_from_diameter():
    c1 = cr.Circle(7)
    c1.from_diameter(8)


def test_repr():
    c1 = cr.Circle(5)
    assert repr(c1) == 'Circle(5)'


def test_str():
    c1 = cr.Circle(9)
    assert str(c1) == "Circle with radius: 9.000000"


def test_add():
    c1 = cr.Circle(11)
    c2 = cr.Circle(7)
    assert (c1 + c2).radius == 18


def test_add_augmented():
    c1 = cr.Circle(11)
    c2 = cr.Circle(7)
    c1 += c2
    assert c1.radius == 18


def test_mul():
    c1 = cr.Circle(14)
    assert (c1 * 3).radius == 42


def test_mul_augmented():
    c1 = cr.Circle(12)
    c1 *= 3
    assert c1.radius == 36


def test_rmul():
    c1 = cr.Circle(14)
    assert (3 * c1).radius == 42


def test_gt():
    c1 = cr.Circle(14)
    c2 = cr.Circle(13)
    assert (c1 > c2)


def test_ge():
    c1 = cr.Circle(14)
    c2 = cr.Circle(14)
    c3 = cr.Circle(23)
    assert c1 >= c2
    assert c3 >= c1


def test_lt():
    c1 = cr.Circle(14)
    c2 = cr.Circle(12)
    assert c2 < c1


def test_le():
    c1 = cr.Circle(14)
    c2 = cr.Circle(14)
    c3 = cr.Circle(22)
    assert c1 <= c2
    assert c2 <= c3


def test_eq():
    c1 = cr.Circle(14)
    c2 = cr.Circle(14)
    assert c1 == c2


def test_ne():
    c1 = cr.Circle(15)
    c2 = cr.Circle(15)
    assert c1 != c2


def test_sort():
    c1 = cr.Circle(1)
    c2 = cr.Circle(2)
    c3 = cr.Circle(3)
    c4 = cr.Circle(4)
    c5 = cr.Circle(4)
    c6 = cr.Circle(6)
    circle_list = [c2, c5, c4, c1, c6, c3]
    circle_list.sort(key=cr.Circle.sort_key)
    assert circle_list == [c1, c2, c3, c4, c5, c6]


def test_truediv():
    c1 = cr.Circle(14)
    c2 = cr.Circle(23)
    c1 /= 2
    with pytest.raises(ValueError):
        c2 /= 0
