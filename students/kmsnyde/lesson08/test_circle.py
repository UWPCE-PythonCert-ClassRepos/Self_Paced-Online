# -*- coding: utf-8 -*-
"""
Created on Wed May  9 18:43:05 2018

@author: Karl M. Snyder
"""

from circle import Circle

def test_1():
    c = Circle(4)
    assert isinstance(c, Circle)
    assert c.radius == 4
test_1()
    
def test_2():
    c = Circle(4)
    assert c.diameter == 8
test_2()
    
def test_3():
    c = Circle(4)
    c.diameter = 22
    assert c.diameter == 22
    assert c.radius == 11
test_3()

def test_4():
    c = Circle(3)
    assert c.area == 28.27
test_4()

def test_5():
    c = Circle.from_diameter(22)
    assert c.diameter == 22
test_5()
    
def test_7():
    c1 = Circle(4)
    c2 = Circle(5)
    assert c1 + c2 == 9
    assert c1 * c2 == 20
    assert c1 * 4 == 16
    assert 10 * c1 == 40
test_7()

def test_8():
    c1 = Circle(4)
    c2 = Circle(5)
    c3 = Circle(5)
    c4 = Circle(8)
    c5 = Circle(10)
    c6 = Circle(20)
    c7 = Circle(30)
    assert c1 <= c2
    assert c2 >= c1
    assert c2 == c3
    circle = list([c1,c2,c3,c4,c5,c6,c7])
    circle.sort()
    assert circle[-1] == Circle(30)
    circle.sort(reverse=True)
    assert circle[-1] == Circle(4)
test_8()
    