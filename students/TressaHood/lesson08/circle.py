#!/usr/bin/env python3

"""
Lesson 08, Main file for Circle Class Assignment
The goal is to create a class that represents a simple circle
"""

#import modules
from math import pi


class Circle(object):
    """This is the main class for the circle
    Setting up all the attributes and methods for this class, including addition, get/set, multiply, equality indicators
    Usually returns the radius/diameter back to the user, except in the cases of set.
    """

    def __init__(self, radius=6):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        self._radius = val

    @property
    def diameter(self):
        return 2 * self._radius

    @diameter.setter
    def diameter(self, val):
        self._radius = val / 2

    @property
    def area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return "Circle with radius: {:.2f}".format(self._radius)

    def __repr__(self):
        return "Circle({})".format(self._radius)

    def __add__(self, other_thing):
        if isinstance(other_thing, Circle):
            return Circle(self._radius + other_thing._radius)

        else:
            return Circle(self._radius + other_thing)

    def __mul__(self, other_thing):
        if isinstance(other_thing, Circle):
            return Circle(other_thing._radius * self._radius)

        else:
            return Circle(other_thing * self._radius)

    def __rmul__(self, other_thing):
        if isinstance(other_thing, Circle):
            return Circle(other_thing._radius * self._radius)

        else:
            return Circle(other_thing * self._radius)

    def __lt__(self, other_thing):
        return self._radius < other_thing._radius

    def __gt__(self, other_thing):
        return self._radius > other_thing._radius

    def __eq__(self, other_thing):
        return self._radius == other_thing._radius

    def sort_key(self):
        return self._radius

    @classmethod
    def from_diameter(classes, diameter):
        radius = diameter / 2
        return Circle(radius)
