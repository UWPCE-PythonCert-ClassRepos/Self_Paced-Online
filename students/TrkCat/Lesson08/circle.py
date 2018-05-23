from math import pi


class Circle():
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError('radius cannot be negative')
        self._radius = val

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, val):
        self._radius = val / 2

    @property
    def area(self):
        return pi * self._radius ** 2

    @classmethod
    def from_diameter(cls, val):
        return cls(val / 2)

    def __str__(self):
        return ('Circle with radius: {}'.format(self._radius))

    def __repr__(self):
        return 'Circle({})'.format(self._radius)
