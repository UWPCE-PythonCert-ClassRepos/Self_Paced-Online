# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:37:09 2018

@author: Laura.Fiorentino
"""


from math import pi


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return self.radius ** 2 * pi

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __rmul__(self, value):
        return Circle(self.radius * value)

    def __mul__(self, value):
        return Circle(self.radius * value)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __truediv__(self, other):
        return Circle(self.radius / other.radius)
