#!/usr/bin/env python3

import math

"""
Lesson8 - Circle Class
"""


class Circle(object):
    version = '0.1'
    radius = ''

    def __init__(self, radius=None, diameter=None):

        if radius is None and diameter is None:
            raise ValueError()

        if radius is not None:
            try:
                if radius < 0:
                    raise ValueError()
            except ValueError:
                print('Radius must be positive.')
                return
            else:
                self.radius = radius
                self._diameter = radius * 2
                self._area = round(math.pi * radius ** 2.0, 6)

        if diameter is not None:
            try:
                if diameter < 0:
                    raise ValueError()
            except ValueError:
                print('Diameter must be positive.')
                return
            else:
                self.radius = diameter / 2
                self._diameter = diameter
                self._area = round(math.pi * self.radius ** 2.0, 6)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter=None):
        self._diameter = diameter
        self.radius = diameter / 2

    @property
    def area(self):
        self._area = round(math.pi * self.radius ** 2.0, 6)
        return self._area

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return Circle(radius)

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def sort_key(self):
            return self.val


circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
           Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
