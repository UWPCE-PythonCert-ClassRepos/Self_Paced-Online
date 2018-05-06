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
