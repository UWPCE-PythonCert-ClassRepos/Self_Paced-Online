# Write a class for a quadratic equation.

# The initializer for that class should take the parameters: a, b, c
# It should store those parameters as attributes.
# The resulting instance should evaluate the function when called, and return the result:
# my_quad = Quadratic(a=2, b=3, c=1)

# my_quad(0)

class Quadratic(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x**2 + self.b *x + self.c

