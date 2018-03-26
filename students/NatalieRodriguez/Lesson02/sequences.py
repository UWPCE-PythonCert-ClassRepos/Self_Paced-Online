# Fibonacci Sequence
# Natalie Rodriguez
# 3/8/2018

def fib_seq(n):
#using recursion to calculate the Fibonacci Sequence
#have the user call the function to name the 'n'th term
#of the sequence.

    if n == 0:
        return 0 #the zeroth term. These would not follow the formula below if called.
    elif n == 1: #the first term
        return 1
    else:
        return (fib_seq(n - 1) + fib_seq(n - 2))


input("Press enter to exit") #to see that it reaches the end of the program

#____________________________________________________________
# Lucas Numbers
# Natalie Rodriguez
# 3/8/2018


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

input("press enter to exit") #to see that it reaches the end of the program

#_________________________________________________________________
# General Function
# Natalie Rodriguez
# 3/8/2018

def sum_series(n, y=0, z=1):
    if n == 0:
        return y #optional value with default of 0
    elif n == 1:
        return z #optional value with default of 1
    else:
        return(sum_series(n-1, y, z) + sum_series(n-2, y, z))

input("press enter to exit")  # to see that it reaches the end of the program

#________________________________________________________________________
# Assert Testing
# Natalie Rodriguez
# 3/9/2018

#Create assert statements for the functions to test if it comes out as true or not.
#If the statement reads as false, it will throw an assert exception.
#I tested instances of different 'n'th terms.

assert fib_seq(3) == 2
assert fib_seq(7) == 13
assert fib_seq(11) == 89

assert lucas(2) == 3
assert lucas(4) == 7
assert lucas(6) == 18

assert sum_series(0) == 0
assert sum_series(8) == 21
assert sum_series(3, 0, 1) == 2 #fibonacci replication
assert sum_series(6, 2, 1) == 18 #lucas replication