#!/usr/bin/env python3
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._diameter = self.radius * 2

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, another_circle):
        return Circle(self.radius + another_circle.radius)

    def __rmul__(self, num):
        return Circle(self.radius * num)

    def __mul__(self, num):
        return Circle(self.radius * num)

    def __lt__(self, another_circle):
        return self.radius < another_circle.radius

    def __gt__(self, another_circle):
        return self.radius > another_circle.radius

    def __eq__(self, another_circle):
        return self.radius == another_circle.radius

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value 
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


class Sphere(Circle):
    def __str__(self):
        return f'Sphere with radius: {self.radius}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    @property
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    @property
    def area(self):
        #returns surface area of a sphere
        return 4 * math.pi * (self.radius ** 2)