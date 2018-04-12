#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  10-Feb-2018
# ------------------------------------------- #

# Define functions


def format_presentation(a_string):
    ''' this function prints stuff for readability '''

    print('\nTask {} returns the formatted string below.'. format(a_string))


def task_one():
    ''' this function will format a 4 element
        tuple and produce
        'file_002 :   123.46, 1.00e+04, 1.23e+04' '''

    a_tup = (2, 123.4567, 10000, 12345.67)

    file, floating, exp_one, exp_two = a_tup

    formatted_string = 'file_{0:03d}: {1:.2f}, {2:.2e}, {3:.2e}'.format(file, floating, exp_one, exp_two)

    return formatted_string


def task_two():
    ''' this function will format a 4 element
        tuple and produce
        'file_002 :   123.46, 1.00e+04, 1.23e+04' '''

    a_tup = (2, 123.4567, 10000, 12345.67)

    file, floating, exp_one, exp_two = a_tup

    template = 'file_{file:03d}: {floating:.2f}, {exp_one:.2e}, {exp_two:.2e}'

    return template.format(file=2, floating=123.4567, exp_one=10000, exp_two=12345.67)


def task_three(a_tuple):
    ''' this function dynamically builds up format
        string '''

    tuple_length = len(a_tuple)
    template = '{:d}, ' * (tuple_length - 1) + '{:d}'
    return 'The {} numbers are: '.format(tuple_length) + template.format(*a_tuple)


def task_four():
    ''' this function will format the tuple
        below to print 02 27 2017 04 30 '''

    a_tup = (4, 30, 2017, 2, 27)
    template = '{0:02d} {1:d} {2:d} {3:02d} {4:d}'
    return template.format(a_tup[3], a_tup[4], a_tup[2], a_tup[0], a_tup[1])


def task_five():
    ''' this function will utilize f-string '''

    a_list = ['oranges', 1.3, 'lemons', 1.1]

    print(f'The weight of an organge is {a_list[1]} and the weight of a lemon is {a_list[3]}')

    print(f'{a_list[0].upper()} weigh {a_list[1] * 1.2} and {a_list[2].upper()} weigh {a_list[3] * 1.2}')


def task_six():
    ''' this function prints a table of several rows
        with each name, age, and a cost '''

    table = [
        ('Makiko', 33, '$1234.23'),
        ('Yumika', 5, '$12.00'),
        ('Kohana', 1, '$890023.01'),
        ('Tri', 34, '$9999999.01')
        ]

    for idx, item in enumerate(table):
        print('{:<10} {:<5} {:<10}'.format(table[idx][0], table[idx][1], table[idx][2]))


# End of function definition

# Presentation

# Task one:
format_presentation('one')
print(task_one())

# Task two:
format_presentation('two')
print(task_two())

# Task three
test_tuple = (23, 3, 4, 9 , 0)
format_presentation('three')
print(task_three(test_tuple))

# Task four
format_presentation('four')
print(task_four())

# Task five
format_presentation('five')
task_five()

# Task six
format_presentation('six')
task_six()

# Task six extra
format_presentation('six extra')
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:^5}' * len(t)).format(*t))
