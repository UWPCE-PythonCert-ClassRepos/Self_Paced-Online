


class Circle(object):
    import math as m

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
         return self._radius*2

    @property
    def area(self):
        return float(f'{Circle.m.pi * self._radius**2:.4f}')

    @diameter.setter
    def diameter(self, diameter):
        self._radius = _diameter/2

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2
        return cls(radius)

    def __str__(self):
        return f'Circle with radius: {self._radius:.6f}'

    def __repr__(self):
        return f'Circle({self._radius:.0f})'

    def __add__(self,circle_x):
        new_circle = Circle(self._radius + circle_x.radius)
        return new_circle

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius * other._radius)
        else:
            return Circle(self._radius * other)

    __rmul__ = __mul__

    def __lt__(self, other):
        return self._radius < other.radius

    def __gt__(self, other):
        return self._radius > other.radius

    def __eq__(self, other):
        return self._radius == other.radius



circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]

