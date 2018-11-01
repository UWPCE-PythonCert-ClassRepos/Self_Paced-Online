# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:48:41 2018

@author: dennis
"""

def fibonacci(n):
    series = [0,1]
    for i in range(n):
        if i>1:
            series.append(series[i-2] + series[i-1])
    print(series[n-1])
    
fibonacci(7)
    
def lucas(n):
    series = [2,1]
    for i in range(n):
        if i>1:
            series.append(series[i-2] + series[i-1])
    print(series[n-1])
    
lucas(8)
    
def sum_series(n,pos1=0,pos2=1):
    series = [pos1,pos2]
    for i in range(n):
        if i>1:
            series.append(series[i-2] + series[i-1])
    print(series[n-1])
    
sum_series(8,2,1)
