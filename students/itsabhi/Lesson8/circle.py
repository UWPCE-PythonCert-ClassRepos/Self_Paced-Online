#!/usr/bin/env python3

import math


class Circle:
    # Circle class
    _diameter = None  # This cannot be stored as its not an object attribute
    _area = None  # This cannot be stored as its not an object attribute

    @property
    def diameter(self):
        return self.radius*2

    def __init__(self, the_radius):
        self.radius = the_radius
        if not self.radius > 0:
            print("Invalid radius....\n")

    @diameter.setter
    def diameter(self, value):
        # Sets radius. Note diameter is not stored as its not an object attribute.
        self.radius = value/2

    @property
    def area(self):
        return (self.radius**2)*math.pi

    @classmethod
    def from_diameter(cls, diam):
        # Returns a Circle class object
        return cls(diam/2)

    def __str__(self):
        return("Circle with radius: "+str(self.radius))

    def __repr__(self):
        return("Circle({})".format(self.radius))
        #return(f"Circle({self.radius})")

    def __add__(self, other):
        sum_of_radius = self.radius + other.radius
        return ("Circle({})".format(sum_of_radius))

    def __mul__(self, other):
        multiplied = self.radius*other
        return ("Circle({})").format(multiplied)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def sort_key(self):
        return self.radius


class Sphere(Circle):

    def __str__(self):
        return ("Sphere with radius: " + str(self.radius))

    def __repr__(self):
        return ("Sphere({})".format(self.radius))

    @property
    def volume(self):
        return (self.radius ** 3) * math.pi * (4/3)

    @property
    def area(self):
        raise NotImplementedError


def main():

    c = Circle(4)
    print(c.radius)
    print(c.diameter)
    c.diameter = 2
    print(c.diameter)
    print(c.radius)
    c = Circle(2)
    print(c.area)
    #c.area = 4
    c = Circle.from_diameter(8)
    print(c.diameter)
    print(c.radius)
    print(c)
    d = eval(repr(c))
    print(repr(c))
    c1 = Circle(2)
    c2 = Circle(4)
    print(c1+c2)
    print(c2*3)
    print(c1 > c2)
    print(c1 < c2)
    print(c1 == c2)
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort(key=Circle.sort_key) # Sorts circles list based on key returned by sort_key function
    print(circles)

    # Object calls for Sphere
    s = Sphere(20)
    print(s)
    print(repr(s))
    print(s.volume)
    #print(s.area)


if __name__ == '__main__':
    main()