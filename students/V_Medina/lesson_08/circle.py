"""
Assignment 8
March 18th 2019
Victor A Medina

"""
import math


class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,val):
        self._radius = val

    @property
    def diameter(self):
        return 2*self._radius

    @diameter.setter
    def diameter(self,val):
        self._radius = val/2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    def __str__(self):
        output = "Circle with a radius of {} and an area of {:.2f}".format(self._radius,self.area)
        return output

    def __repr__(self):
        return "Circle({})".format(self._radius)

    def __add__(self, other_circle):
        self._radius = self._radius + other_circle.radius
        return self

    def __mul__(self, factor):
        self._radius = self._radius * factor
        return self

    def __rmul__(self, factor):
        self._radius = self._radius * factor
        return self

    def __gt__(self, other_circle):
        return self.radius > other_circle.radius

    def __lt__(self, other_circle):
        return self.radius < other_circle.radius

    def __ge__(self, other_circle):
        return self.radius >= other_circle.radius

    def __le__(self, other_circle):
        return self.radius <= other_circle.radius

    def __eq__(self, other_circle):
        return self.radius == other_circle.radius