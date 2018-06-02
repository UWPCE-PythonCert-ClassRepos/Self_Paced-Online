#!/usr/bin/env python3
"""
Lesson 08 Assignment - Create a Circle Class
"""
from math import pi


class Circle:
    """Class for Circle - STEP ONE"""

    def __init__(self, radius):
        if radius is not None and radius < 0:
            raise ValueError('Radius must be more than zero')

        self._radius = radius
        self._diameter = 2 * radius
        self._area = pi * radius**2
        self._perimeter = 2 * self._radius * pi

    def __str__(self):
        """Adding str method to circle class - STEP SIX"""
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        """Adding repr method to circle class - STEP SIX"""
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        """Adding add method to circle class - STEP SEVEN"""
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return Circle(self.radius + other)

    def __sub__(self, other):
        """Adding add method to circle class - STEP SEVEN"""
        if isinstance(other, Circle):
            return Circle(self.radius - other.radius)
        return Circle(self.radius - other)

    def __mul__(self, other):
        """Adding add method to circle class - STEP SEVEN"""
        if isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        """Adding equal method to circle class - STEP EIGHT"""
        return self.radius == other.radius

    def __lt__(self, other):
        """Adding less than method to circle class - STEP EIGHT"""
        return self.radius < other.radius

    def __gt__(self, other):
        """Adding greater than method to circle class - STEP EIGHT"""
        return self.radius > other.radius

    def __le__(self, other):
        """Adding less than or equal to method to circle class - STEP EIGHT"""
        return self.radius <= other.radius

    def __ge__(self, other):
        """Adding greater than or equal to method to circle class - STEP EIGHT"""
        return self.radius >= other.radius

    def __ne__(self, other):
        """Adding does not equal method to circle class - STEP EIGHT"""
        return self.radius != other.radius

    @property
    def radius(self):
        """radius for Circle - STEP ONE"""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError

        if self._radius != value:
            self._diameter = value * 2
            self._radius = value
            self._area = pi * self._radius**2
            self._perimeter = 2 * self._radius * pi

    @classmethod
    def from_diameter(cls, diameter):
        """Alternate constructor that lets the user create a
        Circle directly with the diameter. STEP FIVE"""
        if diameter <= 0:
            raise ValueError('Diameter needs to be a number greater then zero')
        self = cls(diameter/2)
        self.diameter = diameter
        return self

    @property
    def area(self):
        """Area property for Circle - STEP FOUR"""
        return self._area

    @property
    def perimeter(self):
        """setting perimeter property"""
        return self._perimeter

    @property
    def diameter(self):
        """diameter for Circle - STEP TWO"""
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        """Set diameter for Circle - STEP THREE"""
        if value < 0:
            raise ValueError

        if self._diameter != value:
            self._diameter = value
            self._radius = value / 2
            self._area = pi * self._radius**2
