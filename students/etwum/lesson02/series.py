
def fibonacci(n):
    # fib(n) = fib(n-2) + fib(n-1)
    # 0, 1, 1, 2, 3, 5, 8, 13
    # starting two numbers of the fibonacci series
    x = 0
    y = 1

    #add numbers to a list
    list = [x,y]

    # variable used to keep count of the nth value
    count = 1

    while count < n:

        x2 = len(list) -2
        x3 = len(list) - 1

        x4 = list[x2] + list[x3]
        list.append(x4)

        count += 1

    return print(list[-2])

fibonacci(5)



"""def lucas(n):
    return n



def sum_series(n):
    return n"""