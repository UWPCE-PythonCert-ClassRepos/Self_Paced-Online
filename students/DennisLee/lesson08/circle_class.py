#!/usr/bin/env python3

from math import pi  # Need pi for the circle's area calculation.

class Circle():
    """Represent a circle, its radius, diameter, and area."""

    def __init__(self, value):
        """Create a circle using the specified radius value."""
        self.radius = value  # Use the setter to do error checking

    def __repr__(self):
        """Show the formal, evaluateable class representation."""
        return f"Circle({self._radius})" 

    def __str__(self):
        """Show an informal string representation of the class."""
        return f"Circle with radius: {self._radius}"

    def __add__(self, other):
        """
        Add two circles together, with the resulting circle having a
        radius equal to the sum of the individual circle radii.

        :other:  A number or Circle object representing the radius of
                 the second circle.

        :return:  The resulting summed Circle object.
        """
        new_radius = self._radius
        if isinstance(other, (int, float)):
            new_radius += other
        elif isinstance(other, Circle):  
            new_radius += other.radius
        else:
            raise TypeError(f"Cannot add {other} to a circle because it "
                    f"is a '{type(other)}' type, not an 'int' or 'Circle'.")
        return Circle(new_radius)

    def __radd__(self, other):
        """
        Add two circles together, with the resulting circle having a
        radius equal to the sum of the individual circle radii.

        :other:  A number or Circle object representing the radius of
                 the first circle.

        :return:  The resulting summed Circle object.
        """
        return self.__add__(other)

    def __mul__(self, other):
        """
        Multiply two circles together, with the resulting circle having
        a radius equal to the product of the individual circle radii.

        :other:  A number or Circle object representing the radius of
                 the second circle.

        :return:  The resulting multiplied Circle object.
        """
        new_radius = self._radius
        if isinstance(other, (int, float)):
            new_radius *= other
        elif isinstance(other, Circle):  
            new_radius *= other.radius
        else:
            raise TypeError(f"Cannot multiply {other} to a circle because it "
                    f"is a '{type(other)}' type, not an 'int' or 'Circle'.")
        return Circle(new_radius)

    def __rmul__(self, other):
        """
        Multiply two circles together, with the resulting circle having
        a radius equal to the product of the individual circle radii.

        :other:  A number or Circle object representing the radius of
                 the first circle.

        :return:  The resulting multiplied Circle object.
        """
        return self.__mul__(other)

    def __lt__(self, other):
        """
        Return `True` if this circle's radius is less than the other
        circle's radius.
        """
        return self._radius < other.radius

    def __le__(self, other):
        """
        Return `True` if this circle's radius is less than or equal to
        the other circle's radius.
        """
        return self._radius <= other.radius

    def __eq__(self, other):
        """
        Return `True` if this circle's radius is equal to
        the other circle's radius.
        """
        return self._radius == other.radius

    def __ne__(self, other):
        """
        Return `True` if this circle's radius is not equal to
        the other circle's radius.
        """
        return self._radius != other.radius

    def __gt__(self, other):
        """
        Return `True` if this circle's radius is greater than the other
        circle's radius.
        """
        return self._radius > other.radius

    def __ge__(self, other):
        """
        Return `True` if this circle's radius is greater than or equal to
        the other circle's radius.
        """
        return self._radius >= other.radius

    @property
    def radius(self):
        """Get the radius of the circle."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        Set the radius of the circle. Only nonnegative numbers are
        allowed.

        :value:  The new radius value.
        """
        if value < 0:
            raise ValueError(f"Negative radius of '{value}' not allowed.")
        else:
            self._radius = value

    @property
    def diameter(self):
        """Get the diameter of the circle (i.e., twice the radius)."""
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        """
        Set the diameter of the circle. Only nonnegative numbers are
        allowed.

        :value:  The new diameter value.
        """
        # Use the radius setter (instead of setting the internal member)
        # to do error checking
        self.radius = value / 2

    @property
    def area(self):
        """Get the area of the circle (pi times radius squared)."""
        return pi * self._radius ** 2

    @classmethod
    def from_diameter(self, value):
        """Create a circle using the specified diameter value."""
        return Circle(value / 2)