
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
        x4 = list[x2] + list[x3]

        # add the next number of the fibonacci series to the list
        list.append(x4)

        #iterate the count variable
        count += 1

    # return the nth fibonacci integer
    return print(fibonacci_list[-2])

fibonacci(5)



"""def lucas(n):
    return n



def sum_series(n):
    return n"""