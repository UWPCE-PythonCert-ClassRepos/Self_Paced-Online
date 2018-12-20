#-------------------------------------------------#
# Title: Circle Class
# Dev:   LDenney
# Date:  December 9, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 12/09/18, Started Circle Class Assignment
#-------------------------------------------------#

from circle_class import *

########
# Step 1
########

def test_init1():

    c = Circle(4)

def test_init2():
    try:
        c = Circle()
    except Exception as e:
        assert type(e) is TypeError


def test_radius():

    c = Circle(4)

    assert c.radius == 4

########
# Step 2
########

def test_diameter():
    c = Circle(4)

    assert c.diameter == 8

########
# Step 3
########

def test_diameter_changeradius():
    c = Circle(4)
    c.diameter = 2

    assert c.diameter == 2
    assert c.radius == 1

########
# Step 4
########

def test_area():
    c = Circle(2)

    assert c.area == 12.566370

def test_area_attribute_change():
    c = Circle(2)
    try:
        c.area = 4
    except Exception as e:
        assert type(e) is AttributeError

########
# Step 5
########

def test_diameter_constructor():
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4

########
# Step 6
########

def test_str():
    c = Circle(4)

    assert str(c) == 'Circle with radius: 4.0'

def test_repr():
    c = Circle(4)

    assert repr(c) == 'Circle(4.0)'

########
# Step 7
########

def test_add():
    c1 = Circle(2)

    c2 = Circle(4)

    c3 = c1 + c2
    assert repr(c3) == 'Circle(6.0)'

def test_add2():
    c1 = Circle(2)
    c2 = c1 + 3
    assert repr(c2) == 'Circle(5.0)'

def test_reverseadd():
    c1 = Circle(3)
    c2 = 2 + c1

    assert repr(c2) == 'Circle(5.0)'

def test_multiply1():
    c1 = Circle(2)

    c2 = c1 * 2
    assert repr(c2) == 'Circle(4.0)'

def test_multiply2():
    c1 = Circle(4)

    c2 = 2 * c1
    assert repr(c2) == 'Circle(8.0)'

########
# Step 8
########
def test_gt():
    c1 = Circle(2)
    c2 = Circle(4)
    assert not c1 > c2

def test_lt():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 < c2

def test_eq():
    c1 = Circle(2)
    c2 = Circle(4)
    assert not c1 == c2

def test_eq2():
    c2 = Circle(4)
    c3 = Circle(4)
    assert c2 == c3

def test_sort():
    circles = [Circle(6), Circle(7), Circle(8),
    Circle(4), Circle(0), Circle(2), Circle(3),
    Circle(5), Circle(9), Circle(1)]

    circles.sort()

    assert repr(circles) == '[Circle(0.0), Circle(1.0), Circle(2.0), Circle(3.0), Circle(4.0), Circle(5.0), Circle(6.0), Circle(7.0), Circle(8.0), Circle(9.0)]'

#################
# Step 9 Optional
#################

def test_reflected():
    c1 = Circle(2)

    assert c1 * 3 == 3 * c1

def test_iadd_2circles():
    c1 = Circle(2)
    c2 = Circle(3)

    c1 += c2
    assert repr(c1) == 'Circle(5.0)'

def test_iadd_noncircle():
    c1 = Circle(2)
    c1 += 5

    assert repr(c1) == 'Circle(7.0)'

def test_imul_2circles():
    c1 = Circle(2)
    c2 = Circle(3)

    c1 *= c2
    assert repr(c1) == 'Circle(6.0)'

def test_imul_noncircle():
    c1 = Circle(2)
    c1 *= 5

    assert repr(c1) == 'Circle(10.0)'

def test_div():
    c1 = Circle(4)
    c2 = c1 / 2

    assert repr(c2) == 'Circle(2.0)'

def test_idiv():
    c1 = Circle(6)
    c1 /= 3

    assert repr(c1) == 'Circle(2.0)'
