# ------------------------------------------------- #
# Title: Lesson 8, pt 1/2 Circle
# Dev:   Craig Morton
# Date:  9/23/2018
# Change Log: CraigM, 9/23/2018, pt 1/2 Circle
# ------------------------------------------------- #

from math import pi
from functools import total_ordering
import random
import time


@total_ordering
class Circle:
    """
    Compute the circle’s area
    Print the circle and get something nice
    Be able to add two circles together
    Be able to compare two circles to see which is bigger
    Be able to compare to see if there are equal
    (follows from above) be able to put them in a list and sort them
    """

    def __init__(self, the_radius):
        self._radius = the_radius
        self._diameter = the_radius * 2

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter / 2)
        return self

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = self._radius * 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = self._diameter / 2

    @property
    def area(self):
        return self._diameter * pi

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        bigger_circle = Circle(self.radius + other.radius)
        return bigger_circle

    def __iadd__(self, other):
        self.radius = self.radius + other.radius
        return self

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __mul__(self, num):
        return Circle(self.radius * num)

    def __imul__(self, num):
        self.radius = self.radius * num
        return self

    def __rmul__(self, num):
        return self * num

    def sort_key(self):
        return self._radius

