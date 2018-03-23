#!/usr/bin/env python3
# Lesson_3 Activity 3 String Formatting Exercise


def task_one(filedata):
    """Take tuple argument with 4 elements and return formated string"""
    formatted = "file_{:0>3}: {:=.2f}, {:.2e}, {:.2e}".format(*filedata)
    return formatted


def task_two(filedata):
    """Take tuple argument with 4 elements and return formated string"""
    return "file_%03d: %.2f, %.2e, %.2e" %\
           (filedata[0], filedata[1], filedata[2], filedata[3])


def task_three(listnum):
    """Take in a list of integers and return them in a formated string"""
    # list is only 1 item long
    if type(listnum) is int:
        return "The number is {}".format(listnum)
    else:
        list_form = ('{:d}, ' * (len(listnum) - 1)) + '{:d}'
        list_str = list_form.format(*listnum)
        return "the {} numbers are: {}".format(len(listnum), list_str)


def task_four(cinco):
    """Take in a list of 5 integers and return them in a different order"""
    return "{3:02d} {4:02d} {2:04d} {0:02d} {1:02d}".format(*cinco)


def task_five(fruit_info):
    """Return a formatted string using f' formatting"""
    return f'The weight of an {fruit_info[0][:-1]} is {fruit_info[1]} and '\
           f'the weight of a {fruit_info[2][:-1]} is {fruit_info[3]}'


def task_five_sp(fruit_info):
    """Return a formatted string using f' formatting"""
    return f'The weight of an {fruit_info[0][:-1].upper()} is '\
           f'{fruit_info[1]*1.2} and the weight of a '\
           f'{fruit_info[2][:-1].upper()} is {fruit_info[3]*1.2}'


def task_six(table):
    """Get table from user with name, age and cost.  Return formated table"""
    max_first = len(max([item[0] for item in table], key=len))
    max_age = 3
    max_last = len(max([item[2] for item in table], key=len))
    max_cost = len(max([item[3] for item in table], key=len))
    form_str = '{:' + f'{max_first + 2}' + '}{:' + f'{max_age + 2}' + '}'\
               '{:' + f'{max_last + 2}' + '}{:' + f'{max_cost +2}'+'}'
    # set table with header
    form_table = [(form_str.format("Name", "Age", "Last", "Cost"))]
    # format each row and add it to the table
    for row in table:
        form_table.append(form_str.format(row[0], row[1], row[2], row[3]))
    return form_table


def task_six_sp(numbers):
    """Do something"""
    return ('{:<5}' * len(numbers)).format(*numbers)

print(task_one((23, 123.4567, 10000, 12345.67)))
print(task_two((23, 123.4567, 10000, 12345.67)))
print(task_three((23, 123, 10000, 12345)))
print(task_three((1, 2, 3, 4, 5, 6, 7)))
print(task_three((1)))
print(task_four((4, 30, 2017, 2, 27)))
print(task_five(['oranges', 1.3, 'lemons', 1.1]))
print(task_five_sp(['oranges', 1.3, 'lemons', 1.1]))
task_six_table = task_six([["Bob", "27", "Zuruncle", "$-99.00"],
                           ["Suzy", "105", "Zuraunt", "$17.00"],
                           ["Jazzman", "4", "Jazzhands", "$9.00"],
                           ["Sal", "46", "T", "$1117.45"]])
for row in task_six_table:
    print(row)
print(task_six_sp((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
