import math


class Circle(object):
    """Create a class of circles"""
    def __init__(self, radius):
        self._radius = radius
        self._diameter = self.radius*2
        self._area = self._radius*math.pi*2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def set_radius(self, radius):
        self._radius = radius
        self._diameter = radius*2
        self._area = radius*math.pi*2

    def set_diameter(self, diameter):
        self._diameter = diameter
        self._radius = diameter/2
        self._area = diameter * math.pi

    def get_area(self):
        return self._area

    def set_area(self, radius):
        raise ValueError('Cannot set the area.')

    radius = property(get_radius, set_radius)
    diameter = property(get_diameter, set_diameter)
    area = property(get_area, set_area)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        text = "{:.4f}".format(self._radius)
        return 'Circle with radius: ' + text

    def __repr__(self):
        return 'Circle(' + str(self.radius) + ')'

    def __add__(self, another_circle):
        """Returns circle_A + circle_B"""
        return Circle(self._radius + another_circle.radius)

    def __mul__(self, another_circle):
        """Returns circle_A * circle_B"""

        try:
            return Circle(self._radius * another_circle.radius)

        except AttributeError:
            if isinstance(another_circle, int):
                return Circle(self._radius * another_circle)
            else:
                raise AttributeError('Invalid multiplier')

    def __rmul__(self, integer):
        return Circle(self._radius * integer)

    def __lt__(self, b):
        return self.radius < b.radius

    def __le__(self, b):
        return self.radius <= b.radius

    def __eq__(self, b):
        return self.radius == b.radius

    def __ne__(self, b):
        return self.radius != b.radius

    def __ge__(self, b):
        return self.radius >= b.radius

    def __gt__(self, b):
        return self.radius > b.radius
