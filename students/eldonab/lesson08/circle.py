 #!/usr/bin/python
import math


class Circle:
    """create a circle class that represents a simple circle"""

    def __init__(self, radius):
        self.radius = radius
      

    @property
    def diameter(self):
        return self.radius * 2


    @diameter.setter
    def diameter(self, value):
        self.radius = value/2


    @property
    def area(self):
        return math.pi * self.radius ** 2


    @classmethod
    def from_diameter(cls, diameter):
        # needs to return Circle(radius)
        radius = diameter/2 
        return cls(radius)


    def __repr__(self):
        return f"Circle({self.radius})"


    def __str__(self):
        return f"Circle with radius: {float(self.radius)}"
    

    def __add__(self, other):
        return Circle(self.radius + other.radius)


    def __mul__(self, other):
        #circle(5) * 3
        return Circle(self.radius * other)


    def __lt__(self, other):
        return self.radius < other.radius


    def __eq__(self, other):
        return self.radius == other.radius
    
 
    def __gt__(self, other):
        self.radius > other.radius


    def __ne__(self, other):
        return self.radius != other.radius

    def __rmul__(self, other):
        return Circle(other * self.radius)


    def __iadd__(self, other):
        return Circle(self.radius + other.radius)


    def __imul__(self, other):
        return Circle(self.radius * other)


class Sphere(Circle):
    """Create a simple sphere as a subclass of Circle class"""

    def __init__(self, radius):
        super().__init__(radius)


    def __str__(self):
        return f"Sphere with a radius: {float(self.radius)}"


    def __repr__(self):
        return f"Sphere({self.radius})"

    @property
    def volume(self):
        return 4/3*math.pi*(self.radius**3)


    @property 
    def area(self):
        return 4*math.pi*(self.radius**2)




