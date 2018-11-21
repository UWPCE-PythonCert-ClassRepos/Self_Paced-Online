import io
import pytest

from circle_class import *


def test_radius():
    c = Circle(40)
    assert c.radius == 40
    
    
def test_diameter():
    c = Circle(80)
    assert c.diameter == 160

    
def test_edit_radius():
    c = Circle(30)
    assert c.radius == 30
    assert c.diameter == 60
    c.radius = 40
    assert c.radius == 40
    assert c.diameter == 80

    
def test_edit_diameter():
    c = Circle(50)
    assert c.radius == 50
    assert c.diameter == 100
    c.diameter = 300
    assert c.radius == 150
    assert c.diameter == 300
    

def test_area():
    c = Circle(50)
    assert round(c.area, 4) == 7853.9816
    
    
def test_editing_area():
    c = Circle(50)
    c.radius = 40
    assert round(c.area, 4) == 5026.5482
    c.diameter = 150
    assert round(c.area, 4) == 17671.4587
    with pytest.raises(AttributeError):
        c.area = 50


def test_from_diameter_method():
    c = Circle.from_diameter(80)
    assert c.radius == 40
    assert c.diameter == 80
    assert round(c.area, 4) == 5026.5482
    
    
def test_addition_method():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)

    
def test_addition_with_from_diameter_method():
    c1 = Circle.from_diameter(20)
    c2 = Circle(15)
    assert c1 + c2 == Circle(25)
    
    
def test_multiplication():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c2 * 3 == Circle(12)
    assert 3 * c2 == Circle(12)
     
    
def test_less_than():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 < c2

    
def test_greater_than():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c2 > c1
    
    
def test_equals():
    c1 = Circle(10)
    c2 = Circle(10)
    assert c1 == c2
    
    
def test_less_than_equals():
    c1 = Circle(5)
    c2 = Circle(8)
    assert c1 <= c2
    c2 = Circle(5)
    assert c1 <= c2
    
    
def test_greater_than_equals():
    c1 = Circle(5)
    c2 = Circle(8)
    assert c2 >= c1
    c2 = Circle(5)
    assert c2 >= c1
    
    
def test_not_equals():
    c1 = Circle(10)
    c2 = Circle(11)
    assert c1 != c2
    
    
