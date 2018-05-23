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
