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
        diameter() then returns the diameter as radius * 2, giving 
        '''
        self.radius = val / 2

    @property
    def area(self):
        return self.radius * self.radius * pi

    @classmethod
    def from_diameter(cls, val):
        return cls(val / 2)


if __name__ == "__main__":
    circle = Circle(5)
    
    