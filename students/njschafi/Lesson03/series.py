
## NEIMA SCHAFI, LESSON 2 Assignment - Fibonacci Series Exercise

###FIBONACCI series recursive function
def fibonacci(n):
    """The recursive function that returns nth fibonacci value"""
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

###LUCAS series recursive function
def lucas(n):
    """The recursive function that returns nth lucas value"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

###SUM_SERIES recurives function
"""The recursive function that returns nth value of a sequence based on inputted optional variables x,y"""
def sum_series(n,x=0,y=1):
    if n == 0:
        return x ###1st number in series
    elif n == 1:
        return y ###2nd number in series
    else:
        return sum_series(n-2,x,y) + sum_series(n-1,x,y)

###TEST BLOCK
#check fibonacci() outputs correctly
assert fibonacci(12) == 233 #Test to check that the 12th Fibonacci number is 233 using the recusive function fibonacci()
assert fibonacci(0) == 1

#check lucas() outputs correctly
assert lucas(11) == 199
assert lucas(4) == 7 #Test to check that the 4th Lucas number is 7 using the recusive function Lucas()
assert lucas(0) == 2

#check sum_series outputs correctly
assert sum_series(11,2,1) == 199 #Test to check that passing in different optional variables results in correct outputted values from sum_series()
assert sum_series(0,0,1) == 0
assert sum_series(1,0,1) == 1
