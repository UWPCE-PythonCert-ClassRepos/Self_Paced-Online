from circle import *
from math import pi
import pytest


c = Circle(10)
d = Circle(5)


def test_circle():
	assert isinstance(c, Circle)
	assert isinstance(d, Circle)

def test_radius():
	assert c.radius == 10

def test_diameter():
	assert c.diameter == 20

def test_area():
	assert c.area ==  math.pi * c.radius**2

def test__mul__():
	c = Circle(10)
	d = Circle(5)
	assert c * d == 50
	assert c * 5 == 50

def test__add__():
	assert c + d == 15
	assert d + 10 == 15

def test_comparissons():
	assert c > d
	assert d < c
	assert d <= c
	assert c >= d
	assert c != d

def test_sort():

	
	print(list.sort())

def test_sphere():
	sp = Sphere(50)
	assert isinstance(sp, Sphere)
	assert sp.area == (4 * math.pi * 50**2)
	assert sp.volume == ((4/3) * math.pi * 50**3)

	





