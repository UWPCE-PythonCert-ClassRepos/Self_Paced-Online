from math import pi

class Circle:
    
    def __init__(self, the_radius):
        self.radius = the_radius 
        self._diameter = the_radius * 2
        self._area = pi * the_radius ** 2

    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = value / 2
    
    @property
    def area(self):
        return self._area
    
    @classmethod
    def from_diameter(cls, diameter):
        the_radius = diameter / 2
        return Circle(the_radius)
    
    def __str__(self):
        return "Circle with Radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __mul__(self, n_times):
        return Circle(self.radius * n_times)
    
    __rmul__ = __mul__
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self,other):
        return self.radius == other.radius
    
    def __truediv__(self, other):
        return Circle(self.radius / other.radius)