#!/usr/bin/env python3
"""Circle Module"""

import math


class Circle:
    """Circle Class"""
    def __init__(self, radius):
        if radius < 0:
            raise ValueError

        self._radius = radius
        self._diameter = 2 * radius
        self._area = math.pi * radius**2

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius + other.radius)
        return Circle(self._radius + other)

    def __eq__(self, other):
        return self._radius == other.radius

    def __ge__(self, other):
        return self._radius >= other.radius

    def __gt__(self, other):
        return self._radius > other.radius

    def __le__(self, other):
        return self._radius <= other.radius

    def __lt__(self, other):
        return self._radius < other.radius

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius * other.radius)
        return Circle(self._radius * other)

    def __radd__(self, other):
        return Circle(self._radius + other)

    def __repr__(self):
        return f'Circle({self._radius})'

    def __rmul__(self, other):
        return Circle(self._radius * other)

    def __rsub__(self, other):
        return Circle(other - self._radius)

    def __str__(self):
        return (f'Circle with radius: {self._radius}\n'
                f'            diameter: {self._diameter}\n'
                f'            area: {self._area}')

    def __sub__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius - other.radius)
        return Circle(self._radius - other)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def area(self):
        return self._area

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError

        if self._diameter != value:
            self._diameter = value
            self._radius = value / 2
            self._area = math.pi * self._radius**2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError

        if self._radius != value:
            self._radius = value
            self._diameter = value * 2
            self._area = math.pi * self._radius**2
