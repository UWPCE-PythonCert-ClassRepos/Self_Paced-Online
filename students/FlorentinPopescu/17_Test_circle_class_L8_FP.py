# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:35:02 2019
@author: Florentin Popescu
"""

#===================LESSON_08====================

#================================================
# Part 2: Test circle class
#================================================

# imports
import pytest, importlib 
c_module = importlib.import_module("16_Circle_class_L8_FP", package = None)

#------------------------------------------------
# test geometry
def test_geometry():
    with pytest.raises(NameError):
        assert c_module.Circle.geometry(None, None) == "Input geometry must be defined and not null."
        assert c_module.Circle.geometry(None, "a") == "Input geometry must be numeric."
    with pytest.raises(ValueError):
        assert c_module.Circle.geometry(None, -1) == "Input geometry must be positive."  
        
#------------------------------------------------
# test radius initializer
def test_initializer():
    assert c_module.Circle(1).radius == 1
    
#------------------------------------------------
# test diameter
def test_diameter():
    assert c_module.Circle(1).diameter == 2
    
#------------------------------------------------
# test diameter setter
def test_diameter_setter():
    circle = c_module.Circle(1) 
    circle.diameter = 4
    assert circle.diameter == 4 and circle.radius == 2
    
#------------------------------------------------
# test area
def test_area():
    assert c_module.Circle(1).area == c_module.pi * pow(c_module.Circle(1).radius, 2)
    
#--------------------------------------------    
# test circle's radius created from diameter    
def test_from_diameter():
    assert c_module.Circle.from_diameter(2).radius == 1 

#--------------------------------------------    
# test str
def test_str():
    assert str(c_module.Circle(1)) == "Circle's radius = 1"
 
#--------------------------------------------    
# test repr 
def test_repr():
    assert repr(c_module.Circle(1)) == "Circle(1)"

#--------------------------------------------    
# test add
def test_add():
    assert (c_module.Circle(1) + c_module.Circle(2)).radius == 3

#--------------------------------------------    
# test mul
def test_mul():
    assert (c_module.Circle(1) * 2).radius == 2 

#--------------------------------------------    
# test rmul
def test_rmul():
    assert (2 * c_module.Circle(1)).radius == 2 

#--------------------------------------------    
# test lt
def test_lt():
    assert c_module.Circle(1) < c_module.Circle(2)

#--------------------------------------------    
# test gt
def test_gt():
    assert c_module.Circle(2) > c_module.Circle(1)

#--------------------------------------------    
# test eq
def test_eq():
    assert c_module.Circle(1) == c_module.Circle(1)
    
#--------------------------------------------    
# test sort circles
def test_circles_sort():
    assert sorted([c_module.Circle(3), c_module.Circle(1), c_module.Circle(2)], reverse = False) == [c_module.Circle(1), c_module.Circle(2), c_module.Circle(3)]

#--------------------------------------------    
# test iadd
def test_iadd():
    circle = c_module.Circle(1)
    circle += c_module.Circle(2)
    assert circle is not c_module.Circle(1)
    assert circle == c_module.Circle(3)
    assert circle.radius == c_module.Circle(1).radius + c_module.Circle(2).radius
    
#================================================
#--------------- END ----------------------------
#================================================

