# strformat_lab Exercise by tfbanks

#!/usr/bin/env python3

beg_tup = (2, 123.4567, 10000, 12345.67)

# Task One - Reformat beg_str to 'File_002: 123.46, 1.00e+04, 1.23e+04'
tsk1str = f'File_{beg_tup[0]:03}: {beg_tup[1]:.{2}f}, {beg_tup[2]:.2e}, {beg_tup[3]:.2e}'
print("Task one output: ", tsk1str, "\n")


# Task Two - Do task one again, but differently
tsk2str = "File_{:03}: {:.2f}, {:.2e}, {:.2e}".format(*beg_tup)  # sets format and then applies to the tuple items
print("Task two output: ", tsk2str, "\n")


# Task Three - Dynamically build up format strings
def formatter(in_tuple):
    lt = len(in_tuple)  # Takes the length of the tuple to calculate the number of variables input
    format_string = f"The {lt} numbers are: " + (("{:d}, " * (lt-1)) + "{:d}")  # Sets the format String
    print(format_string.format(*in_tuple))  # Prints the format string for the items in the tuple

# three different scenarios

tuple_4nums = (5, 10, 15, 20)
tuple_8nums = (3, 6, 9, 12, 15, 18, 21, 24)
tuple_12nums = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24)

print("Task three outputs for different tuple examples of 4, 8, and 12 numbers:")
formatter(tuple_4nums)
formatter(tuple_8nums)
formatter(tuple_12nums)
print()


# Task 4 change the tuple(4, 30, 2017, 2, 27) to '02 27 2017 04 30' using Index
tsk4_tup = (4, 30, 2017, 2, 27)
tsk4str = f'{tsk4_tup[3]:02} {tsk4_tup[4]} {tsk4_tup[2]} {tsk4_tup[0]:02} {tsk4_tup[1]}'
print("Task four output: ", tsk4str)
print()

# Task 5
# part1: given tsk5_list (below), Return 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
# part2: given tsk5_list (below), Return 'The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32'

tsk5_list = ['oranges', 1.3, 'lemons', 1.1]
tsk5str1 = f'The weight of an {tsk5_list[0][:-1]} is {tsk5_list[1]} and the weight of a {tsk5_list[2][:-1]} is {tsk5_list[3]}'
tsk5str2 = f'The weight of an {tsk5_list[0][:-1].upper()} is {tsk5_list[1]*1.2} and the weight of a {tsk5_list[2][:-1].upper()} is {tsk5_list[3]*1.2}'
print("Task five part 1 output: ", tsk5str1)
print("Task five part 2 output: ", tsk5str2, "\n")

# Task 6 - print rows of data with nice formatting and then set up 1-10 to print with column width of 5
rows = [
        ['Name', 'Age', 'Cost'],
        ['-----', '----', '--------'],
        ['Mike', 6, '$12.25'],
        ['Abby', 12, '$101.50'],
        ['Andrew', 15, '$1,077.77'],
        ['Jimmy', 20, '$8,120.35'],
        ['Jessica', 24, '$10,553.82']
        ]

print("Task six part 1 output: ")
for r in rows:
    print("{:<8} {:^3} {:>10}".format(*r))
print()

print("Task six part 2 output: ")
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(("{:^5}"*len(nums)).format(*nums), "\n")


close_statement = input("Press Any key to exit")
