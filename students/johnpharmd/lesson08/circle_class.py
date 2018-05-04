

class Circle:
    """represents a simple circle, using properties, a class method, and
    special methods"""
    
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
