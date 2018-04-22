from circle import Circle
from math import pi


def test_Circle():
    c = Circle(20)
    assert c.radius == 20
    assert c.diameter == 40
    c.diameter = 10
    assert c.radius == 5
    assert c.diameter == 10
    assert c.area == 5 * 5 * pi


def test_Circle_from_diameter():
    d = Circle.from_diameter(40)
    assert d.radius == 20
    assert d.diameter == 40
    assert d.area == 20 * 20 * pi


def test_str_repr():
    s = Circle(20)
    assert str(s) == 'Circle with radius: 20'
    assert repr(s) == 'Circle(20)'


def test_add_mul():
    a = Circle(1)
    b = Circle(2)
    x = a + b
    assert x.radius == 3
    assert isinstance(x, Circle)
    y = a * b
    assert y.radius == 2
    assert isinstance(y, Circle)


def test_comp():
    a = Circle(1)
    b = Circle(2)
    c = Circle(1)
    assert a < b
    assert b > a
    assert c == a


def test_sort():
    list_unsorted = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(
        0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    assert list_unsorted.sort() == list_unsorted.sort()


def test_iadd_imul():
    i = Circle(2)
    j = Circle(4)
    i += j
    assert i.radius == 6
    i *= j
    assert i.radius == 24
