# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  01-Apr-2018
# ------------------------------------------- #

import math

class Circle:
    def __init__(self, radius):
        if isinstance(radius, (int, float)) and radius > 0:
            self.radius = radius
        else:
            raise TypeError('Radius of a circle has to be an integer or a float or greater than 0.')

    def __str__(self):
        return '{} with radius: {}'.format(self.__class__.__name__, self.radius)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.radius)

    def __add__(self, other):
        if isinstance(other, Circle):
            other = other.radius
            return '{}({})'.format(self.__class__.__name__, self.radius + other)
        else:
            raise TypeError('You can only add 2 Circle instances.')

    def __iadd__(self, other):
        return self.__add__(other)


    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self.radius *= other
            return '{}({})'.format(self.__class__.__name__, self.radius)
        else:
            raise TypeError('You can only multiply by a number.')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.value = value
        self.radius = self.value / 2

    @property
    def area(self):
        try:
            return round(math.pi * self.radius**2, 5)
        except AttributeError:
            raise

    @classmethod
    def from_diameter(cls, diameter):
        if isinstance(diameter, (int, float)):
            return cls(diameter / 2)
        else:
            raise TypeError('Diameter of a circle has to be an integer or a float.')


if __name__ == '__main__':
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = Circle(4)
    c4 = Circle(5)
    c5 = Circle.from_diameter(6)
    c6 = Circle(2)
    print('Is c1 > c2?', c1 > c2)
    print('Is c1 < c2?', c1 < c2)
    print('Is c2 == c3', c2 == c3)
    print('Is c1 == c6', c1 == c6)





