#!/usr/bin/env python3

"""
A class-based system for rendering circles.
"""

import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with radius: {:.5f}".format(self.radius)

    @property
    def diameter(self):
        return self.radius*2
    @diameter.setter
    def diameter(self, val):
        self.radius = val/2

    @property
    def area(self):
        return math.pi*self.radius**2

    @classmethod
    def from_diameter(cls, val):
        radius = val/2
        return cls(radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __truediv__(self, other):
        return self.radius / other

    def __floordiv__(self, other):
        return Circle(self.radius // other)

    def __mod__(self, other):
        return Circle(self.radius % other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ne__(self, other):
        return self.radius != other.radius

