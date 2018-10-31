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

    # Altenate constructor
    @classmethod
    def from_diameter(self, diameter):
        return Circle(diameter / 2)

    # Informal string representation of an object
    def __str__(self):
        return "Circle with radius: {0:.6f}".format(self.radius)

    # Official string representation of an object
    def __repr__(self):
        return "Circle({})".format(self.radius)

    # Returns the addition of two circles
    def __add__(self, new_circ):
        return Circle(self.radius + new_circ.radius)

    # Returns the subtraction of two circles
    def __sub__(self, new_circ):
        return Circle(self.radius - new_circ.radius)

    # Returns the mutliplication of a circle times a value
    def __mul__(self, val):
        return Circle(self.radius * val)

    # Fixes unsupported operand
    def __rmul__(self, val):
        return Circle(self.radius * val)

    #  ##Compare methods## ##

    # Greater than
    def __gt__(self, other):
        return self.radius > other.radius

    # Less than
    def __lt__(self, other):
        return self.radius < other.radius

    # Equal
    def __eq__(self, other):
        return self.radius == other.radius
