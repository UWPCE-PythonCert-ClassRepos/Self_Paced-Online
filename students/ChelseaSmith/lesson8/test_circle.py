#tests for Circle class done in pytest

from circle import *
import math

def test_radius():
    sample = Circle(4)
    assert sample.radius == 4


def test_diameter():
    sample = Circle(4)
    assert sample.diameter == 8


def test_diameter_setter():
    sample = Circle(4)
    sample.diameter = 4
    assert sample.radius == 2


def test_area():
    sample = Circle(4)
    areacalc = math.pi * 4 ** 2
    assert sample.area == areacalc


def test_from_diameter():
    sample = Circle.from_diameter(8)
    assert sample.radius == 4


def test_str():
    sample = Circle(4)
    assert str(sample) == "Circle with radius 4.000000"


def test_repr():
    sample = Circle(4)
    assert repr(sample) == "Circle(4)"


def test_add():
    sample1 = Circle(2)
    sample2 = Circle(4)
    sample = sample1 + sample2
    assert sample.radius == 6


def test_mul():
    sample = Circle(2)
    prodcircle = sample * 3
    assert prodcircle.radius == 6


def test_lt():
    sample1 = Circle(1)
    sample2 = Circle(2)
    assert sample1 < sample2


def test_le():
    sample1 = Circle(1)
    sample2 = Circle(2)
    assert sample1 <= sample2


def test_le2():
    sample1 = Circle(1)
    sample2 = Circle(1)
    assert sample1 <= sample2


def test_eq():
    sample1 = Circle(1)
    sample2 = Circle(1)
    assert sample1 == sample2


def test_ge():
    sample1 = Circle(2)
    sample2 = Circle(1)
    assert sample1 >= sample2


def test_ge2():
    sample1 = Circle(1)
    sample2 = Circle(1)
    assert sample1 >= sample2


def test_gt():
    sample1 = Circle(2)
    sample2 = Circle(1)
    assert sample1 > sample2


def test_ne():
    sample1 = Circle(1)
    sample2 = Circle(2)
    assert sample1 != sample2
