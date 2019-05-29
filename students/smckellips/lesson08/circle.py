#!/usr/bin/env python
import math

class Circle(object):
    def __init__(self, radius):
        self._radius = float(radius)
    def get_radius(self):
        return self._radius
    def get_diameter(self):
        return self._radius * 2
    def set_diameter(self,diameter):
        self._radius = float(diameter /2)
    def get_area(self):
        return math.pi * 2 * self._radius
    def __str__(self):
        return f"Circle with radius: {self._radius}"
    def __repr__(self):
        return f"Circle({self._radius})"
    def __add__(self,other):
        return Circle(self._radius + other._radius)
    def __mul__(self, multiple):
        return Circle(self._radius * multiple)
    def __rmul__(self, multiple):
        return Circle(self._radius * multiple)
    def __eq__(self, other):
        return self._radius == other._radius
    def __ne__(self, other):
        return self._radius != other._radius
    def __gt__(self, other):
        return self._radius > other._radius
    def __ge__(self, other):
        return self._radius >= other._radius
    def __lt__(self, other):
        return self._radius < other._radius
    def __le__(self, other):
        return self._radius <= other._radius
    def __iadd__(self, other):
        self._radius += other._radius
        return self
    def __imul__(self, multiple):
        self._radius *= multiple
        return self

    radius = property(get_radius)
    diameter = property(get_diameter, set_diameter)
    area = property(get_area)

class Sphere(Circle):
    def get_volume(self):
        return float(4 / 3 * math.pi * self._radius ** 3)
    def get_area(self):
        raise NotImplementedError
    def __str__(self):
        return f"Sphere with radius: {self._radius}"
    def __repr__(self):
        return f"Sphere({self._radius})"
    volume = property(get_volume)
