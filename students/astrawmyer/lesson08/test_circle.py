import pytest
import circle

def test_radius():
    c = circle.Circle(5)
    assert c.radius == 5

def test_diameter():
    c = circle.Circle(5)
    assert c.diameter == 10
