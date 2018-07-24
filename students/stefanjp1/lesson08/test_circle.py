import pytest
from circle import *

def test_radius():
    assert Circle(the_radius = 12).radius == 12
    
def test_diameter():
    assert Circle(the_radius = 12).diameter == 24
    
def test_diameter_setter():
    td = Circle(the_radius = 12) 
    td.diameter = 4
    assert td.radius == 2

def test_area():
    assert Circle(the_radius = 2).area ==  12.566370614359172
    with pytest.raises(Exception):
        Circle(the_radius = 2).area =  12

def test_diameter_setter_area():
    td = Circle(the_radius = 12) 
    td = td.from_diameter(4)
    assert td.area ==  12.566370614359172
    
def test_6():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'
    
def test_add_mul():
    a = Circle(4) + Circle(4)
    assert a.radius == Circle(8).radius
    
    assert repr(a * 2) == repr(Circle(16))

def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    
    circles.sort()
    
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]