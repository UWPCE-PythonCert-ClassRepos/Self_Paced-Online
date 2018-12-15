from circle import Circle


# STEP 1 TESTS
def test_circle_init():
    c = Circle(4)
    assert c.radius == 4


def test_circle_init_no_parameters_error():
    msg = ""
    try:
        Circle()
    except TypeError as e:
        msg = e.args[0]
    finally:
        assert msg == "__init__() missing 1 required positional argument: 'radius'"


# STEP 2 TESTS
def test_circle_diameter():
    c = Circle(4)
    assert c.diameter == 8


# STEP 3 TESTS
def test_circle_change_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1


# STEP 4 TESTS
def test_circle_area():
    c = Circle(2)
    assert round(c.area, 3) == 12.566


def test_circle_change_area_error():
    msg = ""
    c = Circle(2)
    try:
        c.area = 42
    except AttributeError as e:
        msg = e.args[0]
    assert msg == "can't set attribute"


# STEP 5 TESTS
def test_circle_alternate_constructor():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


# STEP 6 TESTS
def test_circle_str_method():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4.000000"


def test_circle_repr_method():
    c = Circle(4)
    assert repr(c) == "Circle(4)"


def test_circle_repr_eval():
    c = Circle(4)
    d = eval(repr(c))
    assert str(c) == str(d)


# STEP 7 TESTS
def test_circle_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1+c2) == "Circle(6)"


def test_circle_multiply():
    c = Circle(4)
    assert repr(c*3) == "Circle(12)"


def test_circle_multiply_reversed():
    c = Circle(4)
    assert repr(3*c) == "Circle(12)"


# STEP 8 TESTS
def test_circle_greater_than():
    c1 = Circle(2)
    c2 = Circle(4)
    assert not c1 > c2


def test_circle_less_than():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 < c2


def test_circle_equal():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert c1 != c2
    assert c2 == c3


def test_circle_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
               Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    expected = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
                Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
    assert circles == expected


# STEP 8 OPTIONAL FEATURES TESTS
def test_circle_reflection():
    assert Circle(4)*3 == 3*Circle(4)


def test_circle_augmented_addition():
    c1 = Circle(2)
    c1 += Circle(2)
    assert c1.radius == 4


def test_circle_augmented_multiplication():
    c1 = Circle(2)
    c1 *= 3.1
    assert c1.radius == 6.2


def test_circle_subtraction():
    assert (Circle(2) - Circle(1)).radius == 1


def test_circle_division():
    assert (Circle(2) / 5).radius == 0.4


def test_circle_augmented_subtraction():
    c = Circle(2)
    c -= Circle(1)
    assert c.radius == 1


def test_circle_augmented_division():
    c = Circle(2)
    c /= 5
    assert c.radius == 0.4

