# Lesson 8 Assignment 1
# Circle Class
# Jason Virtue 03/09/2019
# UW Self Paced Python Course

from math import pi


class circle():
    def __init__(self, the_radius):
        self.radius = the_radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, the_diameter):
        self.radius = the_diameter / 2

    @property
    def area(self):
        return 2 * pi * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return circle(self.radius + other.radius)

    def __mul__(self, multiple):
        return circle(self.radius * multiple)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius
