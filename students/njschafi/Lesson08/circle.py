# NEIMA SCHAFI, LESSON 8 Assignment - Circle Class
import math


class Circle(object):
    """Main class for object"""

    def __init__(self, r):
        """Main Constructor"""
        try:
            self._radius = float(r)
        except ValueError:
            print('Error: Need numeric value passed in')

    @classmethod
    def from_diameter(cls, d):
        """Alternate Constructor"""
        self = cls(d/2)
        return self

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius*2

    @diameter.setter
    def diameter(self, d):
        try:
            self._radius = float(d/2)
            self._diameter = d
        except TypeError:
            print('Error: Need numeric value')

    @property
    def area(self):
        """Calculates and returns area of circle instance"""
        return math.pi*(self._radius ** 2)

    @area.setter
    def area(self, a):
        """Raises error if user inputs an area to set radius/diameter"""
        raise AttributeError('Area cannot be set')

    def __str__(self):
        """Displays radius of circle"""
        return 'Circle with radius: {:0.6f}'.format(self._radius)

    def __repr__(self):
        """Displays object instance"""
        return 'Circle({:.0f})'.format(self._radius)

    def __add__(c1, c2):
        """Adds the radius of 2 circles"""
        return Circle(c1.radius + c2.radius)

    def __mul__(self, num):
        """Multiples radius of a circle by an int"""
        return Circle(self.radius * num)

    def __rmul__(self, num):
        """Multiples radius of circle by an int but sequence reversed"""
        return Circle(self.radius * num)

    def __gt__(c1, c2):
        """Compares if one circle is greater than the other"""
        return c1.radius > c2.radius

    def __lt__(c1, c2):
        """Compares if one circle is less than the other"""
        return c1.radius < c2._radius

    def __eq__(c1, c2):
        """Compares if one circle is equal to the other"""
        return c1.radius == c2.radius

    # Optional Features

    def __iadd__(self, other):
        """Augmented adding"""
        return Circle(self.radius + other.radius)

    def __imul__(self, num):
        """Augmented multiplication"""
        return Circle(self.radius * num)
