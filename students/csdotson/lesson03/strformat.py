#!/usr/bin/env python3
# Lesson 3 - String Formatting Excercise

### Task 1 ############################################################
# String formatting the following Tuple using '.format'
a_tuple = (2, 123.4567, 10000, 12345.67)

output = "file_{:03d}: {:3.2f}, {:.2e}, {:.2e}".format(*a_tuple)

print("*" * 5 + "Task 1" + "*" * 5)
print(output + '\n')


### Task 2 ############################################################
# String formatting the following Tuple f-string
a_tuple = (2, 123.4567, 10000, 12345.67)

output = f"file_{a_tuple[0]:03d}: {a_tuple[1]:3.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.2e}"

print("*" * 5 + "Task 2" + "*" * 5)
print(output + '\n')


### Task 3 ############################################################
# Using 'formatter' function to dynamically build string
def formatter(in_tuple):
    l = len(in_tuple)
    form_string = "The {} numbers are: ".format(l) + ", ".join(["{}"] * l)
    return form_string.format(*in_tuple)

print("*" * 5 + "Task 3" + "*" * 5)
tup_1 = (1, 2, 3)
print("First tuple:", tup_1)
print("Formatted first tuple:", formatter(tup_1) + '\n')

tup_2 = (1, 2, 3, 4, 5)
print("Second tuple:", tup_2)
print("Formatted second tuple:", formatter(tup_2) + '\n')


### Task 4 ############################################################
# Tuple formatting using index
a_tuple = (4, 30, 2017, 2, 27)

output = "{:02d} {} {} {:02d} {}".format(a_tuple[3], a_tuple[4], a_tuple[2], a_tuple[0], a_tuple[1])

print("*" * 5 + "Task 4" + "*" * 5)
print(output + '\n')


### Task 5 ############################################################
# Formatting output using f-strings
a_list = ['oranges', 1.3, 'lemons', 1.1]

output_1 = f'The weight of an {a_list[0][0:-1]} is {a_list[1]} and the weight of a {a_list[2][0:-1]} is {a_list[3]}'
output_2 = f'The weight of an {a_list[0][0:-1].upper()} is {a_list[1] * 1.2} and the weight of a {a_list[2][0:-1].upper()} is {a_list[3] * 1.2}'

print("*" * 5 + "Task 5" + "*" * 5)
print(output_1 + '\n')
print(output_2 + '\n')


### Task 6 ############################################################
# Display data in columns
header = '{:^20}{:^10}{:^10}'.format("NAME", "AGE", "COST")
info = [["Ben Hondo", "40", "$56.89"],["Ludwig Vander", "23", "$134.78"],["Squint Ringo", "35", "$1456.90"]]

print("*" * 5 + "Task 6" + "*" * 5)
print(header)
for i, j, k in info:
    print('{:20}{:^10}{:>10}'.format(i, j, k))

# Bonus - print tuple with 10 elements
tup = tuple(range(10))

print()
print("Tuple quick print:")
print(("{:5d}" * len(tup)).format(*tup))
