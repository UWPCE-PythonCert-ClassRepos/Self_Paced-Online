import random
import timeit

def fibonacci_recursive(n):
    """
    Recursively compute the nth Fibonacci number (where n>1).
    The 0th fibonacci number is 0
    The 1st fibonacci number is 1
    The nth fibonacci number is the (n-2)th - (n-1)th fibonacci number.
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci_recursive(n-2)+fibonacci_recursive(n-1)

def fibonacci(n):
    """
    Compute the nth fibonacci number with a loop (where n>1).
    The 0th fibonacci number is 0
    The 1st fibonacci number is 1
    The nth fibonacci number is the (n-2)th - (n-1)th fibonacci number
    """
    fibo = [0,1]
    lastFibo = 0
    if n > 1:
        for x in range(n-1):
            lastFibo = fibo[1]
            fibo[1] = fibo[0]+fibo[1]
            fibo[0] = lastFibo
    else:
        return fibo[n]
    return fibo[1]

def lucas(n):
    """
    Compute the nth lucas number with a loop (where n>1).
    The 0th Lucas number is 2
    The 1st lucas number is 1
    The nth lucas number is the (n-2)th - (n-1)th lucas number
    """
    luca = [2,1]
    lastLuca = 0
    if n > 1:
        for x in range(n-1):
            lastLuca = luca[1]
            luca[1] = luca[0]+luca[1]
            luca[0] = lastLuca
    else:
        return luca[n]
    return luca[1]


n = 35
start = timeit.default_timer()
print('The first '+str(n)+' fibonacci numbers (starting at 0): recursively')
for x in range(n):
    print(fibonacci_recursive(x), end=', ')
print(fibonacci_recursive(n))
print(timeit.default_timer()-start)

start = timeit.default_timer()
print('The first '+str(n)+' fibonacci numbers (starting at 0): w/ a loop')
for x in range(n):
    print(fibonacci(x), end=', ')
print(fibonacci(n))
print(timeit.default_timer()-start)
