#!/usr/bin/env python3

def fibonacci(n, initials):
    """ find fibonacci series for in order of n """
    fib=list(initials)
    total=0
    for a in range(2, n+1):
        fib.append(fib[a-2] + fib[a-1])
    for i in fib:
        total+=i
    return i

#fibonacci(8)

initials=(0, 1)
lucas=(2, 1)

assert fibonacci(7, initials)==fibonacci(6, initials)+fibonacci(5, initials)
assert fibonacci(7, lucas) == fibonacci(
    6, lucas) + fibonacci(5, lucas)
