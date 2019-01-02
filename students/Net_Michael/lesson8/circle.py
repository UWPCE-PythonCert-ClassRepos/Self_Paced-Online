#!/usr/bin/env python3

"""
goal is to create a class that represents a simple circle.
        Compute the circle’s area.
        Print the circle and get something nice.
        Be able to add two circles together.
        Be able to compare two circles to see which is bigger.
        Be able to compare to see if they are are equal.
        (follows from above) be able to put them in a list and sort them.
use:
        properties.
        a bunch of “magic methods”.
        a classmethod (after you’ve learned about them…).
"""

import operator
import math

class Circle:
    def __init__(self, radius):
        self._radius = radius
        if self._radius < 0:
            raise ValueError("Radius can't be less than zero")
            #
    @property
    def radius(self):
    #    print("Radius = ", self._radius)
        return self._radius
    #
    def __str__(self):
        return "Circle with radius: {:.4f}".format(self._radius)
        #
    def __repr__(self):
        return "Circle({})".format(self._radius)
        #
    def __add__(self, other):
        return Circle(self._radius + other._radius)
   #
    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius * other._radius)
        else:
            return self._radius * other
    #
    def __rmul__(self, other):
        return self.__mul__(other)
    #
    def __gt__(self, other):
         return self._radius > other._radius
    #
    def __lt__(self, other):
        return self._radius < other._radius
    #
    def __eq__(self, other):
        return self._radius == other._radius
    #
    @radius.setter
    def radius(self, rr):
        if rr < 0:
            raise ValueError("Radius can't be less than zero")
        self._radius = rr
        #
#    @staticmethod
    def sort_key(self):
        return(self._radius)
        #
    @property
    def diameter(self):
        diameter = 2*self._radius
        return diameter
        #
    @diameter.setter
    def diameter(self, dd):
        self._radius = dd/2
    #
    @property
    def area(self):
        area = math.pi * self._radius **2
        return area
