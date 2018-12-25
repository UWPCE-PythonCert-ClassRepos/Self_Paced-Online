"""
Author: Alyssa Hong
Date: 12/18/2018
Update:
Lesson8 Assignments > The goal is to create a class that represents a simple circle.
"""



#!/usr/bin/env python3

from math import pi


class Circle:
    def __init__(self, value):
        self._radius = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError('Diameter cannot be negative')
        self._radius = value / 2

    @property
    def area(self):
        pi_calc = (self._radius ** 2) * pi
        return "{:.5f}".format(pi_calc)

    @classmethod
    def from_diameter(self, value):
        return Circle(value / 2)

    def __str__(self):
        return "Circle with radius: {:.1f}".format(self._radius)

    def __repr__(self):
        return "Circle({})".format(self._radius)

    def __add__(self, value):
        return Circle(self._radius + value._radius)

    def __multi__(self, value):
        multi_radius = self._radius * value._radius
        return multi_radius

    def __eq__(self, value):
        return self._radius == value._radius

    def __ne__(self, value):
        return self._radius != value._radius

    def __lt__(self, value):
        return self._radius < value._radius

    def __gt__(self, value):
        return self._radius > value._radius


c = Circle(4)
print(c.radius)
print(c.diameter)
print(c.area)
print(c)
print(Circle(6))

circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2),
           Circle(3), Circle(5), Circle(9), Circle(1)]
print(circles)

circles.sort()
print(circles)
