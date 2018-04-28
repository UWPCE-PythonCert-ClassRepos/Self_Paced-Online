# Thomas Horn
# Assignment: The Circle Class
# Class representing a circle.
# Commands:
#  Query the circle using either the radius or diameter.
#  Compute area
#  Print the circle
#  Add 2 circles
#  Compare 2 circle's sizes
#  Sort a list of circles

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        ''' 
        Sets the radius to half the val, changing the og radius.  
        diameter() then returns the diameter as radius * 2.
        '''
        self.radius = val / 2

    @property
    def area(self):
        return self.radius * self.radius * pi

    @classmethod
    def from_diameter(cls, val):
        '''
        Working with class, not the instance of the class when called.
        '''
        return cls(val / 2)

    # Magic Methods

    def __repr__(self):
        return(f"Circle {self.radius}")

    def __str__(self):
        return(f"Circle - Radius: {self.radius}")

    def __add__(self, circle2):
        return self.radius + circle2.radius

    def __mul__(self, circle2):
        return self.radius * circle2.radius

    # Comparison Methods:  eq, ne, lt, gt, le, ge

    def __eq__(self, circle):
        return self.radius == circle2.radius

    def __ne__(self, circle2):
        return self.radius != circle2.radius

    def __lt__(self, circle2):
        return self.radius < circle2.radius

    def __gt__(self, circle2):
        return self.radius > circle2.radius

    def __le__(self, circle2):
        return self.radius <= circle2.radius

    def __ge__(self, circle2):
        return self.radius >= circle2.radius

    def __iadd__(self, circle2):
        # Must return self since it's adding to itself
        self.radius += circle2.radius
        return self 

if __name__ == "__main__":
    circle = Circle(5)
    circle2 = Circle(6)
    circle += circle2
    print(circle)


    pass
    