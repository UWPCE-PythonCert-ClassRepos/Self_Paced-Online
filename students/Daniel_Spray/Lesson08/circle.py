import math

class Circle:
    """Create a class for building a circle"""

    def __init__(self, the_radius):
        """Initialize radius"""
        self.radius = the_radius

    @property
    def diameter(self):
        """Create a property for radius"""
        return self.radius*2

    @diameter.setter
    def diameter(self,new_diameter):
        """Create a way to set the diameter"""
        self.radius = new_diameter/2

    @property
    def area(self):
        """Create a property for area"""
        return math.pi*self.radius**2

    @classmethod
    def from_diameter(cls,diameter):
        """Make a method to set the radius directly from the diameter"""
        return cls(diameter/2)

    def __str__(self):
        """Add a printable string method"""
        return "Circle with radius: "+str(self.radius)

    def __repr__(self):
        """Add a printable string method"""
        return f"Circle({self.radius})"

    def __add__(self,other):
        """Incorporate addition functionality"""
        return Circle(self.radius + other.radius)

    def __mul__(self,other):
        """Incorporate multiplication functionality"""
        return Circle(self.radius * other)

    def __rmul__(other,self):
        """Incorporate multiplication functionality if first number is an int"""
        return Circle(other.radius * self)

    def __lt__(self,other):
        """Allow to compare with less than"""
        return self.radius < other.radius

    def __eq__(self,other):
        """Allow to compare with equal to"""
        return self.radius == other.radius

    def __gt__(self,other):
        """Allow to compare with greater than"""
        return self.radius > other.radius

