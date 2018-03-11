# Create a new module series.py in the lesson02 folder in your student folder.
# In it, add a function called fibonacci.
# The function should have one parameter, n.
# The function should return the nth value in the fibonacci series (starting with zero index)
# Ensure that your function has a well-formed docstring
# Note that the fibonacci series is naturally recursive – the value is defined by previous values:

# fib(n) = fib(n-2) + fib(n-1)


def sum_series(n, x=0, y=1):
    """Return the nth value in the Fibonacci or Lucas series based on parameter input"""
    if (x == 0) and (y == 1):
        # Return the nth value in the Fibonacci series
        fibi = [0, 1]
        if n == 0:
            print(0)
            return 0
        elif n == 1:
            print(1)
            return 1
        else:
            for i in range(n):
                # create Fibonacci series
                small_fib = fibi[i]
                range_plus1 = i + 1
                big_fib = fibi[range_plus1]
                next_fib = small_fib + big_fib
                fibi.append(next_fib)
            fib_nth = fibi[n-2] + fibi[n-1]
            print(fib_nth)
            return fib_nth
    elif (x == 2) and (y == 1):
        # Return the nth value in the Lucas series
        lucas_tuple = [2, 1]
        if n == 0:
            print(2)
            return 2
        elif n == 1:
            print(1)
            return 1
        else:
            for i in range(n):
                # create Lucas series
                small_luc = lucas_tuple[i]
                luc_plus1 = i + 1
                big_luc = lucas_tuple[luc_plus1]
                next_luc = small_luc + big_luc
                lucas_tuple.append(next_luc)
            lucas_nth = lucas_tuple[n - 2] + lucas_tuple[n - 1]
            print(lucas_nth)
            return lucas_nth
    else:
        print("Series not defined. Please enter Fibonacci or Lucas series parameters.")
        return


sum_series(5)
