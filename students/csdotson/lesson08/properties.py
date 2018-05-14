class PythonStyle:

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        if val < 0:
            raise ValueError("x can't be less than 0!")
        self._x = val

    @property  # Decorator
    def y(self):
        return 2 * self.x

    @y.setter
    def y(self, val):
        self.x = val / 2

    def __repr__(self):
        return "PythonStyle({})".format(self.x)
