#!/usr/bin/env python3
import sys


# Format string per the exercise definition
def task_one(in_tuple):
    print("Input string:", in_tuple)
    print()
    string_format = "file_{:03d}: {:.2f}, {:.2e}, {:.2e}"
    print("Formatted string:")
    return string_format.format(*in_tuple)


# Produces same output as task_one but with a different type of format
def task_two(in_tuple):
    print()
    print("Using f-string:")
    string_format = "file_{:03d}: {:.2f}, {:.2e}, {:.2e}"
    return f"file_{in_tuple[0]:03d}: {in_tuple[1]:.2f}, {in_tuple[2]:.2e}, {in_tuple[3]:.2e}"


def formatter(in_tuple):
    print()
    print("Dynamic string:")
    text = "the {} numbers are: ".format(len(in_tuple))
    form_string = text + ", ".join(["{:d}"] * len(in_tuple))
    return form_string.format(*in_tuple)


def task_four(in_tuple):
    print()
    print("Task 5:")
    form_string = "{:02d} " * len(in_tuple)
    return form_string.format(in_tuple[3], in_tuple[4], in_tuple[2], in_tuple[0], in_tuple[1])


# Use f-string to format a list
def task_five(in_list):
    print()
    fruit_1 = in_list[0].rstrip('s')
    fruit_2 = in_list[2].rstrip('s')
    weight_1 = in_list[1]
    weight_2 = in_list[3]

    orange_str = f"The weight of an {fruit_1} is {weight_1} "
    lemon_str = f"and the weight of a {fruit_2} is {weight_2}"
    print (orange_str + lemon_str)
    print()
    orange_str_2 = f"The weight of an {fruit_1.upper()} is {weight_1 * 1.2} "
    lemon_str_2 = f"and the weight of a {fruit_2.upper()} is {weight_2 * 1.2}"
    print (orange_str_2 + lemon_str_2)


def task_six(table_list):
    print()
    for item in table_list:
        print ("{0:2d} {1:3d} {2:4d}".format(*item))



# Test variables
random_strings = (2, 123.4567, 10000, 12345.67)
sample_tuples = (2, 3, 5, 45)
five_tuples = (4, 30, 2017, 2, 27)
t5_elements = ['oranges', 1.3, 'lemons', 1.1]
table_list = [('First', '$99.01', 'Second', '$88.09'),
              ('First', '$999999999.01', 'Second', '$88.09'),
              ('First', '$9999.01', 'Second', '$88.09')]
t6_tuple = ('First', '$999999999.01', 'Second', '$88.09')

# Tasks execute in order
print(task_one(random_strings))
print(task_two(random_strings))
print(formatter(sample_tuples))
print(task_four(five_tuples))
task_five(t5_elements)
task_six(t6_tuple)
