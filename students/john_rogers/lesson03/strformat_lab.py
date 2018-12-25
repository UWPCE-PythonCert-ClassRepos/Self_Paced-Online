#!/usr/bin/env python3
"""
String formatting exercises.
Author: JohnR
Version: .7
Date: 12/14/2018
Notes: Tasks 1 - 5 complete.
"""


def main():
    """
    Establish some global variables and call each function.
    :return:
    """
    short_tuple = (1, 2)
    long_tuple = (1, 2, 3, 4, 5, 6)
    very_long_tuple = (0, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    five_tuple = (4, 30, 2017, 2, 27)
    t5_list = ['orange', 1.3, 'lemon', 1.1]
    names = ['Renton', 'Simon', 'Daniel', 'Francis', 'Tommy', 'Davie']
    ages = [21, 21, 23, 35, 28, 24]
    cost = [107.00, 20, 23.000, 4566.12304, 431.453, 2.0972345]

    print('Task 1 results using f strings: ', end='')
    t1_results = task_1()

    print('Task 2 results using format method: ', end='')
    task_2(t1_results)

    print('Task 3.0 results using tuple with two items: ', end='')
    task_3(short_tuple)

    print('Task 3.1 results using tuple with six items: ', end='')
    task_3(long_tuple)

    print('Task 3.2 results using tuple with ten items: ', end='')
    task_3(very_long_tuple)

    print('Task 4 results for date/time format: ', end='')
    task_4(five_tuple)

    print('Task 5.0 results, more f strings: ', end='')
    task_5(t5_list)

    print('Task 6.0 results, alignment: ')
    task_6(names, ages, cost)


def task_1():
    """
    Take tuple (2, 123.4567, 10000, 12345.67) and produce the below:
    'file_002 :   123.46, 1.00e+04, 1.23e+04'
    :return: Return the original tuple.
    """
    my_tuple = (2, 123.4567, 10000, 12345.67)
    file = my_tuple[0]
    float_2 = my_tuple[1]
    sci_not_2 = my_tuple[2]
    sci_not_3 = my_tuple[3]
    print(f'file_{file:>03}: {float_2:.{5}}, {sci_not_2:.2e},'
          f' {sci_not_3:.2e} ')

    return my_tuple


def task_2(some_tuple):
    """
    Use tuple from task_1 and display using an alternate format method.
    :return: None
    """
    file = some_tuple[0]
    float_2 = some_tuple[1]
    sci_not_2 = some_tuple[2]
    sci_not_3 = some_tuple[3]
    print('file_{:>03}: {:.5}, {:.2e}, {:.2e}'
          .format(file, float_2, sci_not_2, sci_not_3))


def task_3(unknown_tuple):
    """
    Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)" to take
    an arbitrary number of values.
    :return:
    """
    values = []
    for i in unknown_tuple:
        values.append(i)
    l = len(values)
    print(("The {} numbers are: " + ",".join(["{}"] * l)).format(l, *values))


def task_4(date_tuple):
    """
    Given a 5 element tuple (4, 30, 2017, 2, 27) use string formatting
    to print '02 27 2017 04 30'
    :return: None
    """
    d = date_tuple
    print('{:>02} {} {} {:>02} {}'.format(d[3], d[4], d[2], d[0], d[1]))


def task_5(t5_list):
    """
    Use f-strings; Given the 4 element list ['orange', 1.3, 'lemons', 1.1]
    write an f-string that will display 'The weight of an orange is 1.3
    and the weight of a lemon is 1.1.'
    Change the f-string so that is displays the names of the fruit in
    uppercase and weight  += 20%.
    :return: None
    """
    print(f'The weight of an {t5_list[0]} is {t5_list[1]} and the '
          f'weight of a {t5_list[2]} is {t5_list[3]}.')

    print('Task 5.1 extra credit: ', end='')
    print(f'The weight of an {t5_list[0].upper()} is {t5_list[1] * 1.2}'
          f' and the weight of a {t5_list[2].upper()} is {t5_list[3] * 1.2}.')


def task_6(row_1, row_2, row_3):
    """
    Print a table of several rows, each with a
    name, an age and a cost. Make sure some of the costs are in the hundreds
    and thousands to test your alignment specifiers.

    And for an extra task, given a tuple with 10 consecutive numbers,
    can you work how to quickly print the tuple in columns that are 5
    characters wide? It’s easily done on one short line!
    :return: none
    """
    print('Centered')
    for i in range(len(row_1)):
        print(f'{row_1[i]:^10} {row_2[i]:^10n} {row_3[i]:^10n}')

    print()
    print('Right justified')
    for i in range(len(row_1)):
        print(f'{row_1[i]:10} {row_2[i]:10n} {row_3[i]:10n}')

    # TODO: extra credit


if __name__ == '__main__':
    main()