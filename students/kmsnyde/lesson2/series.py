# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:31:18 2018

@author: Karl M. Snyder
"""

def fibonacci(n):
    """Creates a fibonacci sequence with the number of elements determined
    by the "n" parameter"""
    
    list = []
    for i in range(n):
        if (i == 0) or (i == 1):
            list.append(i)
        else:
            list.append(list[-1] + list[-2])
    print(*list, '\n')
    return list
fibonacci(20)

def lucas(n):
    """The Lucas Numbers are a related series of integers that start with
    the values 2 and 1.  Returns the nth value in the lucas numbers series."""
    
    list = [2, 1]
    for i in range(n-2):
        list.append(list[-1] + list[-2])
    print(*list, '\n')
    return list
lucas(20)

def sum_series(count, start1=0, start2=1):
    """Creates a sequence of length "count", in which the first 2 elements
    default to 0 and 1, or which may be changed to any 2 numbers when calling
    the function using start1/start2 argument positions."""
    
    if start1 == 0 and start2 == 1:
        list = []
        for i in range(count):
            if (i==0) or (i==1):
                list.append(i)
            else:
                list.append(list[-2] + list[-1])
    else:
        list = [start1, start2]
        for i in range(count - 2):
            list.append(list[-2] + list[-1])
    print(*list, '\n')
    return list
sum_series(20, 4, 2)

if __name__ == "__main__":
    # Tests if the function produces a sequence of the number of elements
    # provided by the argument.  Result is a number sequnce if True, or 
    # AssertionError if False.
    assert len(fibonacci(10)) == 10
    assert len(lucas(5)) == 5 # AssertionError if not 5
    assert len(sum_series(8)) == 8
    
    # Tests if the first number of the fibonacci (0) and lucas (2) sequences
    # are correct.  AssertionError if False.
    assert fibonacci(5)[0] == 0
    assert lucas(5)[0] == 2
    # Tests if the second element of the sequence (third argument) is correct
    # Assertion error if False.
    assert sum_series(5, 3, 2)[1] == 3 #AssertionErrof if not 2