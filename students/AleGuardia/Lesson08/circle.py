
# Assignment 8 - Alejandro Guardia
import math


class Circle():
    def __init__(self,radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return math.pi*self.radius**2

    @classmethod
    def from_diameter(cls,diameter):
        return cls(diameter/2)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)












