import pytest
from circle import *


def test_circle_radius():
    assert(4 == Circle(4).radius)
    assert(2 == Circle(2).radius)
    with pytest.raises(ValueError):
        Circle(-1)

def test_circle_diameter():
    assert(8 == Circle(4).diameter)
    assert(4 == Circle(2).diameter)

def test_repr():
    assert(eval( repr( Circle(4))) == Circle(4))
