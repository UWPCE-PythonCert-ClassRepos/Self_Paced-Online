#!/usr/bin/env python3
from math import pi


class Circle:
    _radius = None
    _diameter = None
    _area = None

    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius*2
        self._area = pi*radius**2

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._diameter

    @property
    def area(self):
        return self._area

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value/2
        self._area = pi*self._radius**2


