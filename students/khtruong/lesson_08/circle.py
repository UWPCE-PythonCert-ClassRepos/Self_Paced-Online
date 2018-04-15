#!/usr/bin/env python

"""This module create some really cool circles."""
import math
import functools

@functools.total_ordering
class Circle:
    """The circle class"""

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__qualname__, self.radius)

    def __str__(self):
        return '{} with radius: {}'.format(
            self.__class__.__qualname__, self.radius)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val/2

    @property
    def area(self):
        return math.pi * self.radius**2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, val):
        return Circle(self.radius * val)

    def __rmul__(self, val):
        return Circle(self.radius * val)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

if __name__ == "__main__":
    pass