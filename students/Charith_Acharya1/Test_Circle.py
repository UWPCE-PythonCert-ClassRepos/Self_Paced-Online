# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:01:15 2019

@author: acharch
"""

import pytest
import os
import math
os.chdir("C:/U of W")

from Circle_excercise import Circle

#Testing radius
def test_radius():
    c=Circle(2)
    assert c.radius == 2
    
test_radius()
    
#Testing diameter
def test_diameter():
    c = Circle(2)
    assert c.diameter == 4
    
test_diameter()
    
#Testing diameter setter
def test_dia_set():
    c=Circle(10)
    c.diameter = 4
    assert c.diameter == 4
    assert c.radius == 2
    
test_dia_set()
    
# Testing  area
def test_area():
    c=Circle(2)
    area = math.pi * 2**2
    assert c.circle_area == area

test_area()  
    
def test_circle_from_diameter():
    c=Circle.circle_from_diameter(20)
    area1 = math.pi * 10 * 10
    assert c.area_dia == area1
    
test_circle_from_diameter()   

