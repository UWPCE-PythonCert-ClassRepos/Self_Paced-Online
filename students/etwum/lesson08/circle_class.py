from math import pi


class Circle():

    def __init__(self,radius):
        self.radius = radius
        self.__area = pi * radius**2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, radius):
        self.radius = radius/2

    @property
    def area(self):
        return self.__area

    @classmethod
    def get_diameter(cls,diameter):
        return cls(diameter/2)

    def __str__(self):
        return "Circle with radius: {x:.1f}".format(x=self.radius)

    def __repr__(self):
        return 'Circle({x})'.format(x=self.radius)

    def __add__(self, other):
        total_radius = self.radius + other.radius
        return total_radius

    def __mul__(self, other):
        multiply_radius = self.radius * other
        return multiply_radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def sort(self):
        return sorted(self.radius)


