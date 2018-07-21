def fibonacci(n):
    """add a doc string"""
    a=0
    b=1
    c=0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        return c




def lucas(n):
    """add a doc string"""
    a=2
    b=1
    c=0
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        return c



def sum_series(n, a=0, b=1):
    """add a doc string"""
    c=0
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        return c

#sum_series(8)


#add tests here

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(5) == 5

assert lucas(0) == 2
assert lucas(1) == 1
assert lucas(2) == 3
assert lucas(5) == 11

assert sum_series(0) == fibonacci(0)
assert sum_series(1) == fibonacci(1)
assert sum_series(2) == fibonacci(2)
assert sum_series(5) == fibonacci(5)

assert sum_series(0,2,1) == lucas(0)
assert sum_series(1,2,1) == lucas(1)
assert sum_series(2,2,1) == lucas(2)
assert sum_series(5,2,1) == lucas(5)