#Circle Class

from math import pi

class Circle():
    """Generate a circle, radius, diameter and area."""
    
    def __init__(self, radius):
        """Create a circle using set radius value"""
        
        self.radius = radius
        
    @property #You can call it as a attribute rather than method
    def diameter(self): #diameter property
        """Gets the diameter of the circle."""
        
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        """Sets the diameter of the circle."""
        
        self.radius = value / 2
    
    @property
    def area(self):
        """Calculates area of the circle."""
        
        return pi * self.radius ** 2
    
    def __str__(self):
        """Shows informal string representation."""
        
        return f"Circle with radius: {self.radius}"
    
    def __repr__(self):
        """Shows class representation."""
        
        return f"Circle({self.radius})"
        
    def __add__(self, other):
        """Adds two circles together."""
        
        return Circle(self.radius + other.radius)
    
    def __mul__(self, other):
        """Multiples radius of a circle."""
        
        return Circle(self.radius * other)
    
    def __rmul__(other, self):
        """Multiples radius of a circle if first number is an integer."""
        
        return Circle(other.radius * self)
    
    """Rich Comparison methods"""
    def __eq__(self, other):
        """Compare with equal to."""
        
        return self.radius == other.radius
    
    def __lt__(self, other):
        """Compare with less than."""
        
        return self.radius < other.radius
    
    def __gt__(self, other):
        """Compare with greater than."""
        
        return self.radius > other.radius

    """    
    def __ne__(self, other):
        return self.radius != other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius
    
    def __ge__(self, other):
        return self.radius >= other.radius
    """
    