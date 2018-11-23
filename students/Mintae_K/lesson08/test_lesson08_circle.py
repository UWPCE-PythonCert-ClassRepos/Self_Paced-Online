from math import pi
import lesson08_circle as cr


# Test Step 1
def test_circle_create():
    c = cr.Circle(4)
    print(c.radius)
    assert c.radius == 4
    # assert False


# Test Step 2
def test_circle_diameter():
    c = cr.Circle(4)
    print(c.diameter)
    assert c.diameter == 8


# Test Step 3
def test_circle_dia_set():
    c = cr.Circle(4)
    c.diameter = 2
    print(c.diameter)
    print(c.radius)
    assert c.diameter == 2
    assert c.radius == 1


# Test Step 4
def test_area_calc():
    c = cr.Circle(2)
    print(c.area)
    assert c.area == (pi * 2 ** 2)
    try:
        c.area = 42
    except AttributeError:
        print('you can not set area')


# Test Step 5
def test_from_dia():
    c = cr.Circle.from_diameter(8)
    print(c.diameter)
    print(c.radius)
    assert c.diameter == 8
    assert c.radius == 4


# Test Step 6
def test_print():
    c = cr.Circle(4)
    print(c)
    # assert print(c) == "Circle with radius: 4.000000"
    assert repr(c) == ("'Circle(4)'")
    assert eval(repr(c)) == ('Circle(4)')


# Test Step 7
def test_add_mul_circles():
    c1 = cr.Circle(2)
    c2 = cr.Circle(4)
    d = c1 + c2
    assert eval(repr(d)) == 'Circle(6)'
    d = c2 * 3
    assert eval(repr(d)) == 'Circle(12)'
    d = 3 * c2
    assert eval(repr(d)) == 'Circle(12)'


# Test Step 8
def test_compare_cir():
    c1 = cr.Circle(2)
    c2 = cr.Circle(4)
    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c1 == c2) == False
    c3 = cr.Circle(4)
    assert (c2 == c3) == True

    c4 = cr.Circle(8)
    c5 = cr.Circle(1)
    c6 = cr.Circle(44)
    c7 = cr.Circle(23)
    c8 = cr.Circle(13)

    circles = [c1, c2, c3, c4, c5, c6, c7, c8]
    circles.sort(key=cr.Circle.sort_key)

    print (circles)
    assert eval(repr(circles[0])) == ('Circle(1)')
    assert eval(repr(circles[-1])) == ('Circle(44)')
    assert False
