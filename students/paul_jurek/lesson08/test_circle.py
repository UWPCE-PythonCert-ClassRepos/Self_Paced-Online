"""test suite for circle class"""

import math
import pytest
from circle import Circle

@pytest.fixture
def example_circle():
    return Circle(4)

def test_cirle_creation(example_circle):
    """when user initiates a circle with no keyword
    and object is created with equivalent radius"""
    assert example_circle.radius == 4


def test_circle_diameter_exists():
    """when user initates a circle
    then diameter is equal to twice radius"""
    radius = 4
    c = Circle(radius)
    assert c.diameter == 2*radius
    assert c.diameter == 2*c.radius


def test_user_can_change_diameter(example_circle):
    """when user changes a circles diameter
    the radius is updated"""
    new_diameter = 10
    new_radius = new_diameter/2
    assert new_diameter != example_circle.diameter
    example_circle.diameter = new_diameter
    assert example_circle.diameter == new_diameter
    assert example_circle.radius == new_radius
    assert example_circle.area == math.pi * new_radius ** 2


def test_circle_has_correct_area(example_circle):
    """when user initiates circle
    then user can access area attribute"""
    assert example_circle.area == math.pi * example_circle.radius ** 2


def test_user_cannot_change_area_directly(example_circle):
    """when user tries to change area
    they get attribute error"""
    with pytest.raises(AttributeError):
        example_circle.area = 55


def test_circle_can_be_created_from_diameter():
    """when a user creates a circle from diameter
    a circle object is returned with correct radius"""
    c = Circle.from_diameter(8)
    assert c.radius == 4
