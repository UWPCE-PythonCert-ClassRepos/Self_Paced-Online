"""
Name: Muhammad Khan
Date: 04/01/2019
Assignment08

"""
import math as m

class Circle:
    """The initializer or the constructor for the Circle Class"""
    def __init__(self , radius):
        """Instance attributes are initalized here"""
        if radius < 0:
            raise TypeError("Invalid radius < 0")
        self.radius = radius


    @property
    def diameter(self):
        """Return the diameter of a circle"""
        return 2*self.radius


    @diameter.setter
    def diameter(self, diameter):
        """Set the radius"""
        self.radius = diameter / 2


    @property
    def area(self):
        """
        Area property--it can't be changed. Raises an AttributeError
        exception"""
        return m.pi*self.radius**2


    @classmethod
    def from_diameter(cls, diameter):
        """Alternative constructor"""
        return cls(diameter / 2)


    def __repr__(self):
        """Recreate the object and return it for the developer"""
        return "Circle({})".format(self.radius)


    def __str__(self):
        """Return a nicely printable string for the user"""
        return "Circle with radius: {}".format(self.radius)


    def __add__(self,other):
        """Add two circles."""
        return Circle(self.radius + other.radius)


    def __mul__(self,num):
        """Multiply a circle by a number"""
        return Circle(self.radius * num)


    def __rmul__(self,num):
        """Multiples radius of circle by an int but sequence reversed"""
        return Circle(self.radius*num)


    def __lt__(self, other):
        """Return true if the left circle is less than the right circle"""
        return self.radius < other.radius


    def __eq__(self, other):
        """Return true if both circles are equal"""
        return self.radius == other.radius


#########
#Optional
#########

#Augumented assignmnet operators.

    def __iadd__(self, other):
        """Augumented Addition """
        return Circle(self.radius + other.radius)


    def __imul__(self,num):
        """Augumented Multiplication"""
        return Circle(self.radius*num)

# With a similiar apprach, other augumented operaters can be defined as well.



if __name__ == "__main__":

    c = Circle(4)
    print("Diameter = ",c.diameter)
    print("change diameter...")
    c.diameter = 100
    print("Diameter = ",c.diameter)
    print("Alternative Constructor")
    c = Circle.from_diameter(16)
    print("diameter = ",c.diameter)
    print("radius = ", c.radius)

    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(6)
    print(c1+c2)
    print(repr(c3))
    print("Unsorted Circles: ")
    circles=[Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
              Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    print(circles)
    print("Sorted Circles: ")
    circles.sort()
    print(circles)


