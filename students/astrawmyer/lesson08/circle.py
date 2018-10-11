import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

        
    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return (self.radius**2) * math.pi
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
    
    def __str__(self):
        return "Circle with radius: {}".format(self.radius)
    
    def __repr__(self):
        return "Circle({})".format(self.radius)


c = Circle(5)
print(c.radius)
print(c.diameter)
print(c)
""" print(repr(c))
d = eval(repr(c))
print(d) """