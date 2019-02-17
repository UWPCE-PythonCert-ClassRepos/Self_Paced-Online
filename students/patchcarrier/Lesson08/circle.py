import math
from functools import total_ordering

@total_ordering
class Circle:
    """Class used to represent a circle.
    
    A circle is defined by the radius and diameter attriutes.
    """
    
    def __init__(self, radius):
        """Create a circle instance with the specified radius. 
        
        Circle.diameter is set automatically to be consistent with the given radius.
        """
        self.radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        """Update self.radius to the specified value and update  
        self.diameter accordingly."""
        # Only allow radius values that can be converted to a float
        try:
            self._radius = float(new_radius)
        except (TypeError, ValueError) as the_error:
            the_error.args = "Circle.radius must be convertable to type float",
            raise the_error
        self._diameter = 2 * self._radius    
        
    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, new_diameter):
        """Update self.diameter to the specified value and update  
        self.radius accordingly."""
        # Only allow diameter values that can be converted to a float
        try:
            self._diameter = float(new_diameter)
        except (TypeError, ValueError) as the_error:
            the_error.args = "Circle.diameter must be convertable to type float",
            raise the_error
        self._radius = self._diameter / 2
        
    @property
    def area(self):
        return math.pi * self._radius**2
        
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    
    def __str__(self):
        return "Circle with radius = {:f}".format(self.radius)
    
    def __repr__(self):
        return "Circle({:f})".format(self.radius)
    
    def __add__(self, other):
        return type(self)(self.radius + other.radius)

    def _multiply(self, other):
        # Allow other to be types that can be converted to a float(),
        # except strings (only want types that represent numbers)
        if type(other) == str: return NotImplemented
        
        try:
            factor = float(other)
        except (ValueError, TypeError):
            return NotImplemented
        
        return type(self)(self.radius * factor)


    def __mul__(self, other):
        return self._multiply(other)
        
    def __rmul__(self, other):
        return self._multiply(other)
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def sort_key(self):
        return self.radius
        