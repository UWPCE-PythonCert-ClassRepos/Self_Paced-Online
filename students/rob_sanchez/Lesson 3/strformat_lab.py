#!/usr/bin/env python3
import sys


# Format string per the exercise definition
def task_one(in_tuple):
    print("Input string:", in_tuple)
    string_format = "file_{:03d}: {:.2f}, {:.2e}, {:.2e}"
    print("\nTask 1 - Formatted string:")
    return string_format.format(*in_tuple)


# Produces same output as task_one but with a different type of format
def task_two(in_tuple):
    print("\nTask 2 - Using f-string:")
    string_format = "file_{:03d}: {:.2f}, {:.2e}, {:.2e}"
    return f"file_{in_tuple[0]:03d}: {in_tuple[1]:.2f}, {in_tuple[2]:.2e}, {in_tuple[3]:.2e}"


# Dynamically formats a string
def formatter(in_tuple):
    print("\nTask 3 - Dynamic string:")
    text = "the {} numbers are: ".format(len(in_tuple))
    form_string = text + ", ".join(["{:d}"] * len(in_tuple))
    return form_string.format(*in_tuple)


#
def task_four(in_tuple):
    print("\nTask 4:")
    form_string = "{:02d} " * len(in_tuple)
    return form_string.format(in_tuple[3], in_tuple[4], in_tuple[2], in_tuple[0], in_tuple[1])


# Use f-string to format a list
def task_five(in_list):
    print("\nTask 5:")
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


# Prints a table with alignment specifiers
def task_six(table_list):
    print("\nTask 6:")
    width = 15
    tbl_row = '{:{align}{width}}' * len(table_list[0])
    for item in table_list:
        print (tbl_row.format(*item, align='<', width=width))


# Extra task 6
def tas_six_pt2(in_tuple):
    print("\nExtra task:")
    print (('{:5}'*len(in_tuple)).format(*in_tuple))


# Test variables
random_strings = (2, 123.4567, 10000, 12345.67)
sample_tuples = (2, 3, 5, 45)
five_tuples = (4, 30, 2017, 2, 27)
t5_elements = ['oranges', 1.3, 'lemons', 1.1]
table_list = ([['Name', 'Cost', 'Age(years)'],
              ['Hamster', '$25.39', '1'],
              ['Turtle', '$150.00', '6'],
              ['Pangolin', '$1000.00', '8'],
              ['Tiger', '$8,999.99', '3']])
t6_tuple = ('1', '2', '3', '3', '4', '5', '6', '7', '8', '9', '10')

# Tasks execute in order
print(task_one(random_strings))
print(task_two(random_strings))
print(formatter(sample_tuples))
print(task_four(five_tuples))
task_five(t5_elements)
task_six(table_list)
tas_six_pt2(t6_tuple)
