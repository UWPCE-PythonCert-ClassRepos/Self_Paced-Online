from math import pi
from circle import Circle
import pytest


def test_step1():
    c = Circle(5)
    assert c.radius == 5


def test_step2():
    c = Circle(5)
    assert c.diameter == 10


def test_step3():
    c = Circle(5)
    c.diameter = 20
    assert c.diameter == 20
    assert c.radius == 10


def test_step4():
    c = Circle(2)
    assert c.area == pi * 2 ** 2
    with pytest.raises(AttributeError):
        c.area = 10


def test_step5():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_step6():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4'
    assert repr(c) == 'Circle(4)'
