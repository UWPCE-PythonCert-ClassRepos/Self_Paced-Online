#!/usr/bin/env python3
import math


class Circle:

    # Circle class init class
    # Returns the radius of a circle
    def __init__(self, radius):
        self.radius = radius

    # Returns teh diameter of a circle
    @property
    def diameter(self):
        return self.radius * 2

    # Returns teh diameter of a circle
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    # Returns teh area of a circle
    @property
    def area(self):
        return round(math.pi * self.radius**2, 5)
