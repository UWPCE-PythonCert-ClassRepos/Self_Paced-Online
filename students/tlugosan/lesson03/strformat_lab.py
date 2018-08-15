#!/usr/bin/env python3

"""Formatting strings"""

# original list
my_list = (2, 123.4567, 10000, 12345.67)
list_length = len(my_list)
print(", ".join(["{}"] * list_length).format(*my_list))

# TASK 1: print (2, 123.4567, 10000, 12345.67) as file_002 :, 123.46, 1.00e+04, 1.23e+04 using format() string
print("file_{0:0>3} :, {1:.2f}, {2:.2e}, {3:.2e}".format(*my_list))
print()

# TASK 2: print (2, 123.4567, 10000, 12345.67) as file_002 :, 123.46, 1.00e+04, 1.23e+04 using f-string
print(
    f"file_{my_list[0]:0>3} :, {my_list[1]:.2f}, {my_list[2]:.2e}, {my_list[3]:.2e}")
print()


# TASK 3: dynamically build up format strings
def formatter(in_tuple):
    """This function dynamically builds up format strings."""
    len_in_tuple = len(in_tuple)
    new_string = "The {} numbers are: " + \
        ", ".join(["{}"] * len_in_tuple).format(len_in_tuple, *in_tuple)
    return new_string


test_tuple1 = (2, 3, 4)
print(formatter(test_tuple1))
test_tuple2 = (2, 3, 4, 5, 6, 7)
print(formatter(test_tuple2))
print()

# TASK 4: print tuple with elements in different order
tuple_task_four = (4, 30, 2017, 2, 27)
print("{3:0>2}, {4}, {2}, {0:0>2}, {1}".format(*tuple_task_four))
print()

# TASK 5: format string using f-string
tuple_task_five = ['oranges', 1.3, 'lemons', 1.1]
print(
    f"The weight of an {tuple_task_five[0]} is {tuple_task_five[1]} and the weight of a {tuple_task_five[2]} is {tuple_task_five[3]}")
print()
print(
    f"The weight of an {tuple_task_five[0].upper()} is {tuple_task_five[1]*1.2} and the weight of a {tuple_task_five[2].upper()} is {tuple_task_five[3]*1.2}")
print()

# TASK 6; display lists in columns
table = [
    ['name', 'Toni L', 'age', 43, 'cost', '$23,02'],
    ['name', 'Andrea B', 'age', 28, 'cost', '$13323,56'],
    ['name', 'Nancy T', 'age', 60, 'cost', '$455,99']
    ]

for row in table:
    print("{0:<10}{1:<20}{2:<5}{3:<5d}{4:<10}{5:>20}".format(*row))

print()

consecutive_number= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
length_consecutive_numbers = len(consecutive_number)
print(" ".join(["{:>5}"] * length_consecutive_numbers).format(*consecutive_number))
