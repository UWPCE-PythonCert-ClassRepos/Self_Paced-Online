import math


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return f"Circle with radius: {self._radius}"

    def __repr__(self):
        return f"Circle({self._radius})"

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    @property
    def area(self):
        return self._radius * self._radius * math.pi

    def __add__(self, other):
        return type(self)(self.radius + other.radius)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.radius == other.radius
        return False

    def __mul__(self, n):
        return type(self)(self.radius * n)

    def __rmul__(self, n):
        return self * n

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius
