# series.py
# Fibonacci, Lucas, sum_series assignment
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
# The first numbers are 2 & 1 and is the difference from the Fibonacci Series.
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n-2) + lucas(n-1))

def sum_series(x,y=0,z=1):
# This function allows for three parameters to compute a series that is
# similar to the Fibonacci & Lucas Series.  Where x is the nth value in
# the series, y is the first number in the series, & z is the second number.
# The user defines the first 2 numbers in the series.  If the user enters
# 0 & 1 then the result is the Fibonacci Series, if the user enters 2 & 1
# then the result is the Lucas Series.
    if x == 0:
        return y
    elif x == 1:
        return z
    else:
        return (sum_series(x-2,y,z) + sum_series(x-1,y,z))

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
    print ('This function returns the nth value in a series.')
    x=int(input('Enter a number for n to compute the nth value: '))
    y=int(input('Enter the first number in the series: '))
    z=int(input('Enter the second number in the series: '))
    print('The value is: ',end="")
    print (sum_series(x,y,z))

user_input()

def test_fibonacci():
# This function checks to make sure that the 10th fibonacci number is in fact 55
# If it isn't then it will raise an assertion failure.
    assert fibonacci(10) == 55

def test_lucas():
# This function checks to make sure that the 10th lucas number is in fact 123
# If it isn't then it will raise an assertion failure.
    assert lucas(10) == 123

def test_sum_series():
# This function checks to make sure that the 10th sum_series number is in fact 288
# If it isn't then it will raise an assertion failure.
    assert sum_series(10,2,4) == 288

print()
print ('The first 11 Fibonacci numbers are (zero based index):')
print ('0,1,1,2,3,5,8,13,21,34,55')
test_fibonacci()
print()
print ('The first 11 Lucas numbers are (zero based index):')
print ('2,1,3,4,7,11,18,29,47,76,123')
test_lucas()
print()
print ('The first 11 custom series using sum_series(10,2,4) are (zero based index):')
print ('2,4,6,10,16,26,42,68,110,178,288')
test_sum_series()
