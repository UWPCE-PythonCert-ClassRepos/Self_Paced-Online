"""test suite for circle class"""
from circle import Circle

def test_cirle_creation():
    """when user initiates a circle with no keyword
    and object is created with equivalent radius"""
    c = Circle(4)
    assert c.radius == 4