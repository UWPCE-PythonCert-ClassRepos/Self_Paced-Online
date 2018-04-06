#!/usr/bin/env python

"""This module create some really cool circles."""
import math


class Circle:
    """The circle class"""

    def __init__(self, radius):
        self.radius = radius

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


if __name__ == "__main__":
    pass