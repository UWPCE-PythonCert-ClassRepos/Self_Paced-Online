# Brandon Henson
# 4/2/18
# Lesson 2 series.py
# using index and math to make functions and assertions

'''This function prints out the digit based on parameter.'''


def fibonacci(n):
    fibo_list = [0, 1]
    for i in range(2, n+1):
        x = fibo_list[i-2] + fibo_list[i-1]
        fibo_list.append(x)
# printed to test if I'm getting the index number
# print(fibo_list[n])
    return fibo_list[n]


def lucas(n):
    """This function prints out the 'lucas' digit in the parameter."""
    luc_list = [2, 1]
    for i in range(2, n+1):
        x = luc_list[i-2] + luc_list[i-1]
        luc_list.append(x)
# printed to test if I'm getting the index number
# print(luc_list[n])
    return luc_list[n]


def sum_series(n, a=0, b=1):
    sum_list = [a, b]
    for i in range(2, n+1):
        x = sum_list[i-2] + sum_list[i-1]
        sum_list.append(x)
# print (sum_list[n])
    return sum_list[n]

# a few assert statements to test the fibonacci function
assert fibonacci(12) == 144
assert fibonacci(11) == 89
assert fibonacci(10) == 55
# a few assert statements to test the lucas function
assert lucas(12) == 322
assert lucas(11) == 199
assert lucas(10) == 123
# a few assert statements to test the sum_series function
assert sum_series(12, 4, 5) == 1076
assert sum_series(11, 3, 5) == 610
