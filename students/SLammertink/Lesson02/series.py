# Author SLammertink
# UW Lesson 02 series.py exercises
# Calculate Fibonacci, Lucas and a sum_series series


# Function that calculates the nth number in a Fibonacci list
def fibonacci(n):
    ''' The function should return the nth value in the fibonacci series (starting with zero index)'''
    return sum_series(n) # this function uses the function sum_series() to calculate the Fibonacci number


# Function that calculates the nth number in a Lucas list

def lucas(n):
    ''' a function, lucas, that returns the nth value in the lucas numbers series.'''
    return sum_series(n, 2, 1) # This function uses the sum_series() function to calculate the Lucas number

# Fuction for the sum_series assigmnet in Lesson 2

def sum_series(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return sum_series(n-1, a, b) + sum_series(n-2, a, b)

## Assert the functions:

# Fibonacci:
assert fibonacci(3) == 2
assert fibonacci(8) == 21
assert fibonacci(29) == 514229

# Lucas

assert lucas(3) == 4
assert lucas(8) == 47
assert lucas(29) == 1149851

# num_series:

assert num_series(3, 4, 3) == 10
assert num_series(3, 4, 8) == 20
