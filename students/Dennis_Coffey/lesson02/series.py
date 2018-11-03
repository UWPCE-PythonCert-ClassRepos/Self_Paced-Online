# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:48:41 2018

@author: dennis
"""

"""Returns the value of the nth position in a summing series"""
def sum_series(n,pos0=0,pos1=1):
    series = [pos0,pos1]
    for i in range(n+1):
        if i>1:
            series.append(series[i-2] + series[i-1])
    return series[n]

"""Returns the value of the nth position in a fibonacci series"""
def fibonacci(n):
    return sum_series(n)
    
"""Returns the value of the nth position in a lucas series"""
def lucas(n):
    return sum_series(n,2,1)
    
print(sum_series(6,2,1))
print(fibonacci(6))
print(lucas(5))

if __name__ == "__main__":
    
    print('Running tests')
    #test n=0 and n=1 for fibonacci series
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    #test for another fibonacci series
    assert fibonacci(6) == 8
    #tests for lucas series
    assert lucas(5) == 11
    assert lucas(1) == 1
    assert lucas(0) == 2
    #tests for generic series
    assert sum_series(6,2,1) == 18
    assert sum_series(4,5,2) == 16
    print('Test passed')