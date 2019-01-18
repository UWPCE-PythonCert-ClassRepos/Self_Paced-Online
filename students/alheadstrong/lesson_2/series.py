'''Author: Alex Filson
Updated: 1.18.19
Fibonacci Exercise for Lesson 2
Py210, Online Self-Paced
'''

def fibonacci(n):
    '''recursive function that returns nth number in fibonacci sequence'''
    if n == 0 or n == 1:
        return(n)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

def lucas(n):
    '''recursive function that returns nth number in fibonacci sequence'''
    if n == 0:
        return(2)
    if n == 1:
        return(1)
    else:
        return(lucas(n-1)+lucas(n-2))

for i in range(20):
    print(fibonacci(i))
for i in range(20):
    print(lucas(i))
