#!/usr/bin/env python3

import math


class Circle:
    # Step 1
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    # Step 2 and 3
    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    # Step 4
    @property
    def area(self):
        area = (self._radius ** 2) * math.pi
        return f"{area:.2f}"

    # Step 5
    @classmethod
    def from_diameter(self, diameter):
        return Circle(diameter / 2)

    # Step 6
    def __str__(self):
        return f"Circle with radius: {self._radius}"

    def __repr__(self):
        return f"Circle({self._radius})"

    # Step 7
    def __add__(self, other):
        return Circle(self._radius + other._radius)

    def __mul__(self, other):
        return Circle(self._radius * other)

    # Step 8
    def __eq__(self, other):
        return self._radius == other._radius

    def __ne__(self, other):
        return self._radius != other._radius

    def __lt__(self, other):
        return self._radius < other._radius

    def __gt__(self, other):
        return self._radius > other._radius

