########################################################
#Author: Kennan Yilmaz
#Date: 10/17/2018
#Description:  This module contains code that prints Fiboniacci and
# Lucas numbers
########################################################

def fiboniacci(n):
    """ This function produces the nth value in Fiboniacci series"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fiboniacci (n-2) + fiboniacci(n-1)  # Recursive

def lucas(n):
    """ This function produces the nth value in Lucas series"""

    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas (n-2) + lucas(n-1)  # Recursive

def sum_series(n, firstval=0, secondval=1):
    """ This function produces the nth value of a generic series"""

    if firstval==0 and secondval==1:
        #Fiboniacci numbers
        return n
    elif firstval==2 and secondval==1:
        #Lucas series
        if n==0:
            return 2
        elif n==1:
            return 1

        return sum_series (n-1, firstval, secondval) + sum_series (n-2, firstval, secondval)  # Recursive

#Write test cases
#Fiboniacci 8th value
testval=fiboniacci (8)
assert(testval==21), "Fiboniacci 8th value is wrong!"

#Lucas 5th value
testval=lucas (5)
assert(testval==11), "Lucas 5th value is wrong!"

#Generic function 10th value
testval=sum_series (10)
assert(testval==10), "Generic function 10th value is wrong!"


