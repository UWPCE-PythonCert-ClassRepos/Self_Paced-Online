#!/usr/bin/env python3

from math import pi


class Circle:
    '''A class to provide information about circles'''

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return (self.radius ** 2) * pi

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return Circle(radius)

    def __str__(self):
        return "Cirle with Radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, n):
        return Circle(self.radius * n)

    __rmul__ = __mul__

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius
