def fibonacci(n):
    x=[0, 1]
    for i in range(n):
        if i > 1:
            x = x + [x[i-2] + x[i-1]]
    print (x)
    print(x[i])

def lucas(n):
    x=[2, 1]
    for i in range(n):
        if i > 1:
            x = x + [x[i-2] + x[i-1]]
    print (x)
    print(x[i])

def sum_series(n,first=0,second=1):
    x=[first, second]
    for i in range(n):
        if i > 1:
            x = x + [x[i-2] + x[i-1]]
    print (x)
    print(x[i])