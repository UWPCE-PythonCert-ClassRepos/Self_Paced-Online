#!/usr/bin/python3

## author: Roy Tate (githubtater)

import math

class Circle:

    def __init__(self, radius):
        '''Create a circle with a radius. Radius is mandatory (cant have a circle without one)'''
        self._radius = radius

    @property
    def radius(self):
        '''Get radius of circle'''
        return self._radius

    @property
    def diameter(self):
        '''Get diameter of circle'''
        return self._radius * 2

    @diameter.setter
    def diameter(self, val):
        '''Allow the diameter to be set by the user'''
        self._radius = val / 2

    @property
    def area(self):
        '''Get the area of the circle (radius**2*pi)'''
        return (self._radius ** 2 * math.pi)

    @classmethod
    def from_diameter(self, val):
        '''Allow the creation of a circle by providing a diameter.'''
        return Circle(val / 2)

    def __str__(self):
        '''Provide a basic string representation of a Circle'''
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        '''Show the formal representation'''
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        '''Add two strings together'''
        new_radius = self._radius
        if isinstance(other, int):
            new_radius += other
        elif isinstance(other, Circle):
            new_radius += other.radius
        return Circle(new_radius)

    def __radd__(self, other):
        '''Allows reflected addition (c1 + 3 or 3 + c1)'''
        return self.__add__(other)

    def __mul__(self, other):
        '''Multiply two circles together resulting in a new circle'''
        new_radius = self._radius
        if isinstance(other, int):
            new_radius *= other
        elif isinstance(other, Circle):
            new_radius *= other.radius
        else:
            raise TypeError('Cannot multiply circle by {} because {} is not supported.'.format(other, type(other)))
        return Circle(new_radius)

    def __rmul__(self, other):
        ''''Allows reflected multiplication (c1 * 3 == 3 * c1)'''
        return self.__mul__(other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def sort_key(self):
        return self._radius


