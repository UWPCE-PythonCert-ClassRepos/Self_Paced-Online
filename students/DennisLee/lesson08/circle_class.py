#!/usr/bin/env python3

from math import pi

class Circle():

    def __init__(self, value):
        self.radius = value

    def __repr__(self):
        return f"Circle({self._radius})" 

    def __str__(self):
        return f"Circle with radius: {self._radius}"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError(f"Negative radius of '{value}' not allowed.")
        else:
            self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * self._radius ** 2

    @classmethod
    def from_diameter(self, value):
        return Circle(value / 2)