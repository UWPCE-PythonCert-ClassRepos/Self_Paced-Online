#!/usr/bin/env python3
"""Circle Module"""

import math


class Circle:
    """Circle Class"""
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius
        self._area = math.pi * radius**2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def area(self):
        return self._area

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError

        if self._diameter != value:
            self._diameter = value
            self._radius = value / 2
            self._area = math.pi * self._radius**2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError

        if self._radius != value:
            self._radius = value
            self._diameter = value * 2
            self._area = math.pi * self._radius**2
