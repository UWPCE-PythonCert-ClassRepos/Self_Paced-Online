#!/usr/bin/env python3
"""Circle Module"""


class Circle:
    """Circle Class"""
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError

        self._diameter = value
            self._radius = value / 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError

        self._radius = value
            self._diameter = value * 2
