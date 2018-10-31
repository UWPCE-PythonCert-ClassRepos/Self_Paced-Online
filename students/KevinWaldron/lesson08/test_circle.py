#!/usr/bin/env python3

from circle import Circle

def test_circle():
    c = Circle(5)
    assert(c.radius == 5)
    assert(c.diameter == 10)

    # verify out of range values fail
    try:
        Circle(0)
    except ValueError:
        pass
    else:
        assert(False)
    try:
        c.radius = -1
    except ValueError:
        pass
    else:
        assert(False)

def test_diameter():
    c = Circle(5)
    c.diameter = 20
    assert(c.radius == 10)
    assert(c.diameter == 20)

    c = Circle.from_diameter(42)
    assert(c.radius == 21)
    assert(c.diameter == 42)

    try:
        c.diameter = -1
    except ValueError:
        pass
    else:
        assert(False)

def test_area():
    c = Circle(10)
    assert(c.area == 314.1592653589793)

    # Verify area isn't settable
    try:
        c2 = Circle(2)
        c2.area = 42
    except AttributeError:
        pass
    else:
        assert(False)

def test_str():
    c = Circle(10)
    assert(str(c) == "Circle with radius 10.00")

def test_repr():
    c = Circle(10)
    assert(repr(c) == "Circle(10)")

def test_numeric():
    c = Circle(10)
    c2 = Circle(5)
    assert(repr(c + c2) == "Circle(15)")
    assert(repr(c + 2) == "Circle(12)")
    assert(repr(2 + c) == "Circle(12)")
    assert(repr(c * c2) == "Circle(50)")
    assert(repr(c * 2) == "Circle(20)")
    assert(repr(2 * c) == "Circle(20)")
    assert(repr(c / c2) == "Circle(2.0)")
    assert(repr(c / 2) == "Circle(5.0)")
    assert(repr(20 / c) == "Circle(2.0)")
    assert(repr(c - c2) == "Circle(5)")
    assert(repr(c - 2) == "Circle(8)")
    assert(repr(12 - c) == "Circle(2)")
    try:
        2 - c
    except ValueError:
        pass
    else:
        assert(False)

def test_comparisons():
    c = Circle(10)
    c2 = Circle(5)

    assert(c2 < c)
    assert(c2 <= c)
    assert(c > c2)
    assert(c >= c2)
    assert(c != c2)
    c = Circle(5)
    assert(c == c2)
    assert(c2 <= c)
    assert(c >= c2)

def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert(circles == [Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)])

def test_augmented_assignment():
    c = Circle(10)
    c2 = c
    c += 10
    assert(c.radius == 20)
    assert(c2 is c)
    c -= 10
    assert(c.radius == 10)
    assert(c2 is c)
    c *= 2
    assert(c.radius == 20)
    assert(c2 is c)
    c /= 2
    assert(c.radius == 10)
    assert(c2 is c)
    c2 = Circle(2)
    c3 = c2
    c += c2
    assert(c.radius == 12)
    assert(c3 is c2)
    c -= c2
    assert(c.radius == 10)
    assert(c3 is c2)
    c *= c2
    assert(c.radius == 20)
    assert(c3 is c2)
    c /= c2
    assert(c.radius == 10)
    assert(c3 is c2)


