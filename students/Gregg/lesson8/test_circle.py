import pytest
from circle import *


def test_circle_radius():
    assert(4 == Circle(4).radius)
    assert(2 == Circle(2).radius)


def test_repr():
    assert(eval( repr( Circle(4))) == Circle(4))
