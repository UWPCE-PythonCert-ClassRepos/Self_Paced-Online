#!/usr/bin/env python3

# Lesson_8 Activity 1 The Circle Class
import math


class Circle:

    def __init__(self, radius=1):
        self.radius = radius
        self._area = radius ** 2 * math.pi
        self._circumference = 2 * math.pi * radius

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __rmul__(self, other):
        # for reverse order
        if isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __truediv__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius / other.radius)
        else:
            return Circle(self.radius / other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __iadd__(self, other):
        if isinstance(other, Circle):
            self.radius += other.radius
        else:
            self.radius += other
        return self

    def __imul__(self, other):
        if isinstance(other, Circle):
            self.radius *= other.radius
        else:
            self.radius *= other
        return self

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        # make sure the radius changes when we change diameter
        self.radius = value / 2

    @property
    def area(self):
        """ Read Only """
        return self._area

    @property
    def circumference(self):
        """ Read Only """
        return self._circumference

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
