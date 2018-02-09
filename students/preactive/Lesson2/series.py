def fib(n):
    a,b = 1,0
    for i in range(n-1):
        a,b = b, a+b
        print(a)
    return
#fib(5)

def lucas(n):
    a,b = -1,2
    for i in range(n-1):
        a,b = b, a+b
        print(a)
    return
#lucas(10)

def sum_series(a,b="",c=""):
    
