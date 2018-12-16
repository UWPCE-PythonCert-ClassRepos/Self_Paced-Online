def fibonacci(n):
    """Return requested number from Fibonacci series by calling sum_series
        with appropriate parameters"""
    return sum_series(n)


def lucas(n):
    """Return requested number from Lucas series"""
    return sum_series(n, 2, 1)

def sum_series(n, x=0, y=1):
    if n == 1:
        return x
    elif n == 2:
        return y
    else:
        return sum_series(n-2, x, y) + sum_series(n-1, x, y)

#Check 7th number in Fibonacci series
assert fibonacci(7) == 8

#Check 7th number in Lucas series
assert lucas(7) == 18

#Check 1st number in Fib
assert fibonacci(1) == 0

#Check 2nd number in Luc
assert lucas(2) == 1

#Optional input section for finding numbers in the series
'''series = input("Enter F for Fibonacci and L for Lucas: ").upper()
num = int(input("Enter number greater than 1 for series: "))

if series == 'F':
    print(fibonacci(num))
else:
    print(lucas(num))'''