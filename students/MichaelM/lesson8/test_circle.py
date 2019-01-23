# open a terminal window
# cd lesson8
# pytest test_circle.py

import pytest
import circle_class as cc



"""
assert that the circle class instantiates with the correct radius
"""

def test_1():
    c = cc.Circle(10)
    assert c.radius == 10

"""
assert that the radius is required
"""

def test_2():
    try:
        c = cc.Circle()
    except TypeError as error:
        s = str(error)
    assert "missing 1 required positional argument: 'usr_radius'" in s

"""
assert that the diameter is correct
"""
def test_3():
    c = cc.Circle(10)
    assert c.diameter == 20


"""
assert that the user can set the diameter
"""
def test_4():
    c = cc.Circle(10)
    c.diameter = 10
    assert c.diameter == 10

"""
assert that the user can get the area
"""
def test_5():
    c = cc.Circle(10)
    assert c.area == 628.0

"""
assert that the user can not set the area
"""
def test_6():
    c = cc.Circle(10)
    try:
        c.area = 10
    except AttributeError as error:
        s = str(error)
    assert "can't set attribute" in s

"""
assert that the alternate constructor to create a circle from diameter functions
"""
def test_7():
    c = cc.Circle.from_diameter(10)
    assert str(c) == "Circle with radius: 5.0"


"""
assert that class can be printed
"""
def test_8(capfd):
    c = cc.Circle.from_diameter(10)
    test_string = ""
    print(c)
    out, err = capfd.readouterr()
    if "Circle with radius: 5.0" in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that __repr__ is in the class
"""
def test_9():
    c = cc.Circle.from_diameter(10)
    assert repr(c) == "Circle(5.0)"

"""
assert that the class can sum
"""
def test_10(capfd):
    c1 = cc.Circle(2)
    c2 = cc.Circle(4)
    test_string = ""
    print(c1 + c2)
    out, err = capfd.readouterr()
    if "Circle(6.0)" in out:
        test_string = "success"
    assert test_string == "success"

"""
assert that the class can muliply
"""
def test_11(capfd):
    c1 = cc.Circle(2)
    c2 = cc.Circle(4)
    test_string = ""
    print(c2 * 3)
    out, err = capfd.readouterr()
    if "Circle(12.0)" in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that the class can muliply (reversed)
"""
def test_11(capfd):
    c1 = cc.Circle(2)
    c2 = cc.Circle(4)
    test_string = ""
    print(3 * c2)
    out, err = capfd.readouterr()
    if "Circle(12.0)" in out:
        test_string = "success"
    assert test_string == "success"



"""
assert that comparison operators function correctly
"""
def test_11(capfd):
    c1 = cc.Circle(2)
    c2 = cc.Circle(4)
    test_string = ""
    print(c1 > c2)
    out, err = capfd.readouterr()
    if "False" in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that equality functions correctly
"""
def test_12(capfd):
    c1 = cc.Circle(2)
    c2 = cc.Circle(4)
    test_string = ""
    print(c1 == c2)
    out, err = capfd.readouterr()
    if "False" in out:
        test_string = "success"
    assert test_string == "success"


"""
assert that sort functions correctly
"""

def test_12(capfd):
    circles = [cc.Circle(4), cc.Circle(2), cc.Circle(3), cc.Circle(1)]
    test_string = ""
    circles.sort()
    print(circles)
    out, err = capfd.readouterr()
    if "[Circle(1.0), Circle(2.0), Circle(3.0), Circle(4.0)]" in out:
        test_string = "success"
    assert test_string == "success"









