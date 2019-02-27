


class Circle(object):
    """For manipulating circles"""

    import math as m

    def __init__(self, radius):
        """Initialize radius"""
        self._radius = radius

    @property
    def radius(self):
        """radius property"""
        return self._radius

    @property
    def diameter(self):
        """Diameter property"""
         return self._radius*2

    @property
    def area(self):
        """Area property"""
        return float(f'{Circle.m.pi * self._radius**2:.4f}')

    @diameter.setter
    def diameter(self, diameter):
        """Set diameter"""
        self._radius = _diameter/2

    @classmethod
    def from_diameter(cls, diameter):
        """Returns radius from diameter"""
        radius = diameter/2
        return cls(radius)

    def __str__(self):
        """Returns new string"""
        return f'Circle with radius: {self._radius:.6f}'

    def __repr__(self):
        """Returns string of Circles radius"""
        return f'Circle({self._radius:.0f})'

    def __add__(self,circle_x):
        """Addition of circle objects"""
        new_circle = Circle(self._radius + circle_x.radius)
        return new_circle

    def __mul__(self, other):
        """multiplication of circle objects"""
        if isinstance(other, Circle):
            return Circle(self._radius * other._radius)
        else:
            return Circle(self._radius * other)

    __rmul__ = __mul__

    def __lt__(self, other):
        """Allows less than to work with circle objects"""
        return self._radius < other.radius

    def __gt__(self, other):
        """Allows greater than to work with circle objects"""
        return self._radius > other.radius

    def __eq__(self, other):
        """Allows equivalence comparison of circle objects"""
        return self._radius == other.radius




