def fibonacci(n):
    x=[0, 1]
    for i in range(n):
        if i > 1:
            x = x + [x[i-2] + x[i-1]]
    print (x)
    print(x[i])
    return x[i]

def lucas(n):
    x=[2, 1]
    for i in range(n):
        if i > 1:
            x = x + [x[i-2] + x[i-1]]
    print (x)
    print(x[i])
    return x[i]

def sum_series(n,first=0,second=1):
    x=[first, second]
    for i in range(n):
        if i > 1:
            x = x + [x[i-2] + x[i-1]]
    print (x)
    print(x[i])
    return x[i]

#test to see 10th number in lucas series is equal to 77
assert lucas(10) == 76

#test to see 10th number in fib series is equal to 77
assert fibonacci(10) == 34

#test to see 10th number in fib series is equal to 10th in sum_series
assert fibonacci(10) == sum_series(10)