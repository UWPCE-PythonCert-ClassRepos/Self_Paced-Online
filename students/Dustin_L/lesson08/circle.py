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
        """Creates a circle from a diameter"""
        return cls(diameter / 2)

    @property
    def area(self):
        """Returns the circle's area"""
        return self._area

    @property
    def diameter(self):
        """Returns the circle's diameter"""
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        """Sets the circle's diameter

        Args:
            value: diameter value

        Raises:
            ValueError: If value is less than 0
        """
        if value < 0:
            raise ValueError

        if self._diameter != value:
            self._diameter = value
            self._radius = value / 2
            self._area = math.pi * self._radius**2

    @property
    def radius(self):
        """Returns the circle's radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Sets the circle's radius

        Args:
            value: radius value

        Raises:
            ValueError: If value is less than 0
        """
        if value < 0:
            raise ValueError

        if self._radius != value:
            self._radius = value
            self._diameter = value * 2
            self._area = math.pi * self._radius**2

    def sort_key(self):
        """Key for efficient Circle sort operations"""
        return self._radius
