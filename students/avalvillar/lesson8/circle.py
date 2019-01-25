"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    January 22th 2019
"""

'''
This is the circle class that inherits from object. A Circle must have a radius
and from there a diameter (or vice versa) and an area can be calculated on
demand. Sorting is achieved by implementing the less than and equals dunders
as some simple mathematics work against the circle objects as well.
'''

import math

class Circle(object):

    #Initialiver (default) which requires a radius then computes a diameter
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2

    #String dunder allowing for human readable string output
    def __str__(self):
        return 'Circle with radius: ' + str(self.radius)

    #Repr dunder used for more detailed output and eval() function call
    def __repr__(self):
        return '\'Circle({})\''.format(self.radius)

    #Addition dunder using to add two circle radius and make a new circle
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    #Multiplication dunder used to make a circle from a circle and numeric
    def __mul__(self, other):
        return Circle(self.radius * other)

    #Reflective multiplication when a numeric is given before the circle
    def __rmul__(self, other):
        return Circle(self.radius * other)

    #Less than dunder used for comparisons needed to sort (or compare)
    def __lt__(self, other):
        return self.radius < other.radius

    #Equals dunder used for comparisons needed to sort (or compare)
    def __eq__(self, other):
        return self.radius == other.radius

    #Alternative initilizer that can be used by a given diameter instead of radius
    @classmethod
    def from_diameter(self, diameter):
        return Circle(diameter / 2)

    #Property for the radius
    @property
    def radius(self):
        return self._radius

    #Setter for the radius
    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._diameter = radius * 2

    #Property for the diameter
    @property
    def diameter(self):
        return self._diameter

    #Setter for the diameter
    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self._radius = diameter / 2

    #Property for an area (calculate and return on demand)
    @property
    def area(self):
        return round(math.pi * math.pow(self._radius, 2), 6)
