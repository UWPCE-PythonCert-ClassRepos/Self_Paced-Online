#-------------------------------------------------#
# Title: Fibonacci
# Dev:   LDenney
# Date:  October 4, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/4/18, Created File
#-------------------------------------------------#

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n - 1)

def lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-2) + lucas(n - 1)

def sum_series(n, op1 = 0, op2 = 1):
    if n == 1:
        return op1
    elif n == 2:
        return op2
    else:
        return sum_series(n - 2, op1, op2) + sum_series(n - 1, op1, op2)

#testing block
#tests that fibonacci() shows correct 8th value in fibonacci sequence
assert fibonacci(8) == 13, "Error with fibonacci!"
#tests that lucas() shows correct 8th value in lucas sequence
assert lucas(8) == 29, "Error with lucas!"
#tests that sum_series() shows correct 8th value with fibonacci defaults
assert sum_series(8)== 13, "Error with the generalization to fibonacci!"
#tests that sum_series() shows correct 8th value with fibonacci defaults
assert sum_series(8,2,1)== 29, "Error with the generalization to lucas"