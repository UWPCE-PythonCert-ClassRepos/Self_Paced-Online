#!/usr/bin/env python3
"""
String formatting exercises.
Author: JohnR
Version: .2
Notes: Tasks 1 and 2 complete. 
"""


def main():
    """
    Core script logic.
    :return:
    """
    t1_results = task_1()
    task_2(t1_results)


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
    print('*' * 50)
    print('Task 1 results using f strings: ')
    print('Original: ', end='')
    print(my_tuple)
    print('Modified: ', end='')
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
    print('*' * 50)
    print('Task 2 results using older format method: ')
    print('Original: ', end='')
    print(some_tuple)
    print('Modified: ', end='')
    print('file_{:>03}: {:.5}, {:.2e}, {:.2e}'.format(file, float_2,
                                                      sci_not_2, sci_not_3))


def task_3():
    """
    Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)" to take
    an arbitrary number of values.
    :return:
    """
    pass


def task_4():
    """
    Given a 5 element tuple (4, 30, 2017, 2, 27) use string formatting
    to print '02 27 2017 04 40'
    :return: None
    """
    pass


def task_5():
    """
    Use f-strings; Given the 4 element list ['oranges', 1.3, 'lemons', 1.1]
    write an f-string that will display 'The of an orange is 1.3 and the
    weight of a lemon is 1.1'.
    Change the f-string so that is displays the names of the fruit in
    uppercase and weight 20% higher.
    :return: None
    """
    pass


def task_6():
    """
    tbd
    :return: tbd
    """
    pass


if __name__ == '__main__':
    main()