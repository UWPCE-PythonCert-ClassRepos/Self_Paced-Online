

def fibonacci_series(n):  # n = the number of numbers to display in the series
    output = [0]  # following the logic of the process below, we already append() b, so that we can display the 0th value
    a = 1
    b = 0

    for i in range(n):
        output.append(a)
        b, a = a, a + b  # append() a; a = a+b; b = the old a
    return output[n]


def lucas_series(n):  # n = the number of numbers to display in the series
    output = [2]
    a = 1
    b = 2

    for i in range(0, n):
        output.append(a)
        b, a = a, a + b  # this follows the same logic, but begins with 2, 1 instead of 0, 1
    return output[n]


def sum_series(n, b=0, a=1):  # default values are identical to fibonacci_series() above, but b and a can be any two #s
    output = [b]

    for i in range(0, n):
        output.append(a)
        b, a = a, a + b
    return output[n]


print(fibonacci_series(5))  # should result in 5th (starting from zero) fibonacci number = 11
print(lucas_series(5))  # should result in 5th (starting from zero) lucas number = 5
print(sum_series(5, 0, 1))  # should result in 5th (starting from zero) fibonacci number = 5
print(sum_series(5, 2, 1))  # should result in 5th (starting from zero) lucas number = 11
print(sum_series(5, 0, -1))  # should result in 5th (starting from zero) *negative* fibonacci number = -5
