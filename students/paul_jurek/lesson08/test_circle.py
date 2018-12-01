"""test suite for circle class"""

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