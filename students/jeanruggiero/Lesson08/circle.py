#!/usr/bin/env python3

import math
from functools import total_ordering

class RadiusError(Exception): pass

@total_ordering
class Circle():
    """
    Circle class represents a simple circle.
    """

    def __init__(self, radius):
        # Check provided radius is numeric and positive
        try:
            int(radius)
        except ValueError:
            raise RadiusError("Radius must be a number!")
        if radius  < 0:
            raise RadiusError("Radius can't be negative!")
        self.radius = radius

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __str__(self):
        return 'Circle of radius: {:.6f}'.format(self.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __sub__(self,other):
        # Check radius remains positive
        if self.radius - other.radius < 0:
            raise RadiusError("Radius can't be negative!")
        return Circle(self.radius - other.radius)

    def __isub__(self,other):
        # Check radius remains positive
        if self.radius - other.radius < 0:
            raise RadiusError("Radius can't be negative!")
        self.radius -= other.radius
        return self

    def __mul__(self, value):
        return Circle(self.radius*value)

    def __imul__(self, value):
        self.radius *= value
        return self

    def __rmul__(self,value):
        return self*value

    def __truediv__(self,value):
        return Circle(self.radius/value)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self, value):
        self.radius = value/2

    @property
    def area(self):
        return math.pi * self.radius**2

    @classmethod
    def from_diameter(cls, value):
        """Create instance of circle from diamater."""
        return cls(value/2)
