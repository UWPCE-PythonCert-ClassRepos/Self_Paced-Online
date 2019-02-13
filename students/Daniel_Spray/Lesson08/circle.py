import math

class Circle:
    def __init__(self, the_radius):
        self.radius = the_radius

    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self,new_diameter):
        self.radius = new_diameter/2

    @property
    def area(self):
        return math.pi*self.radius**2

    @classmethod
    def from_diameter(cls,diameter):
        return cls(diameter/2)

    def __str__(self):
        return "Circle with radius: "+str(self.radius)

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self,other):
        if isinstance(other,(float,int)):
            return Circle(self.radius + other)
        elif isinstance(other,Circle):
            return Circle(self.radius + other.radius)

    def __mul__(self,other):
        if isinstance(other,(float,int)):
            product = Circle(self.radius * other)
        elif isinstance(other,Circle):
            product = Circle(self.radius * other.radius)
        return product

    def __lt__(self,other):
        return self.radius < other.radius

    def __eq__(self,other):
        return self.radius == other.radius

    def __gt__(self,other):
        return self.radius > other.radius