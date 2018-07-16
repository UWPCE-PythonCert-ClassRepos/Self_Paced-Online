# Fibonacci Series Exercise by tfbanks
# NOTE: Fib (Fibonacci series) and Luc (Lucas Series) were defined outside the sum_series function
# This way they can be run separately; they can also be called in the sum_series function when criteria is met


def fib(n):  # Defines the nth value in the Fibonacci Series starting with integers 0 and 1
    if n == 0:
        return 0  # Sets the first starting integer to 0
    elif n == 1:
        return 1  # sets the second starting integer to 1
    else:
        return fib(n-1) + fib(n-2)  # Returns the value at the nth position


def luc(n):  # Defines the nth position in the Lucas Series starting with integers 2 and 1
    if n == 0:
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
        print("Please insert a number greater than 0")  # Tells to only insert values greater than Zero
    elif f == 2 and s == 1:
        print(luc(n))  # Calls Lucas Series Function when f = 2 and s = 1
    elif f == 0 and s == 1:
        print(fib(n))  # Calls the Fibonacci Function when f = 0 and s = 1 (either by input or default)
    else:
        print(other(n))  # Calls the Other Series Function when f is not 0 or 2 and s is not 1

# Test fib function
# print(fib(7))

# Test luc function
# print(luc(4))

# Values to test correct functioning of the sum_series function
# sum_series(-5, 0, 1)
# sum_series(5, 0, 1)
# sum_series(5, 2, 1)
# sum_series(8)
# sum_series(5, 1, 2)

# Assertion tests
# assert(fib(10) == 100), "Fibonacci Assert Test 1 Failed"
# assert(fib(8) == 22), "Fibonacci Assert Test 2 Failed"
# assert(fib(5) == 11), "Fibonacci Assert Test 3 Failed"

# assert (luc(2) == 2),  "Lucas Assert Test 1 Failed"
# assert (luc(5) == 23),  "Lucas Assert Test 2 Failed"
# assert (luc(7) == 45),  "Lucas Assert Test 3 Failed"

# assert(sum_series(4, 3, 2)) == 23, "Sum_Series Assert Test 1 Failed"
# assert(sum_series(2, 2, 2)) == 8, "Sum_Series Assert Test 2 Failed"
# assert(sum_series(3, 5, 4)) == 23, "Sum_Series Assert Test 3 Failed"
