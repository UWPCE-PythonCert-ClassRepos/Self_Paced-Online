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
        return math.pi * (self.radius**2)

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter/2)
        return self

    def __str__(self):
        return "Circle with radius: {:.2f}".format(self.radius)

    def __repr__(self):
        return "Circle({:d})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __radd__(self, other):
        return Circle.__add__(self, other)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle.__mul__(self, other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __iadd__(self, other):
        self.radius += other.radius
        return self
