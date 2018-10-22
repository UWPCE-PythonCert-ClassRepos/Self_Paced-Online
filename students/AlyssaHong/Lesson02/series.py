"""
Author: Alyssa Hong
Date: 10/11/2018
Lesson2 Assignments > Fibonacci Series Exercise
"""

# Goal : The Fibonacci Series is a numeric series starting with the integers 0 and 1.
#       In this series, the next integer is determined by summing the previous two.
#       This gives us:
#       0, 1, 1, 2, 3, 5, 8, 13, ...
#       We will write a function that computes this series – then generalize it.


def fibonacci(n):
    a,b = 0,1
    for i in range(n-1):
       a, b = b, a+b
    return a   

for i in range(1,10):
    print(fibonacci(i))


# Lucas Numbers :The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1.
#The resulting series looks like this: 2, 1, 3, 4, 7, 11, 18, 29, ...


def lucas(n):
    a,b = 0,1
    for i in range(n-1):
        if i == 0:
            a = 2
        elif i == 1:
            a = 1
        elif i > 1:
            a, b = b, a+b 
    return a

for i in range(2,10):
    print(lucas(i))
    

        
