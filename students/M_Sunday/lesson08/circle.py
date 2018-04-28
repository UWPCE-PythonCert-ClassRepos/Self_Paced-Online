#!/usr/bin/python
from math import pi


class Circle(object):

    @staticmethod
    def entry_check(the__radius):
        if isinstance(the__radius, (str, list, tuple, dict)):
            raise TypeError("Radius entry must be a single, positive, and "
                            "non-string value")
        else:
            if the__radius < 0:
                raise ValueError("Radius must be greater than 0")
            else:
                return the__radius

    def __init__(self, the_radius):
        self._radius = self.entry_check(the_radius)

    def __repr__(self):
        return "Circle({})".format(self._radius)

    def __str__(self):
        return "Circle with radius: {0:.6f}".format(float(self._radius))

    def __add__(self, other):
        new_circle = self._radius + other._radius
        return Circle(new_circle)

    def __rmul__(self, other):
        new_circle = self._radius * other
        return Circle(new_circle)

    def __mul__(self, other):
        new_circle = self._radius * other
        return Circle(new_circle)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, the_radius):
        self._radius = self.entry_check(the_radius)

    @property
    def diameter(self):
        return self._radius * 2.0

    @diameter.setter
    def diameter(self, diam):
        self._radius = diam / 2.0

    @property
    def area(self):
        return pi * self._radius**2

    @classmethod
    def from_diameter(cls, dia):
        return cls(dia / 2.0)
