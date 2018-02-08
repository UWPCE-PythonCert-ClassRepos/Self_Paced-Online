"""
The Fibonacci Series is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This gives us:
0, 1, 1, 2, 3, 5, 8, 13, ...
"""


#should be recursive
def fibonacci(n):
    """return the nth value in the fibonacci series fib(n) = fib(n-2) + fib(n-1)"""
    if n > 2: 
        return fibonacci(n-2) + fibonacci(n-1)   
    elif n > 1:
        return fibonacci(n-1)
    else:
        return n

if __name__ == '__main__': 
    for i in range(10):
         print('the ' + str(i) + ' value of fibonnaci series is: ' + str(fibonacci(i)))
