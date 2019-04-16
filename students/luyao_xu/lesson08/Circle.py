#!/usr/bin/env python3
from math import pi

# Step 1
class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    # step 2
    @property
    def diameter(self):
        return self.radius * 2

    # step3
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    # step 4
    @property
    def area(self):
        return 2 ** self.radius * pi

    # step 5
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    # step 6
    def __repr__(self):
        return"Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with radius of {}".format(self.radius)

    # step 7
    def __add__(self, other):
        return self.radius + other.radius

    def __mul__(self, val):
        return self.radius * val

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    # step 8
    @staticmethod
    def sort_key(self):
        return sorted(self.radius)














