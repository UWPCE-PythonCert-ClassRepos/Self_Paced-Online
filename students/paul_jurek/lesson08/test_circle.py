"""test suite for circle class"""

import math
import pytest
from circle import Circle


@pytest.fixture
def example_circle():
    return Circle(4)


@pytest.fixture
def small_circle():
    return Circle(2)


@pytest.fixture
def big_circle():
    return Circle(20)


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


def test_str_gives_correct_output(example_circle):
    """when user call str method
    the correct output is called"""
    assert example_circle.__str__() == 'Circle with radius: 4'


def test_repr_gives_correct_output(example_circle):
    """when user calls repr
    then it gives correct response"""
    assert repr(example_circle) == f'Circle({example_circle.radius})'


def test_circle_can_be_created_from_repr(example_circle):
    """when a user initiates a circle from a repr
    it creates a circle"""
    d = eval(repr(example_circle))
    assert d.radius == example_circle.radius


def test_circle_addition(example_circle):
    """given two circles are added
    then the radius is added and a new circle is returned"""
    new_circle = example_circle + example_circle
    assert new_circle.radius == example_circle.radius * 2


def test_circle_can_grow_with_added_number(example_circle):
    """given a circle
    when someone adds a number
    the circle radius grows"""
    old_radius = example_circle.radius
    example_circle + old_radius
    assert example_circle.radius == old_radius * 2
    assert example_circle.diameter == example_circle.radius * 2


def test_circle_multiplies_by_num(example_circle):
    """give a circle
    when multiplied by number
    resulting radius increases by that amount"""
    old_radius = example_circle.radius
    example_circle * 2
    assert example_circle.radius == old_radius * 2
    assert example_circle.diameter == example_circle.radius * 2

    2 * example_circle
    assert example_circle.radius == old_radius * 4
    assert example_circle.diameter == example_circle.radius * 2


def test_circle_greater_than_comparison(small_circle, big_circle):
    assert ~(small_circle > big_circle)
    assert small_circle < big_circle


def test_circle_greater_than_equal_comparison(small_circle, big_circle):
    assert ~(small_circle >= big_circle)
    assert small_circle <= big_circle
    assert small_circle >= small_circle
    assert big_circle <= big_circle


def test_equal_circl_comparison(small_circle, big_circle):
    assert ~(small_circle == big_circle)
    assert ~(big_circle == small_circle)
    assert small_circle == small_circle
    assert big_circle == big_circle


def test_circle_sorting(small_circle, big_circle, example_circle):
    circles = [big_circle, small_circle, example_circle]
    circles.sort()
    assert circles == [small_circle, example_circle, big_circle]


def test_reflected_numerics(example_circle):
        """given a circle and object
        if you multiply them relectivelly
        they return same thing"""
        assert example_circle * 3 == 3 * example_circle


def test_regular_division(example_circle):
        """given user divides with one operator
        then new circle created with modified radius"""
        new_circle = example_circle / 2
        assert new_circle.radius == example_circle.radius / 2


def test_error_raised_on_division_with_0_or_negative_inputs(example_circle):
        """when user divides by 0 or negative number
        an input error is raised"""
        with pytest.raises(ValueError):
                example_circle / -1
                example_circle / 0


def test_self_division(example_circle):
    """when divided by with /=
    the current object is modified"""
    original_radius = example_circle.radius
    example_circle /= 2
    assert original_radius / 2 == example_circle.radius
