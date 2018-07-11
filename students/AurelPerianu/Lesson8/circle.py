#!/usr/bin/env python3

from math import pi


class Circle:
    def __init__(self, radius=1):
        self._in_rad = radius

    @property
    def radius(self):
        return self._in_rad

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError('Radius cannot be negative')
        self._in_rad = val

    @property
    def diameter(self):
        return 2 * self._in_rad

    @diameter.setter
    def diameter(self, val):
        if val < 0:
            raise ValueError('Diameter cannot be negative')
        self._in_rad = val / 2

    @property
    def area(self):
        return pi * self._in_rad ** 2

    def __str__(self):
        return "Circle with radius: "+str(self._in_rad)

    def __repr__(self):
        return f'Circle({str(self._in_rad)})'

    def __valid__(self, other):
        """ Limit the add operation only to circle class"""
        if isinstance(other, Circle):
            return True
        else:
            raise ValueError('The value should be a circle')

    def __add__(self, other):
        if self.__valid__(other):
            return Circle(self._in_rad+other._in_rad)

    def __valid_int__(self, other):
        """Limit to multiplication operation only at numbers"""
        if isinstance(other, (int, float)):
            return True
        else:
            raise ValueError('The value should be a number')

    def __mul__(self, val):
        if self.__valid_int__(val):
            return Circle(self._in_rad*val)

    def __rmul__(self, val):
        if self.__valid_int__(val):
            return Circle(val*self._in_rad)

    __rmul__ = __mul__

    def sort_key(self):
        """
          sorted(list_of_simple_objects, key=Simple.sort_key)
        """
        return self.val

    def __lt__(self, other):
        if self.__valid__(other):
            return self._in_rad < other._in_rad

    def __le__(self, other):
        if self.__valid__(other):
                return self._in_rad <= other._in_rad

    def __eq__(self, other):
        if self.__valid__(other):
            return self._in_rad == other._in_rad

    def __ne__(self, other):
        if self.__valid__(other):
                return self._in_rad != other._in_rad

    def __ge__(self, other):
        if self.__valid__(other):
            return self._in_rad >= other._in_rad

    def __gt__(self, other):
        if self.__valid__(other):
            return self._in_rad > other._in_rad

    @classmethod
    def from_diameter(cls, value):
        """Create a circle/sphere using the specified diameter value."""
        return cls(value / 2)


class Sphere(Circle):

    def __str__(self):
        return "Sphere with radius: " + str(self._in_rad)

    def __repr__(self):
        return f'Sphere({str(self._in_rad)})'

    @property
    def area(self):
        return 4*pi * self._in_rad ** 2

    @property
    def volume(self):
        return 4/3*pi * self._in_rad ** 3

    def __valid__(self, other):
        """ Limit the add operation only to circle class"""
        if isinstance(other, Sphere):
            return True
        else:
            raise ValueError('The value should be a Sphere')
