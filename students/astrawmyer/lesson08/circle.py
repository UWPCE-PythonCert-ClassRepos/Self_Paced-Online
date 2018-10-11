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


    def __add__(self, other):
        new_circle = self.radius + other.radius
        return Circle(new_circle)
    

    def __mul__(self, other):
        new_circle = self.radius * other
        return Circle(new_circle)
    

    def __rmul__(self, other):
        new_circle = self.radius * other
        return Circle(new_circle)


    def __lt__(self, other):
        return self.radius < other.radius
    

    def __gt__(self, other):
        return self.radius > other.radius


    def __eq__(self, other):
        return self.radius == other.radius


circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
circles.sort()
print(circles)