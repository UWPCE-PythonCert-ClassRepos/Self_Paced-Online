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
        
    # confirm area with negative radius not allowed
    try:
        c_neg = Circle(-4)
    except ValueError:
        pass
    else:
        assert(False)
        
def test_operators():
    # test the various operators on circles
    c1 = Circle(5)
    c2 = Circle(3)
    c3 = c1 + c2
    assert(c3.radius == 8)
    c4 = c1 + 7
    assert(c4.radius == 12)
    c5 = c1 * c2
    assert(c5.radius == 15)
    c6 = c2 * 2
    assert(c6.radius == 6)
    c7 = c4/c6
    assert(c7.radius == 2)
    c8 = c3/2
    assert(c8.radius == 4)
    c9 = 2 + c1
    assert(c9.radius == 7)
    c10 = 9 - c2
    assert(c10.radius == 6)
    c11 = 3 * c1
    assert(c11.radius == 15)
    c12 = 12/c2
    assert(c12.radius == 4)
    
def test_aug_operators():
    # test augmented operators
    c1 = Circle(4)
    c1 += 6
    assert(c1.radius == 10)
    c2 = Circle(5)
    c2 += c1
    assert(c2.radius == 15)
    c2 -= 2
    assert(c2.radius == 13)
    c2 -= c1
    assert(c2.radius == 3)
    c2 *= 3
    assert(c2.radius == 9)
    c2 *= c1
    assert(c2.radius == 90)
    c2 /= 9
    assert(c2.radius == 10)
    c2 /= c1
    assert(c2.radius == 1)
    
def test_comparators():
    # test the comparison operators for circles
    c1 = Circle(3)
    c2 = Circle.from_diameter(6)
    c3 = Circle(8)
    c4 = Circle(12)
    
    assert(c1 < c3)
    assert(c2 == c1)
    assert(c4 > c3)
    
def test_sort():
    circles = [Circle(9), Circle(1), Circle(4), Circle(3), Circle(7), Circle(2)]
    circles.sort()
    assert(circles == [Circle(1), Circle(2), Circle(3), Circle(4), Circle(7), Circle(9)])