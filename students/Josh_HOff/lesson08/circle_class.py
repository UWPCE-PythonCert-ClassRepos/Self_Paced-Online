import sys
import copy
import math
import pathlib

class Circle(object):

    def __init__(self, value):
        self._radius = value
        self._diameter = value * 2
        self._area = (math.pi) * (value ** 2)
        
    @classmethod
    def from_diameter(cls, value):
        cls.radius = value / 2
        cls.diameter = value
        cls.area = (.25 * math.pi) * (value ** 2)
        return cls
        
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2
        self._area = (math.pi) * (value ** 2)
    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2
        self._area = (.25 * math.pi) * (value ** 2)
    @property
    def area(self):
        return self._area
    @area.setter
    def area(self, value):
        raise AttributeError
    @area.deleter
    def area(self):
        del self._area
    @diameter.deleter
    def diameter(self):
        del self._diameter
    @radius.deleter
    def radius(self):
        del self._radius
        
    def __add__(self, other_circle):
        return Circle( self._radius + other_circle._radius)
        
    def __mul__(self, other_circle):
        print(self._radius)
        print(other_circle)
        return Circle(other_circle * self._radius)
        
    def __lt__(self, other_circle):
        return self._radius < other_circle._radius
        
    def __gt__(self, other_circle):
        return self._radius > other_circle._radius
        
    def __eq__(self, other_circle):
        return self._radius == other_circle._radius
    
    def __str__(self):
        return f'Circle with radius: {self.radius}'
        
    def __repr__(self):
        return f'Circle({self.radius})'
        
    __rmul__ = __mul__
        
'''def get_user_radius():
    return input(f'\nWhat is the Radius?: ')

    
def get_user_diameter():
    return input(f'\nwhat is the Diameter?: ')

    
def quitting():
    sys.exit()

    
def continue_func():
    return

switch_func_dict = {'1':get_user_radius, '2':get_user_diameter, 'quit':quitting}'''
        
if __name__ == '__main__':
    c = Circle(50)

'''    while True:
        response = input(f'1: Radius\n2: Diameter\n')
        var = float(switch_func_dict.get(response, continue_func)())
        
        if response == '1':
            c.radius = var
            
        elif response == '2':
            c.diameter = var
        else:
            continue'''