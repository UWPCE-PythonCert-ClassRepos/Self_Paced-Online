# Given two int values, return their sum. Unless
# the two values are the same, then return double
# their sum.

def sum_double(a, b):

    if(a==b):
        sum_result = 2*(a+b)
    else:
        sum_result = a+b

    return sum_result