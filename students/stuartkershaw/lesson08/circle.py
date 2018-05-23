#!/usr/bin/env python3

from math import pi


class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("A positive radius value is required.")
        self._radius = val

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, val):
        if val < 0:
            raise ValueError("A positive radius value is required.")
        self._radius = val / 2

    @property
    def area(self):
        return self.radius * self.radius * pi

    @classmethod
    def from_diameter(cls, val):
        return cls(val / 2)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def sort_key(self):
        return self.radius
