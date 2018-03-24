#The Fibonacci Series is a numeric series starting with the integers 0 and 1.

#In this series, the next integer is determined by summing the previous two.

#This gives us:

# 0, 1, 1, 2, 3, 5, 8, 13, ...
# We will write a function that computes this series – then generalize it.
# 
# Step 1
# 
# Create a new module series.py in the lesson02 folder in your student folder.
# In it, add a function called fibonacci.
# The function should have one parameter, n.
# The function should return the nth value in the fibonacci series (starting with zero index)
# Ensure that your function has a well-formed docstring
# Note that the fibinacci series is naturally recursive – the value is defined by previous values:
# 
# fib(n) = fib(n-2) + fib(n-1)

def fibonacci (n):
    fib_nm2 = 0
    fib_nm1 = 1

    if n == 0: return 0
    if n == 1: return 1

    fib_n = None
    for i in range(n - 1):
        fib_n = fib_nm1 + fib_nm2
        fib_nm2 = fib_nm1
        fib_nm1 = fib_n
    return fib_n

def fibonacci_recursive (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Lucas Numbers
# 
# The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
# 
# 2, 1, 3, 4, 7, 11, 18, 29, ...
# In your series.py module, add a new function, lucas, that returns the nth value in the lucas numbers series.
# 
# Ensure that your function has a well-formed doc
# Lucas Numbers
# 
# The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
# 
# 2, 1, 3, 4, 7, 11, 18, 29, ...
# In your series.py module, add a new function, lucas, that returns the nth value in the lucas numbers series.
# 
# Ensure that your function has a well-formed doc


def lucas (n):
    luc_nm2 = 2
    luc_nm1 = 1

    luc = None
    if n == 0: return 2
    if n == 1: return 1
    for i in range( n -1 ):
        luc_n = luc_nm2 + luc_nm1
        luc_nm2 = luc_nm1
        luc_nm1 = luc_n
    return luc_n

    
def lucas_recursive(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas_recursive(n-1) + lucas_recursive(n-2)



# Generalizing
# 
# Both the fibonacci series and the lucas numbers are based on an identical formula.
# 
# Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
# 
# Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series.
# 
# Note: While you could check the input arguments, and then call one of the functions you wrote, the idea of this exercise is to make a general function, rather than one specialized. So you should reimplement the code in this function.
# 
# In fact, you could go back and reimplement your fibonacci and lucas functions to call this one with particular arguments.
# 
# Ensure that your function has a well-formed docstring

def sum_series( n, nm2=0, nm1=1):
    if n == 0: return nm2
    if n == 1: return nm1
    else:
        for i in range (n-1):
            num = nm2 + nm1
            nm2 = nm1
            nm1 = num
        return num 

    
       
    




# print('fibonacci(0): %s' % fibonacci(0))
# print('fibonacci(0): %s' % fibonacci(0))
# print('lucas(1): %s' % lucas(1))
# print('lucas(1): %s' % lucas(1))
# 
# print('CALL fibonacci(5)')
# print('fibonacci(2): %s' % fibonacci(2))
# print('CALL lucas(5)')
# print('lucas(2): %s' % lucas(2))

# Iterative
for i in range(10):
    print('fib(%s) = %s' % (i, fibonacci(i)))

# Recursive
for i in range(10):
    print('fib_recursive(%s) = %s' % (i, fibonacci_recursive(i)))

for i in range(10):
    print('sss---(%s) = %s' % (i,sum_series(i)))


# lucas Iterative
for i in range(10):
    print('lucas(%s) = %s' % (i, lucas(i)))

for i in range(10):
    print('lucas_recursive(%s) = %s' % (i, lucas_recursive(i)))

for i in range(10):
    print('sss (%s) = %s' % (i, sum_series(i, 2, 1)))
