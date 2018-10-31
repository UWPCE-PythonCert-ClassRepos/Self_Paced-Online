'''
Shin Tran
Python 210
Assignment 8
'''

# This program represents a simple circle, takes in a float as a radius parameter

import math
import operator

class Circle(float):

    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2

    # Returns the radius of the circle
    @property
    def radius(self):
        return self._radius

    # Returns the diameter of the circle
    @property
    def diameter(self):
        return self._diameter

    # Allows the user to set the radius of the circle
    # Also modifies the diameter
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2

    # Allows the user to set the diameter of the circle
    # Also modifies the radius
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2

    # Returns the area of the circle, user is unable to modify the area
    @property
    def area(self):
        return math.pi * math.pow(self._radius, 2)

    # Returns the circumference of the circle,
    # user is unable to modify the circumference
    @property
    def circumference(self):
        return math.pi * self._diameter

    # Allows the user to declare a cirlce by diameter
    @classmethod
    def from_diameter(class_object, diameter):
        return class_object(diameter / 2)

    # Returns a string of the Circle and radius
    def __str__(self):
        ret_string = "Circle with raidus: {}".format(self._radius)
        return ret_string

    # Returns a string of the Circle and radius
    def __repr__(self):
        ret_string = "'Circle({})'".format(self._radius)
        return ret_string

    # Adds two instances of a circle together
    # Returns a circle with the two radii added together
    def __add__(self, new):
        return Circle(self.radius + new.radius)

    # Subtracts one instances of a circle from another
    # Returns a circle with the difference of the two radii
    def __sub__(self, new):
        return Circle(self.radius - new.radius)

    # Multiplies the cirlce by a number passed in as a paramter
    # Returns a circle with the product of the circle and number parameter
    def __mul__(self, new):
        return Circle(self.radius * new)

    # Divides the cirlce by a number passed in as a paramter
    # Returns a circle with the quotient of the circle divided by the parameter
    def __truediv__(self, new):
        return Circle(self.radius / new)

    # Compares to see if a circle is less than another circle
    def __lt__(self, comparison):
        return self.radius < comparison.radius

    # Compares to see if a circle is greater than another circle
    def __gt__(self, comparison):
        return self.radius > comparison.radius

    # Compares to see if a circle equaled another circle
    def __eq__(self, comparison):
        return self.radius == comparison.radius

    # Compares to see if a circle is less or equaled to another circle
    def __le__(self, comparison):
        return self.radius <= comparison.radius

    # Compares to see if a circle is greater than or equaled to another circle
    def __ge__(self, comparison):
        return self.radius >= comparison.radius

    # Compares to see if a circle is not equaled another circle
    def __ne__(self, comparison):
        return self.radius != comparison.radius