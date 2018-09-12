#!/usr/bin/env python3

# Task One

print('file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}'.format(2, 123.4567, 10000, 12345.67))

# Task Two

element_tuple = (2, 123.4567, 10000, 12345.67)
print('file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}'.format(*element_tuple))
print(f'file_{element_tuple[0]:0>3d}: {element_tuple[1]:.2f}, {element_tuple[2]:.2e}, {element_tuple[3]:.2e}')

# Task Three

def formatter(in_tuple):
    form_string = f"the {len(in_tuple)} numbers are: {'{} '*len(in_tuple)}"
    return form_string.format(*in_tuple)

print(formatter((1,2,3,4,5,6)))

# Task Four

five_element_tuple = (4,30,2017,2,27)
print("{3:0>2d}, {4}, {2}, {0:0>2d}, {1}".format(*five_element_tuple))

# Task Five

four_element_list = ['oranges',1.3,'lemons',1.1]
print(f"The weight of an {four_element_list[0][:-1]} is {four_element_list[1]} and the weight of a {four_element_list[2][:-1]} is {four_element_list[-1]}")
print(f"The weight of an {four_element_list[0][:-1].upper()} is {four_element_list[1]*1.2} and the weight of a {four_element_list[2][:-1].upper()} is {four_element_list[-1]*1.2}")
