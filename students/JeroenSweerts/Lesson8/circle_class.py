import math
import functools

class Circle():
    def __init__(self, the_radius=None):
        if the_radius is not None and the_radius < 0:
            raise ValueError("radius can't be less than zero")
        self._radius = the_radius

    def __str__(self):
        return "Circle with radius: " + str(self._radius)

    def __repr__(self):
        result = str(self.__class__.__qualname__) + "(" + str(self._radius) + ")"
        return result

    def __add__(self, circle):
        self._radius = self._radius + circle.radius
        return self

    def __mul__(self, multiplicator):
        self._radius = self._radius * multiplicator
        return self

    def __rmul__(self, multiplicator):
        self._radius = self._radius * multiplicator
        return self

    def __eq__(self, circle):
        return self._radius == circle.radius

    def __gt__(self, circle):
        return self._radius > circle.radius

    def __le__(self, circle):
        return self._radius <= circle.radius

    def __ge__(self, circle):
        return self._radius >= circle.radius

    @property
    def radius(self):
        """property for the radius of the circle"""
        return self._radius

    @radius.setter
    def radius(self, val):
        """setter, tests if radius is positive"""
        if val < 0:
            raise ValueError("radius can't be less than zero")
        self._radius = val

    @property
    def diameter(self):
        """diameter of the circle based on the radius"""
        return 2*self._radius

    @diameter.setter
    def diameter(self, val):
        """sets the radius and diameter and checks if the given diameter is positive"""
        if val < 0:
            raise ValueError("diameter can't be less than zero")
        self._radius = val/2

    @property
    def area(self):
        """area is calculated on the current circle radius"""
        return self._radius*self._radius*math.pi

    @classmethod
    def from_diameter(circle, diameter):
        """an alternate constructor that lets the user create a Circle directly
        with the diameter"""
        self = circle()
        if diameter < 0:
            raise ValueError("diameter can't be less than zero")
        self.diameter = diameter
        return self
