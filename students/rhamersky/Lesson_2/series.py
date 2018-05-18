# Description: This program returns the value from the fibonacci and lucus series.
# Developer: Ryan Hamersky
# Date: 05/01/2018
# Rev: A - 05/15/2018 add comment to the code.

# -----Presentation Section-----

def fibonacci(n):
    '''
    Returns a number from the fibonacci series.
    :param n: Number input
    :return:
    '''
    number1 = 0
    number2 = 1
    counter = 0

    while True:
        newnumber = number1 + number2
        if n is counter:
            print(number1)
            break
        else:
            number1 = number2
            number2 = newnumber
            counter = counter + 1
            continue
    return

fibonacci(6)  # --> Testing fibonacci()

def lucus(n):
    '''
    Returns a number from the fibonacci series.
    :param n: Number input
    :return:
    '''
    number1 = 2
    number2 = 1
    counter = 0

    while True:
        newnumber = number1 + number2
        if n is counter:
            print(number1)
            break
        else:
            number1 = number2
            number2 = newnumber
            counter = counter + 1
            continue
    return

lucus(7)  # --> Testing lucus()

def sum_series(n,number1 = 0,number2 = 1):
    '''
    Returns a number from the fibonacci or lucus series depending on the parameter inputs number1
    and number 2.
    :param n: Number inout from the user.
    :return:
    '''
    counter = 0
    while True:
        newnumber = number1 + number2
        if n - 1 is counter:
            print(number1)
            break
        else:
            number1 = number2
            number2 = newnumber
            counter = counter + 1
            continue
    return

number = int(input("Please, enter a number greater than 0. Type 0 to exit. "))
while number > 0:
    sum_series(number,2,1)
    number = int(input("Please, enter a number greater than 0. Type 0 to exit. "))
    continue

def fibonacci_new(n):
    '''
    Returns a number from the fibonacci series.
    :param n: Number input from the user.
    :return:
    '''
    sum_series(n)
    return

fibonacci_new(6)  # --> Testing fibonacci_new()

def lucus_new(n):
    '''
    Returns a number from the lucus series.
    :param n: Number input from the user.
    :return:
    '''
    sum_series(n,2,1)
    return

lucus_new(7)  # --> Testing lucus_new()