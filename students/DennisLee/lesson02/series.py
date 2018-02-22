def fibonacci(n: int) -> int:
    """
    Print a list of fibonacci numbers up to a certain series count.

    :n:  The desired index number of the fibonacci series
         (starting with position 0).

    :return:  The value of the fibonacci series at the specified index,
              where a fibonacci number is always equal to the sum of the
              previous two numbers in the fibonacci series, and the
              1st two fibonacci numbers have values of **0** and **1**.
    """

    x: int = 0
    y: int = 1
    if n < 0:
        return -1  # error code - indexes can't be negative
    elif n == 0:
        return x
    elif n == 1:
        return y
    else:
        for i in range(n - 1):
            x, y = y, x + y
        return y

def lucas(n: int) -> int:
    """
    Print a list of lucas numbers up to a certain series count.

    :n:  The desired index number of the lucas series
         (starting with position 0).

    :return:  The value of the lucas series at the specified index,
              where a lucas number is always equal to the sum of the
              previous two numbers in the lucas series, and the
              1st two lucas numbers have values of **2** and **1**.
    """

    x: int = 2
    y: int = 1
    if n < 0:
        return -1  # error code - indexes can't be negative
    elif n == 0:
        return x
    elif n == 1:
        return y
    else:
        for i in range(n - 1):
            x, y = y, x + y
        return y

def sum_series(index_num: int,
               index_0_value: int = 0,
               index_1_value: int = 1) -> int:
    """
    Retrieve a particular number within a series that contains the sum
    of the series's previous two values.

    :index_num:  The position number to retrieve (zero-based index).

    :index_0_value:  The value of the first value within the series.
                     Default is the fibonacci series's first value (0).

    :index_1_value:  The value of the second value within the series.
                     Default is the fibonacci series's second value (0).

    :return: The value of the specified index number within the series.
    """

    if index_num < 0:
        return -1  # error code - indexes can't be negative
    elif index_num == 0:
        return index_0_value
    elif index_num == 1:
        return index_1_value
    else:
        x, y = index_0_value, index_1_value
        for i in range(index_num - 1):
            x, y = y, x + y
        return y    

if __name__ == '__main__':
    print('The first 50 fibonacci numbers:')
    for a in range(50):
        print(fibonacci(a))

    print('\nThe first 50 lucas numbers:')
    for a in range(50):
        print(lucas(a))

    print('\nThe first 50 numbers of the sum_series function [#0==1,#1==2]:')
    for a in range(50):
        print(sum_series(a, 1, 2))

    print('\nThe first 50 numbers of the sum_series function [defaults/fibonacci]:')
    for a in range(50):
        print(sum_series(a))

    print('\nThe first 50 numbers of the sum_series function [series=lucas]:')
    for a in range(50):
        print(sum_series(a, 2))
