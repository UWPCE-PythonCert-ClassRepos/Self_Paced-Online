#!/usr/bin/env python3
"""
For Step 8 optional features, implemented:
(1) reflected multiplication, no other operators make sense
(2) implemented magic methods for subtraction and division
(3) implemented augmented addition, subtraction, multiplication, and division
"""
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
        return Circle(self._radius + other.radius)

    def __sub__(self, other):
        if self._radius<other.radius:
            raise ValueError("Radius cannot be less than zero")
        return Circle(self._radius - other.radius)

    def __mul__(self, other):
        return Circle(self._radius * other)

    def __truediv__(self, other):
        return Circle(self._radius / other)

    def __rmul__(self, other):
        return Circle(self._radius * other)

    def __eq__(self, other):
        return self._radius == other.radius

    def __lt__(self, other):
        return self._radius < other.radius

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __imul__(self, other):
        return self * other

    def __idiv__(self, other):
        return self / other

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


