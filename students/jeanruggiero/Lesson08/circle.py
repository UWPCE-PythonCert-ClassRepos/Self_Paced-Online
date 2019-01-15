#!/usr/bin/env python3

import math

class Circle():
    """
    Circle class represents a simple circle.
    """

    def __init__(self, radius):
        self.radius = radius

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
