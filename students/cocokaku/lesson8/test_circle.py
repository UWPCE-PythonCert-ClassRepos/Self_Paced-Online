from circle import Circle


# STEP 1 TESTS
def test_circle_init():
    c = Circle(4)
    assert c.radius == 4


def test_circle_init_no_parameters_error():
    msg = ""
    try:
        c = Circle()
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
