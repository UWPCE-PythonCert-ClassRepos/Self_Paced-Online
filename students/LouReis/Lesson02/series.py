# series.py
# Fibonacci assignment
# Coded by LouReis
#
# Note that the Fibonacci Series is naturally recursive –
# the value is defined by previous values:
# fib(n) = fib(n-2) + fib(n-1)

# This function calculates the nth value in the Fibonacci Series.
# This is a recursive funtion.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-2) + fibonacci(n-1))

# This function calculates the nth value of the Lucas Series.
# The first numbers are 2 & 1 is the difference from the Fibonacci Series.
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n-2) + lucas(n-1))

def sum_series(x,y=0,z=1):
    if x == 0:
        return y
    elif x == 1:
        return z
    else:
        return (sum_series(x-2,y,z) + sum_series(x-1,y,z))

def sum_series(x,y=0,z=1):
    if y == 0 and z == 1:
        if x <= 1:
            return x
        else:
            return (sum_series(x-2) + sum_series(x-1))
    elif y == 2 and z == 1:
        if x == 0:
            return 2
        elif x == 1:
            return 1
        else:
            return (sum_series(x-2) + sum_series(x-1))
    else:
        if x <= 1:
            return y
        elif x == 2:
            return z
        else:
            return (sum_series(x-2) + sum_series(x-1))

def sum_series (x,y=0,z=1):
    if x <= 1:
        return y
    elif x == 2:
        return z
    else:
        return (sum_series(x-2) + sum_series(x-1))


def user_input():
#This function prompts the user for the square size & grid dimensions.
    print ('This function returns the nth value in the Fibonacci series.')
    n=int(input('Enter a number for n to compute the nth value: '))
    print('The value is: ',end="")
    print (fibonacci(n))
    print ('This function returns the nth value in the Lucas series.')
    n=int(input('Enter a number for n to compute the nth value: '))
    print('The value is: ',end="")
    print (lucas(n))

user_input()
