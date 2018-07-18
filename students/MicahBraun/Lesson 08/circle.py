# ----------------------------------------------------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Lesson 08 -- circle.py
# PURPOSE: Create circle class
# DATE: 07/16/2018
#
# DESCRIPTION: Circle class describes circle object with radius, diameter, and area properties for accessing and
# setting circle attributes. Also includes __str__, __repr__, __add__, __mul__, __eq__, __lt__, __gt__ Magic methods
# for further class decoration (__str__ and __repr__ for displaying data), (__add__, __mul__ for adding/multiplying
# class objects together), (__eq__, __lt__, __gt__ for evaluating equality between class objects)
# ----------------------------------------------------------------------------------------------------------------------
from math import pi


class Circle:
    """
    Simple Circle class: performs calculations for radius, diameter, area of circle
    """

    def __init__(self, the_radius):                                 # Step 1
        """
        class initializer
        :param the_radius:
        """
        self._radius = the_radius
        self._diameter = the_radius * 2                              # Step 2

    @classmethod                                                     # Step 5
    def from_diameter(cls, diameter):
        """
        Access Circle from diameter using @classmethod decorator
        :param diameter: receives values passed in at constructor-level
        :return:
        """
        self = cls(diameter / 2)
        return self

    @property                                                        # Step 3 (@property radius: @property area)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        Allows for setting radius value (updating resulting diameter value)
        :param value: The radii value
        :return:
        """
        self._radius = value
        self._diameter = self._radius * 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        """
        Allows for setting diameter value (updating resulting radius value)
        :param value: The diameter value
        :return:
        """
        self._diameter = value
        self._radius = self._diameter / 2

    @property                                                          # Step 4
    def area(self):
        """
        Returns area of passed radius value as Circle area using equation.
        :return:
        """
        # area of circle == pi * r^2
        a = self._radius * self._radius
        return a * pi

    def __str__(self):                                                  # Step 6
        """
        String representation of Circle class
        :return:
        """
        return "Circle {}".format(self.radius)

    def __repr__(self):
        """
        Similar to __str__, more machine-targeted but provides string output
        :return:
        """
        return "Circle({})".format(self.radius)

    def __add__(self, other):                                   # Step 7
        """
        Method for adding two circles together
        :param other:
        :return:
        """
        add_circles = Circle(self.radius + other.radius)
        return add_circles

    def __mul__(self, other):
        """
        Method for multiplying two circles together
        :param other:
        :return:
        """
        multiply_circles = Circle(self.radius * other.radius)
        return multiply_circles

    def __eq__(self, other):                                # Step 8
        """
        Method for testing equality of one circle against another
        :param other:
        :return:
        """
        return self.radius == other.radius

    def __lt__(self, other):
        """
        Method for testing inequality of circles
        :param other:
        :return:
        """
        return self.radius < other.radius

    def __gt__(self, other):
        """
        Method for testing inequality of circles
        :param other:
        :return:
        """
        return self.radius > other.radius

