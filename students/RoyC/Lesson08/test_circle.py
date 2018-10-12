#!/usr/bin/env python3

from circle import Circle
from math import pi

def test_size():
    # test constructor and setters for size
    c = Circle(5)
    assert(c.radius == 5)
    assert(c.diameter == 10)
    assert(c.area == (25 * pi))
    
    c.radius = 8
    assert(c.radius == 8)
    assert(c.diameter == 16)
    assert(c.area == (64 * pi))
    
    c.diameter = 20
    assert(c.radius == 10)
    assert(c.diameter == 20)
    assert(c.area == (100 * pi))
    
    c2 = Circle.from_diameter(40)
    assert(c2.radius == 20)
    assert(c2.diameter == 40)
    assert(c2.area == 400 * pi)
    
    # confirm area not settable
    try:
        c2.area = 200
    except AttributeError:
        pass
    else:
        assert(False)