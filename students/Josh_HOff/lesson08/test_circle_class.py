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
    print(c1 + c2)
    assert False