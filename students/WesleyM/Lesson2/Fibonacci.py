def fibonacci(n):
    """This function prints out the nth digit in the Fibonacci series."""
    fib1 = 0
    fib2 = 1
    i = 2
    
    if n == 0:
        print(fib1)
    elif n == 1:
        print(fib2)
    else:
        while(i < n+1):
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
            i = i + 1
        print(fib3)


def lucas(n):
    """This function prints out the nth digit in the Lucas series."""
    luc1 = 2
    luc2 = 1
    i = 2
    
    if n == 0:
        print(luc1)
    elif n == 1:
        print(luc2)
    else:
        while(i < n+1):
            luc3 = luc1 + luc2
            luc1 = luc2
            luc2 = luc3
            i = i + 1
        print(luc3)

def sum_series(n, num1 = 0, num2 = 1):
    """This function prints out the nth digit in the Fibonacci series by default or the nth digit in a series with two optional numbers."""
    i = 2
    
    if n == 0:
        print(num1)
    elif n == 1:
        print(num2)
    else:
        while(i < n+1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            i = i + 1
        print(num3)

if __name__ != "__main__":
# Test fibonacci(n) is returning the expected value
    assert fibonacci(1) == 1
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55

# Test lucas(n) is returning the expected value
    assert lucas(1) == 4
    assert lucas(6) == 18
    assert lucas(10) == 123

# Test sum_series is returning the expected value
    assert sum_series(6) == 8
    assert sum_series(10,2,1) == 123
