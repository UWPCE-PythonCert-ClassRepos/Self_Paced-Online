from circle import Circle


def test_radius_attribute():
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    c = Circle(4)
    assert c.diameter == 8


def test_diameter_setter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1


def test_area():
    c = Circle(2)
    assert c.area == 12.566370614359172


def test_alt_constructor():
    c = Circle.from_diameter(8)
    assert c.radius == 4


def test_str():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4.000000'


def test_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'


def test_numeric():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1 + c2) == 'Circle(6)'
    assert repr(c2 * 3) == 'Circle(12)'
    assert repr(3 * c2) == 'Circle(12)'


def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert (c1 > c2) is False
    assert (c1 < c2) is True
    assert (c1 == c2) is False
    assert (c2 == c3) is True


def test_sort():
    circles = [Circle(25), Circle(3), Circle(0), Circle(1), Circle(82)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(3), Circle(25), Circle(82)]


def test_reflected():
    assert Circle(2) * 3 == 3 * Circle(2)


def test_division():
    assert repr(Circle(4)/2) == 'Circle(2)'


def test_iadd():
    c1 = Circle(2)
    c2 = Circle(4)
    c1 += c2
    assert repr(c1) == 'Circle(6)'

