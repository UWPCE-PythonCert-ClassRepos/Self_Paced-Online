# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:31:18 2018

@author: Karl M. Snyder
"""

def fibonacci(n):
    """Creates a fibonacci sequence that displays the nth number in the
    sequence, identified by the "n" parameter"""
    
    fib_list = []
    for i in range(n):
        if (i == 0) or (i == 1):
            fib_list.append(i)
        else:
            fib_list.append(fib_list[-1] + fib_list[-2])
    print(fib_list[n-1], '\n')
    return fib_list[n-1]
    
fibonacci(10)

def lucas(n):
    """The Lucas Numbers are a related series of integers that start with
    the values 2 and 1.  Returns the nth value in the lucas numbers series."""
    
    lucas_list = [2, 1]
    for i in range(n-2):
        lucas_list.append(lucas_list[-1] + lucas_list[-2])
    print(lucas_list[n-1], '\n')
    return lucas_list[n-1]
lucas(20)

def sum_series(n, start1=0, start2=1):
    """Creates a sequence of length "n", in which the first 2 elements
    default to 0 and 1 (fibonaccie), or which may be changed to any 2
    numbers when calling the function using start1/start2 argument
    positions. Returns the nth value in the sequence, as chosen by the 
    'n' parameter."""
    
    if start1 == 0 and start2 == 1:
        series_list = []
        for i in range(n):
            if (i==0) or (i==1):
                series_list.append(i)
            else:
                series_list.append(series_list[-2] + series_list[-1])
    else:
        series_list = [start1, start2]
        for i in range(n - 2):
            series_list.append(series_list[-2] + series_list[-1])
    print(series_list[n-1], '\n')
    return series_list[n-1]
sum_series(21, 4, 5)

if __name__ == "__main__":
    # Tests if the function produces the number chosen in as parameter "n".
    # remove comment (#) before assert below to test that assertion, add 
    # comment (#) to remove test
    assert fibonacci(10) == 34  #Returns no error
    #assert fibonacci(10) == 233 #Returns error; answer = 233
    #assert lucas(7) == 18 #Returns no error
    #assert lucas(12) == 322 # Returns error: answer = 199
    #assert sum_series(20, 4, 5) == 31241 #Returns no error
    #assert sum_series(10, 4, 5) == 665 #Returns error; answer = 254