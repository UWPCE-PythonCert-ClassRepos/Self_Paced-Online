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
        if isinstance(other,(float,int)):
            return Circle(self.radius + other)
        elif isinstance(other,Circle):
            return Circle(self.radius + other.radius)

    def __radd__(self,other):
        """Incorporate addition functionality if int is first"""
        if isinstance(self,(float,int)):
            return Circle(self + other.radius)
        elif isinstance(self,Circle):
            return Circle(self.radius + other)

    def __mul__(self,other):
        """Incorporate multiplication functioality"""
        product = Circle(self.radius * other)
        return product

    def __rmul__(other,self):
        """Incorporate multiplication functioality if first number is an int"""
        product = Circle(other.radius * self)
        return product

    def __lt__(self,other):
        """Allow to compare with less than"""
        return self.radius < other.radius

    def __eq__(self,other):
        """Allow to compare with equal to"""
        return self.radius == other.radius

    def __gt__(self,other):
        """Allow to compare with greater than"""
        return self.radius > other.radius

