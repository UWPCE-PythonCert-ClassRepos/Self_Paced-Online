
def fibonacci(n):
    # this function finds the nth integer in the fibonacci series
    # fibonacci series ....0, 1, 1, 2, 3, 5, 8, 13
    # the next integer is determined by summing the previous two

    # starting two numbers of the fibonacci series (0 and 1)
    x = 0
    y = 1

    # adds the starting two numbers to a list
    fibonacci_list = [x,y]

    # variable used to keep count of the nth value
    count = 1

    while count < n:
        # loops while the variable count is less than the parameter n

        # find the length of the list and substracts 1 and 2
        # in order to find the previous two numbers in the fibonacci series

        x2 = len(fibonacci_list) -2
        x3 = len(fibonacci_list) - 1
        x4 = fibonacci_list[x2] + fibonacci_list[x3]

        # add the next number of the fibonacci series to the list
        fibonacci_list.append(x4)

        #iterate the count variable
        count += 1

    # return the nth fibonacci integer
    return print(fibonacci_list[-2])




def lucas(n):
    # this function finds the nth integer in the lucas series
    # lucas series ....2, 1, 3, 4, 7, 11, 18, 29
    # the next integer is determined by summing the previous two

    # starting two numbers of the lucas series (0 and 1)
    x = 2
    y = 1

    # adds the starting two numbers to a list
    lucas_list = [x,y]

    # variable used to keep count of the nth value
    count = 1

    while count < n:
        # loops while the variable count is less than the parameter n

        # find the length of the list and substracts 1 and 2
        # in order to find the previous two numbers in the lucas series

        x2 = len(lucas_list) -2
        x3 = len(lucas_list) - 1
        x4 = lucas_list[x2] + lucas_list[x3]

        # add the next number of the lucas series to the list
        lucas_list.append(x4)

        # iterate the count variable
        count += 1

    # return the nth lucas integer
    return print(lucas_list[-2])




def sum_series(n ,y = 0, z = 1):
    # this function finds the nth integer in any series based on the input parameters
    # the next integer is determined by summing the previous two

    # adds the starting two numbers to a list
    series_list = [y,z]

    # variable used to keep count of the nth value
    count = 1

    while count < n:
        # loops while the variable count is less than the parameter n

        # find the length of the list and substracts 1 and 2
        # in order to find the previous two numbers in the series

        x2 = len(series_list) -2
        x3 = len(series_list) - 1
        x4 = series_list[x2] + series_list[x3]

        # add the next number of the series to the list
        series_list.append(x4)

        # iterate the count variable
        count += 1

    # return the nth integer
    return print(series_list[-2])


while True:
    #Test functions
    x = int(input("input a number"))
    y = int(input("input a number"))
    z = int(input("input a number"))

    # test to make sure the value of x is greater than zero
    assert x > 0

    # test to make sure the values of y + z are greater than zero for the sum_series function
    assert y + z > 0

    fibonacci(x)
    lucas(x)
    sum_series(x,y,z)

    break








