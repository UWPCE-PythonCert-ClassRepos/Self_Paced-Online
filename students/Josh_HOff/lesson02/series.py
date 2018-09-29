def fibonacci(n):
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