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
    return sum_series(n)

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
    return sum_series(n, 2)

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
    # check correct fibonacci function values for index pos 5, 7, and 8
    assert fibonacci(5) == 5
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21

    print('The first 50 fibonacci numbers:')
    for a in range(50):
        print(fibonacci(a))

    # check correct lucas function values for index pos 5, 7, and 8
    assert lucas(5) == 11
    assert lucas(7) == 29
    assert lucas(8) == 47

    print('\nThe first 50 lucas numbers:')
    for a in range(50):
        print(lucas(a))

    # check correct sum_series function values for index pos 5, 7, and 8
    # for a series with seed values 4 and 9
    assert sum_series(5, 4, 9) == 57
    assert sum_series(7, 4, 9) == 149
    assert sum_series(8, 4, 9) == 241

    print('\nThe first 50 numbers of the sum_series function [#0=>4,#1=>9]:')
    for a in range(50):
        print(sum_series(a, 4, 9))
