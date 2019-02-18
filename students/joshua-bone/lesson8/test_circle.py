from circle import Circle
import math
import pytest


# Assert that two floating point values are equal to within 7 decimal places
def assertEqualsFloat(f1, f2):
    assert math.fabs(f1 - f2) < 0.0000001


def test_radius():
    c = Circle(2)
    assert c.radius == 2


def test_diameter():
    c = Circle(2)
    assert c.diameter == 4


def test_set_diameter():
    c = Circle(2)
    c.diameter = 2
    assert c.radius == 1


def test_area():
    c = Circle(3)
    assertEqualsFloat(c.area, 9 * math.pi)


def test_area_cannot_set():
    c = Circle(2)
    with pytest.raises(AttributeError) as ae:
        c.area = 10


def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8


def test_print():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4"


def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4)"


def test_eq():
    c1 = Circle(1)
    assert c1 == Circle(1)
    assert c1 != Circle(2)


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)


def test_mult():
    c1 = Circle(3)
    assert c1 * 5 == Circle(15)
    assert 3 * c1 == Circle(9)


def test_le_ge():
    c1 = Circle(1)
    c2 = Circle(2)
    assert c1 < c2
    assert c2 > c1


def test_sort():
    circles = [Circle(2), Circle(1), Circle(3)]
    circles.sort()
    assert circles == [Circle(1), Circle(2), Circle(3)]
