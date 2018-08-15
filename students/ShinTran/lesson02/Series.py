'''
Shin Tran
Python 210
Lesson 2 Assignment
'''

# Prints the Fibonacci series up to a given number passed as a parameter
# 0, 1, 1, 2, 3, 5, 8, 13
def fibonacci(n):
    x = 0
    y = 1
    print(f"This prints the first {n} numbers of the Fibonacci series.")
    if n >= 1:
        print(x)
    if n >= 2:
        print(y)
    for i in range(3,n+1):
        z = x + y
        x = y
        y = z
        print(z)
    print()

# Prints the Lucas series up to a given number passed as a parameter
# 2, 1, 3, 4, 7, 11, 18, 29, ...
def lucas(n):
    x = 2
    y = 1
    print(f"This prints the first {n} numbers of the Lucas series.")
    if n >= 1:
        print(x)
    if n >= 2:
        print(y)
    for j in range(3,n+1):
        z = x + y
        x = y
        y = z
        print(z)
    print()

'''
Add a third function called sum_series with one required parameter
and two optional parameters. The required parameter will determine
which element in the series to print. The two optional parameters
will have default values of 0 and 1 and will determine the first two
values for the series to be produced.
Calling this function with no optional parameters will produce numbers
from the fibonacci series. Calling it with the optional arguments 2 and 1
will produce values from the lucas numbers. Other values for the optional
parameters will produce other series.
'''
def sum_series(n, x = 0, y = 1):
    print(f"This prints the first {n} numbers of a custom series based on your parameters of {x} and {y}.")
    if n >= 1:
        print(x)
    if n >= 2:
        print(y)
    for j in range(3,n+1):
        z = x + y
        x = y
        y = z
        print(z)
    print()

# Python program to use main for function call
if __name__ == "__main__":
    fibonacci(15)
    lucas(15)
    sum_series(15)
    sum_series(15,2,1)
    sum_series(15,3,2)