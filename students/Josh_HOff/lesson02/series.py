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