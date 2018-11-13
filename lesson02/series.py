"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    November 6th 2018
"""

#Fibonacci Sequence: N is the sum of the previous two numbers
def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) #recursive call

#Lucas Sequence: Same formula as Fibonacci but starting with zero and one
def lucas(n):
    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        return lucas(n-1) + lucas(n-2)#recursive call

"""
    Sum-Series Sequence: Default is Fibonacci and Lucas can be used with two
    and one as the additional parameters (n, 2, 1) - other variations can use
    the same formula
"""
def sum_series(n, zero=0, one=1):
    if (n == 0):
        return zero
    elif (n == 1):
        return one
    else:
        #recursive call using what was originally passed (or defaults)
        return sum_series(n-1, zero, one) + sum_series(n-2, zero, one)

#Assert Statements: Will display alert message if expected output is incorrect
#Fibonacci
assert fibonacci(0) == 0, "fibonacci(0) = 0 FAILED"
assert fibonacci(5) == 5, "fibonacci(5) = 5 FAILED"
assert fibonacci(7) == 13, "fibonacci(7) = 13 FAILED"
#Lucas
assert lucas(0) == 2, "lucas(0) = 2 FAILED"
assert lucas(3) == 4, "lucas(3) = 4 FAILED"
assert lucas(6) == 18, "lucas(6) = 18 FAILED"
#Sum-Series: Fibonacci, Lucas, and 'Other' using different starting numbers
assert sum_series(7) == 13, "sum_series(7) = 13 FAILED"
assert sum_series(6, 2, 1) == 18, "sum_series(6, 2, 1) = 18 FAILED"
assert sum_series(8, 4, 3) == 115, "sum_series(8, 4, 3) = 115 FAILED"

"""
    Additional fucntions for fibonacci and lucas but utilizing the
    sum_series function. Asserts are included as well.
"""
#Fibonacci
def fibonacci2(n):
    return sum_series(n)

#Lucas
def lucas2(n):
    return sum_series(n, 2, 1)

#Assert Statements: Will display alert message if expected output is incorrect
#Fibonacci
assert fibonacci2(0) == 0, "fibonacci(0) = 0 FAILED"
assert fibonacci2(5) == 5, "fibonacci(5) = 5 FAILED"
assert fibonacci2(7) == 13, "fibonacci(7) = 13 FAILED"
#Lucas
assert lucas2(0) == 2, "lucas(0) = 2 FAILED"
assert lucas2(3) == 4, "lucas(3) = 4 FAILED"
assert lucas2(6) == 18, "lucas(6) = 18 FAILED"