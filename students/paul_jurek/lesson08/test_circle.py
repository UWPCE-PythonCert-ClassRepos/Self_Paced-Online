"""test suite for circle class"""
from circle import Circle


def test_cirle_creation():
    """when user initiates a circle with no keyword
    and object is created with equivalent radius"""
    c = Circle(4)
    assert c.radius == 4


def test_circle_diameter_exists():
    """when user initates a circle
    then diameter is equal to twice radius"""
    radius = 4
    c = Circle(radius)
    assert c.diameter == 2*radius
    assert c.diameter == 2*c.radius
