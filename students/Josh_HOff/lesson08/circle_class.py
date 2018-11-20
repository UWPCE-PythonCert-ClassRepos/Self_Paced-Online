import sys
import copy

class Circle(object):

    def __init__(self, value):
        self._radius = value
        self._diameter = value * 2
        
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2
    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2
    @diameter.deleter
    def diameter(self):
        del self._diameter
    @radius.deleter
    def radius(self):
        del self._radius

        
        
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