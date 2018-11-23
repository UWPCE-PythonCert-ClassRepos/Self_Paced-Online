def fibonacci(n):
    if n == 0:  # initializes the series
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)  # function recursion to calculate values beyond the first two


def lucas(n):
    if n == 0:  # initializes the series
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)  # function recursion to calculate values beyond the first two


def sum_series(n, a=0, b=1):  # establishes default values for optional parameters
    if n == 0:  # initializes the series
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n-2, a, b) + sum_series(n-1, a, b)  # a and b included so default values aren't used


print("Fibonacci test")
print(fibonacci(0))  # this and the following test make sure that the if and elif statements work right
print(fibonacci(1))
print(fibonacci(6))  # verifies that the recursion part of the function works correctly

print("Lucas test")
print(lucas(0))  # this and the following test make sure that the if and elif statements work right
print(lucas(1))
print(lucas(5))  # verifies that the recursion part of the function works right

print("Sum series test")
print(sum_series(0))  # this and the following test make sure that the function works with only the required parameter
print(sum_series(5))
print(sum_series(0, 2, 1))  # these tests check that the test works for various optional paramenters
print(sum_series(5, 2, 1))
print(sum_series(5, 1, 1))
