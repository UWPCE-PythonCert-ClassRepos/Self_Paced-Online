#!/usr/bin/env python

from math import pi


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self,value):
        self.radius = value / 2

    @property
    def area(self):
        return self.radius**2 * pi

    @classmethod
    def from_diameter(cls, diameter):
        return  cls(diameter / 2.0)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other.radius)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __gt__(self, other):
         return self.radius > other.radius

    def __ge__(self, other):
         return self.radius >= other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius