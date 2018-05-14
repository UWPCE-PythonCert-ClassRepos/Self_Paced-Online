from decimal import Decimal

# Task 1

tuple1 = ( 2, 123.4567, 10000, 12345.67)

format_task1 = 'file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}'.format(tuple1[0], tuple1[1], tuple1[2], tuple1[3])
print(format_task1)

# Task 2

tuple1 = ( 2, 123.4567, 10000, 12345.67)

first_part = '{:0>3d}'.format(tuple1[0])
second_part = '{:.2f}'.format(tuple1[1])
third_part = '{:.2e}'.format(tuple1[2])
fourth_part = '{:.2e}'.format(tuple1[3])

format_task2 = f'file_{first_part}: {second_part}, {third_part}, {fourth_part}'

print(format_task2)

# Task 3

def formatter(in_tuple):
    modifier = 'the {} numbers are: '.format(len(in_tuple)) + (len(in_tuple) * '{:d}, ')
    return modifier[:-2].format(*in_tuple)

assert formatter((2,3,5)) == 'the 3 numbers are: 2, 3, 5'
assert formatter((2,3,5,7,9)) == 'the 5 numbers are: 2, 3, 5, 7, 9'

# Task 4

tuple4 = (4, 30, 2017, 2, 27)

string_modified = '{:0>2d} {:d} {:d} {:0>2d} {:d}'.format(tuple4[3], tuple4[4], tuple4[2], tuple4[0], tuple4[1])
print(string_modified)

# Task 5

# Part 1
element_list = ['oranges', 1.3, 'lemons', 1.1]
new_format1 = f'The weight of an {element_list[0][:-1]} is {element_list[1]} and the weight of a {element_list[2][:-1]} is {element_list[3]}'
print(new_format1)

# Part 2

new_format2 = f'The weight of an {element_list[0][0:1].upper() + element_list[0][1:-1]} is {1.2 * element_list[1]} and the weight of a {element_list[2][0:1].upper() + element_list[2][1:-1]} is {1.2 * element_list[3]}'
print(new_format2)

# Task 6

# Part 1

first_row = '{:14} {:>3d} {:>12}'.format('Karla', 50, '$2500.11')
second_row = '{:14} {:>3d} {:>12}'.format('Sam', 66, '$5.23')
third_row = '{:14} {:>3d} {:>12}'.format('Sabrina', 56, '$107.07')

print(first_row)
print(second_row)
print(third_row)

# Part 2

part2 = tuple(range(1,11))
print(('{:5d}' * len(part2)).format(*part2))
