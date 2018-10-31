def fibonacci(n):
#    return sum_series(n)
    if (n == 0) or (n == 1):
        return 0
    num0 = 0
    num1 = 1
    for x in range(1, n - 1):
        if (x % 2 == 0):
            num0 = num0 + num1
        else:
            num1 = num0 + num1
    return num1 + num0
def lucas(n):
#    return sum_series(n, 2, 1)
    if (n == 0):
        return 0
    if (n == 1):
        return 2
    if (n == 2):
        return 1
    num0 = 2
    num1 = 1
    for x in range(2, n - 1):
        if (x % 2 == 0):
            num0 = num0 + num1
        else:
            num1 = num0 + num1
    return num1 + num0
def sum_series(n, num0 = 0, num1 = 1):
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return num0
    for x in range(2, n - 1):
        if (x % 2 == 0):
            num0 = num0 + num1
        else:
            num1 = num0 + num1
    return num1 + num0
    
#testing fibonacci series here. This gives us 0, 1, 1, 2, 3, 5, 8, 13, ...
assert fibonacci(6) == 5
assert fibonacci(8) == 13
assert fibonacci(4) == 2
#testing lucas numbers here. This gives us 2, 1, 3, 4, 7, 11, 18, 29, ...
assert lucas(5) == 7
assert lucas(7) == 18
assert lucas(3) == 3
#testing both fibonacci series and lucas numbers in this function.
assert sum_series(7) == 8 #fibonacci series
assert sum_series(5) == 3 #fibonacci series
assert sum_series(4, 2, 1) == 4 # lucas numbers
assert sum_series(8, 2, 1) == 29 #lucas numbers