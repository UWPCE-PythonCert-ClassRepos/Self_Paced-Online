# -------------------------------------#
# Desc: Fibonacci Series Module
# Dev: Will White
# Date: 4/1/2018
# ChangeLog: (When,Who,What)
# -------------------------------------#


def fibonacci(n):
    """
    Returns the nth value in the fibonacci series (starting with zero index). The user passes an index position. The
    value of the first two index positions are set to 0 and 1 respectively. All other index positions use a recursive
    formula to calculate the positions value.

    :param n: The index position the program calculates
    :return: The program returns the value of the inputted index position
    """

    if n == 0:  # The value at the first index is set to return '0'
        return 0
    elif n == 1:  # The value at the second index is set to return '1'
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Recursive formula to calculate the value when the index > '1'


def lucas(n):
    """
    Returns the nth value in the lucas series (starting with zero index). The user passes an index position. The
    value of the first two index positions are set to 2 and 1 respectively. All other index positions use a recursive
    formula to calculate the positions value.

    :param n: The index position the program calculates
    :return: The program returns the value of the inputted index position
    """

    if n == 0:  # The value at the first index is set to return '2'
        return 2
    elif n == 1:  # The value at the second index is set to return '1'
        return 1
    else:
        return lucas(n-1) + lucas(n-2)  # Recursive formula to calculate the value when the index > '1'


def sum_series(n, opt_var_1=0, opt_var_2=1):
    """
    Returns the nth value in the fibonacci series (starting with zero index). The user passes an index position. The
    first two index positions are both optional variables which the user can pass as arguments through the function. If
    nothing is passed, these variables are set to 0 and 1 respectively  All other index positions use a recursive
    formula to calculate the positions value.

    :param n: The index position the program calculates
    :param opt_var_1: An optional variable to set the value of the first index position
    :param opt_var_2: An optional variable to set the value of the second index position
    :return: The program returns the value of the inputted index position
    """

    if n == 0:
        return opt_var_1
    elif n == 1:
        return opt_var_2
    else:
        return sum_series(n - 1, opt_var_1, opt_var_2) + sum_series(n - 2, opt_var_1, opt_var_2)


# Assert Statements to test functions
m = 4  # The index position we'll pass to the functions

# Prints the value of the 5th index position for each series without passing any optional parameters. The values of the
# first two index positions in sum_series are set to 0 & 1 respectively
# sum_series == fibonacci
print(fibonacci(m))
print(lucas(m))
print(sum_series(m))
print()

# Prints the value of the 5th index position for each series. The values of the first two index positions in sum_series
# are passed as arguments and set to 2 & 1 respectively
# sum_series == lucas
print(fibonacci(m))
print(lucas(m))
print(sum_series(m, 2, 1))
print()

# Prints the value of the 5th index position for each series. The values of the first two index positions in sum_series
# are passed as arguments and set to 5 & 6 respectively
# sum_series != lucas or fibonacci
print(fibonacci(m))
print(lucas(m))
print(sum_series(m, 5, 6))