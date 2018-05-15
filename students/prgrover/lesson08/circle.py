#!/usr/bin/env python3

import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return self.radius**2 * math.pi

    @classmethod
    def from_diameter(cls, diameter):
        cls.radius = diameter / 2
        return cls(cls.radius)

    def __str__(self):
        return "Circle with radius: {:.2f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        total = self.radius + other.radius
        return Circle(total)

    def __mul__(self, other):
        total = self.radius * other
        return Circle(total)

#    def __gt__(self, other):
#        return self.radius > other.radius
    
#    def __lt__(self, other):
#        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius
