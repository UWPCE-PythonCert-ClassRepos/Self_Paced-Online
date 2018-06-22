from circle import Circle

def test_init():
    c = Circle(4)
    assert (c.radius == 4) is True

def test_diameter():
    c = Circle(4)
    assert (c.diameter == 8) is True
    assert (c.radius == 4) is True
    c.diameter = 2
    assert (c.diameter == 2) is True
    assert (c.radius == 1) is True

def test_area():
    c = Circle(2)
    assert (c.area == 12.566370614359172) is True

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert (c.diameter == 8) is True
    assert (c.radius == 4) is True

def test_str_():
    c = Circle(4)
    assert (str(c) == 'Circle with radius: 4') is True

def test_repr_():
    c = Circle(4)
    assert (repr(c) == 'Circle(4)') is True

def test_add_():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 + c2 == Circle(6)) is True

def test_mul_():
    c2 = Circle(4)
    assert (c2*3 == Circle(12)) is True

def test_ls_():
    c1 = Circle(2)
    c2 = Circle(4)
    assert ((c1 > c2) == False) is True
    assert ((c1 < c2) == True) is True
    assert ((c1 == c2) == False) is True
    c3 = Circle(4)
    assert ((c3 == c2) == True) is True

def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert (circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]) is True
