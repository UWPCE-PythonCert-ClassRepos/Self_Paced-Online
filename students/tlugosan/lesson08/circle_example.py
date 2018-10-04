#!/usr/bin/env python3
from math import pi


class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius must greater than 0")
        else:
            self._radius = radius

    @property
    def diameter(self):
        return 2 * self._radius

    @diameter.setter
    def diameter(self, val):
        self._radius = val / 2

    @property
    def area(self):
        return 2 * self.radius * pi

    @classmethod
    def from_diameter(cls, diameter):
        return diameter / 2

    def __repr__(self):
        return "Circle({})".format(self._radius)

    def __str__(self):
        return "Circle with radius: {:1f}".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, val):
        return Circle(self.radius * val)

    def __rmul__(self, val):
        return self.__mul__(val)

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return Circle(self.radius != other.radius)

    @staticmethod
    def sort_key(self):
        return self.radius


    def __truediv__(self, val):
        if val == 0:
            raise ValueError("Divison with 0 is not allowed.")
        else:
            return Circle(self.radius / val)
