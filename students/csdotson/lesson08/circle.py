class Circle:
    """Create a Circle class representing a simple circle"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2
