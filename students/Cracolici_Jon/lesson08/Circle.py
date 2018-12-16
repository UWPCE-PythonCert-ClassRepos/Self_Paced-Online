#Jon Cracolici
#UW-Python Cert
#Lesson 08 - Creating a Circle Class w/Tests


import math

class Circle:
    """This is my Circle class. It constructs a circle using the radius, or the diameter. """
    def __init__(self, radius):
        """This is the initializer, which also checks the input of radius. Task 1"""
        try:
            radius = float(radius)
            if (radius < 0.0) == True:
                print('The radius must be a non-negative numeric value.')
                return None
                #I put this here to abort construction. Im not sure its working the way I want.
            else:
                pass
        except TypeError:
            print('You have entered a non-numeric value for the radius.')
            return None
        except ValueError:
            print('You have entered a non-numeric value for the radius.')
            return None
        #Class parameters (radius, diameter)
        self._radius = radius
        #Task 1
        self._diameter = self._radius*2
        #Task 2


    @classmethod
    def from_diameter(clas, diameter):
        """Alternate initializer:
        Uses the diameter instead of the radius as the parameter.
        Task 5."""
        return clas(diameter/2.0)


    @property
    def radius(self):
        return self._radius


    @property
    def diameter(self):
        """Returns Diameter - Task 3."""
        return self._diameter


    @property
    def area(self):
        """Sets area property - Task 4."""
        return math.pi*self._radius*self._radius
    
    
    #Enables setting radius and diameter on existing instance.
    @radius.setter
    def radius(self, value):
        try:
            value = float(value)
            if (value < 0.0) == True:
                print('The radius must be a non-negative numeric value.')
                return False #I put this here to abort construction
            else:
                pass
                
        except TypeError:
            print('You have entered a non-numeric value for the radius.')
            return None
        except ValueError:
            print('You have entered a non-numeric value for the radius.')
            return None
        self._radius = value
        self._diameter = value*2
        

    @diameter.setter
    def diameter(self, value):
        """Allows setting of diameter property - Task 3."""
        try:
            value = float(value)
            if (value < 0.0) == True:
                print('The diameter must be a non-negative numeric value.')
                return None
            else:
                pass
                
        except TypeError:
            print('You have entered a non-numeric value for the diameter.')
            return None
        except ValueError:
            print('You have entered a non-numeric value for the diameter.')
            return None
        self._radius = value/2.0
        self._diameter = value

    # Printing Functionality - Task 6
    def __str__(self):
        return 'A circle with radius {:.2f}.'.format(self._radius)

    def __repr__(self):
        return 'Circle ({:.2f})'.format(self._radius)


    #Math Functionality - Task 7
    def __add__(self, other):
        return Circle(self._radius + other._radius)
    
    
    def __sub__(self, other):
        return Circle(self._radius - other._radius)
    
    
    def __mul__(self, other):
        #I could probably add a try except block here.
        if isinstance(other, Circle):
            return Circle(self._radius * other._radius)
        else:
            return Circle(self._radius * other)
    
    
    #Comparison Functionality - Task 8
    def __lt__(self, other):
        return self._radius < other._radius
    
    
    def __gt__(self, other):
        return self._radius > other._radius
    
    
    def __eq__(self, other):
        return self._radius == other._radius
    
    

    