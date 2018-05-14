#Natalie Rodriguez
# Lesson 08: Circle
# May 12, 2018
'''
Goal:
The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter, and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area
Print the circle and get something nice
Be able to add two circles together
Be able to compare two circles to see which is bigger
Be able to compare to see if there are equal
(follows from above) be able to put them in a list and sort them
You will use:

properties
a classmethod
a define a bunch of “special methods”

General Instructions:
For each step, write a couple of unit tests that test the new features.
Run these tests (and they will fail the first time)
Add the code required for your tests to pass.
    '''

#imports

import math


class Circle:

    def __init__(self, in_radius=1):
        self._radius = in_radius

    def __str__(self):
        return "Circle with radius: "+str(self.radius)

    def __repr__(self):
        return "Circle("+str(self.radius)+")"

    def __add__(self, other):
        return Circle(self.radius+other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __imul__(self, scalar):
        self.radius *= scalar
        return self

    def __sub__(self, other):
        return Circle(self.radius-other.radius)

    def __mul__(self, scalar):
        return Circle(self.radius*scalar)

    def __rmul__(self, scalar):
        return Circle(self.radius*scalar)

    def __pow__(self, power):
        return Circle(self.radius**power)

    def __truediv__(self, scalar):
        return Circle(self.radius/scalar)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __len__(self):
        return round(self.circumference)

    @classmethod
    def from_diameter(cls, in_diameter):
        return cls(in_diameter / 2)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return 2 * self._radius

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return math.pi*(self._radius**2)

    @property
    def circumference(self):
        return 2*math.pi*self._radius