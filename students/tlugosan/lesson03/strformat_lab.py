#!/usr/bin/env python3

# """"""

# original list
my_list = (2, 123.4567, 10000, 12345.67)
list_length = len(my_list)
print(", ".join(["{}"]*list_length).format(*my_list))

# TASK 1: print (2, 123.4567, 10000, 12345.67) as file_002 :, 123.46, 1.00e+04, 1.23e+04 using format() string
print("file_{0:0>3} :, {1:.2f}, {2:.2e}, {3:.2e}". format(*my_list))
print()

# TASK 2: print (2, 123.4567, 10000, 12345.67) as file_002 :, 123.46, 1.00e+04, 1.23e+04 using f-string
print(f"file_{my_list[0]:0>3} :, {my_list[1]:.2f}, {my_list[2]:.2e}, {my_list[3]:.2e}")
print()


# TASK 3: dynamically build up format strings
def formatter(in_tuple):
    len_in_tuple = len(in_tuple)
    new_string = "The {} numbers are: " + ", ".join(["{}"]*len_in_tuple).format(len_in_tuple, *in_tuple)
    return new_string


test_tuple1 = (2, 3, 4)
print(formatter(test_tuple1))
test_tuple2 = (2, 3, 4, 5, 6, 7)
print(formatter(test_tuple2))
print()

# TASK 4: print tuple with elements in different order by using positional reference
tuple_task_five = (4, 30, 2017, 2, 27)
print("{3:0>2}, {4}, {2}, {0:0>2}, {1}".format(*tuple_task_five))
