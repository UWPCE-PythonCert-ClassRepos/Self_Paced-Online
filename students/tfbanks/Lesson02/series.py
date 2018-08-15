# Fibonacci Series Exercise by tfbanks
# NOTE: Fib (Fibonacci series) and Luc (Lucas Series) were defined outside the sum_series function
# This way they can be run separately; they can also be called in the sum_series function when criteria is met


def fib(n):  # Defines the nth value in the Fibonacci Series starting with integers 0 and 1

    if n < 0:
        return "Please insert a number greater than 0"  # Tells to only insert values greater than Zero
    elif n == 0:
        return 0  # Sets the first starting integer to 0
    elif n == 1:
        return 1  # sets the second starting integer to 1
    else:
        return fib(n-1) + fib(n-2)  # Returns the value at the nth position


def luc(n):  # Defines the nth position in the Lucas Series starting with integers 2 and 1

    if n < 0:
        return "Please insert a number greater than 0"  # Tells to only insert values greater than Zero
    elif n == 0:
        return 2  # Sets the first starting integer to 2
    elif n == 1:
        return 1  # sets the second starting integer to 1
    else:
        return luc(n-1) + luc(n-2)  # Returns the value at the nth position


def sum_series(n, f=None, s=None):  # Defines a series to run either Fibonacci, Lucas, or Other Series
        # n = number - the nth position in the series
        # f = first optional value - sets the first starting integer to f
        # s = second optional value - sets the second starting integer to s

    f = f or 0  # sets the first starting integer to 0 if no value is input
    s = s or 1  # sets the second starting integer to 1 if no value is input

    def other(n):  # Defines the nth position in the Other Series
        if n == 0:
            return f  # sets the first integer to f
        elif n == 1:
            return s  # sets the second integer to s
        else:
            return other(n-1) + other(n-2)  # Returns the value at the nth position

    if n < 0:
        return "Please insert a number greater than 0"  # Tells to only insert values greater than Zero
    elif f == 2 and s == 1:
        return luc(n)  # Calls Lucas Series Function when f = 2 and s = 1
    elif f == 0 and s == 1:
        return fib(n)  # Calls the Fibonacci Function when f = 0 and s = 1 (either by input or default)
    else:
        return other(n)  # Calls the Other Series Function when f is not 0 or 2 and s is not 1


# Assertion tests
# Fibonacci Series
assert fib(7) == 13
assert(fib(12) == 144)
assert(fib(22) == 17711)
print("All Fibonacci Assert Tests Passed")

# Lucas Series
assert(luc(4) == 7)
assert(luc(10) == 123)
assert(luc(15) == 1364)
print("All Lucas Assert Tests Passed")

# sum_series
assert sum_series(8, 0, 1) == 21
assert sum_series(6, 2, 1) == 18
assert sum_series(3, 5, 4) == 13
assert sum_series(11) == 89
print("All sum_series Assert Tests Passed")

