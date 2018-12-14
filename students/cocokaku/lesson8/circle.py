#!/usr/bin/env python3
from math import pi
from functools import total_ordering

@total_ordering
class Circle:
    _radius = None
    _diameter = None
    _area = None

    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius*2
        self._area = pi*radius**2

    def __str__(self):
        return f"Circle with radius: {self._radius:.6f}"

    def __repr__(self):
        return f"Circle({self._radius})"

    def __add__(self, other):
        if type(other) != type(self):
            raise TypeError("both objects must be Circle type")
        return Circle(self._radius + other.radius)

    def __mul__(self, other):
        return Circle(self._radius * other)

    def __rmul__(self, other):
        return Circle(self._radius * other)

    def __eq__(self, other):
        return self._radius == other.radius

    def __lt__(self, other):
        return self._radius < other.radius

    @classmethod
    def from_diameter(self, diameter):
        return Circle(diameter/2)

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


