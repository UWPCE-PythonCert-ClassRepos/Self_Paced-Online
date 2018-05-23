import pytest
from circle import Circle


def test_circle_radius():
    with pytest.raises(Exception) as excinfo:
        c = Circle()
    assert str(excinfo.value) == "__init__() missing 1 required positional "\
                                 "argument: 'radius'"

    c = Circle(100)
    assert c.radius == 100


def test_circle_diameter():
    c = Circle(100)
    assert c.radius == 100
    assert c.diameter == 200

    c.diameter = 50
    assert c.radius == 25
    assert c.diameter == 50


def test_circle_area():
    c = Circle(2)
    assert c.area == 12.566370614359172

    with pytest.raises(Exception) as excinfo:
        c = Circle(2)
        c.area = 16
    assert str(excinfo.value) == "can't set attribute"


def test_circle_alt_constructor():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_circle_str(capsys):
    c = Circle(4)
    print(c)
    captured = capsys.readouterr()
    assert captured.out == "Circle with radius: 4\n"

    assert repr(c) == "Circle(4)"

    d = eval(repr(c))

    assert d.radius == 4
    assert d.diameter == 8


def test_circle_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)


def test_circle_mul():
    c1 = Circle(4)
    assert c1 * 3 == Circle(12)


def test_circle_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 > c2) is False
    assert (c1 < c2) is True
    assert (c1 == c2) is False

    c3 = Circle(4)
    assert (c2 == c3) is True


def test_circle_sort():
    circles = [Circle(6),
               Circle(7),
               Circle(8),
               Circle(4),
               Circle(0),
               Circle(2),
               Circle(3),
               Circle(5),
               Circle(9),
               Circle(1)]
    circles.sort(key=Circle.sort_key)
    assert circles == [Circle(0),
                       Circle(1),
                       Circle(2),
                       Circle(3),
                       Circle(4),
                       Circle(5),
                       Circle(6),
                       Circle(7),
                       Circle(8),
                       Circle(9)]
