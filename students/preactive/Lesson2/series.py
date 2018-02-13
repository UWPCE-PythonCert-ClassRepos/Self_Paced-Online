def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
#print(fib(8))

def lucas(n):
    a,b = -1,2
    for i in range(n):
        a, b = b, a+b
    return print(a)
#lucas(5)

def sum_series(n, a=0, b=1):
    if a == 0:
        if n == 1:
            return 0
        if n == 2:
            return 1
    return sum_series(n - 1) + sum_series(n - 2)
print(sum_series(7))
