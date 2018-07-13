"""
Return the fibonacci or lucas series of n length.

functions:
fibonacci(n) - Return the fibonacci series of n length.
lucas(n) - Return the lucas series of n length.
sum_series(n, x, y) - Generlization used by fibonaci(n) and lucas(n).
"""

def fibonacci(n):
    """Return the fibonacci series of n length starting with [0,1]."""
    sum_series(n, 0, 1)

def lucas(n):
    """Return the lucas series of n length starting with [2,1]."""
    sum_series(n, 2, 1)

def sum_series(n, x = 0, y = 1):
    """Return the fibonacci (default) or lucas series of n length.

    Generlization used by fibonaci(n) and lucas(n).

Parameters
----------
n : int
    Defines the length of the fibonacci or lucas series.
x : int, optional (default = 0)
    Is the int at the 0 index of the fibonacci or lucas series.
y : int, optional (default = 1)
    Is the int at the 1 index of the fibonacci or lucas series.
    """
    lst = []
    # Append the list at the i index
    for i in range(n):
        if(i == 0):
            lst.append(x)
        elif(i == 1):
            lst.append(y)
        elif(i > 1):
            lst.append((lst[i-2]+lst[i-1]))
    print(lst)