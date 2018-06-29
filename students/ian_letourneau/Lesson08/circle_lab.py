#!/usr/bin/env python3
# Ian Letourneau
# 6/4/2018

import math


class Circle:

    def __init__(self, radius):
        """Construct object and set object variables radius 
        to given value and diameter to double the given value."""
        self.radius = radius
        self.diameter = radius*2

    def sort_key(self):
        """Set a sort key to improve sorting runtime."""
        return self._radius

    def __str__(self):
        """Override object string method to format correctly."""
        return 'Circle with a radius: {}'.format(self._radius)

    def __repr__(self):
        """Override object string method to format correctly."""
        return "'Circle({})'".format(self._radius)

    @property
    def radius(self):
        """Add a get_radius as property."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Add a set_radius as property. And recalculate
        diameter utilizing the radius given."""
        self._radius = value
        self._diameter = value*2

    @property
    def diameter(self):
        """Add a get_diameter as property."""
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        """Add a set_diameter as property and recalculate
        radius utilizing the diameter given."""
        self._diameter = value
        self._radius = value/2

    @property
    def area(self):
        """Add an area calculation property. (pi*r)^2"""
        return (math.pi*self._radius)*2

    @classmethod
    def from_diameter(cls, value):
        """Add an alternate constructor to create Circle
        objects from a given diameter. recalculates radius
        using half the given value."""
        self = cls(value)
        self._diameter = value
        self._radius = value/2
        return self

    def __add__(self, other):
        """Overload adding function to add circle radius
        to a second circle radius."""
        return Circle(self._radius + other._radius)

    def __mul__(self, other):
        """Overload multiplier function to multiply
        circle radius by an integer."""
        return Circle(self._radius*other)

    def __rmul__(self, other):
        """Overload reverse multiplier function to allow
        for multiplication with the integer passed as first
        parameter."""
        return Circle(self._radius*other)

    def __eq__(self, other):
        """Overload equals comparison operator to compare
        circle radii equality."""
        return self._radius == other._radius

    def __lt__(self, other):
        """Overload less than comparison operator to compare
        circle radii differences."""
        return self._radius < other._radius
