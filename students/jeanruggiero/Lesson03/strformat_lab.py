#!/usr/bin/env python

##################################TASK 1#######################################
# Tuple containing info about the file
file_info = ( 2, 123.4567, 10000, 12345.67)

# Format string to format file_info
file_format = 'file_{:03d} :  {:.2f}, {:.2e}, {:.3G}'

# Apply format string to file_info and print results
file_disp = file_format.format(*file_info)
print(file_disp)

##################################TASK 2#######################################

# Create a dictionary defining the file info
file_info2 = {'name': 2, 'size': 123.4567, 'use': 10000, 'key': 12345.67}

# Create a format string that uses the dictionary keywords and apply it
file_disp2 = "file_{name:03d} :  {size:.2f}, {use:.2e}, {key:.3G}".format(**file_info2)
print(file_disp2)


##################################TASK 3#######################################

def formatter(in_tuple):
    """Prints the numbers in a tuple of arbitrary length."""
    # Build a format string
    form_string = 'the {:d} numbers are: '+'{:d}, '*(len(in_tuple)-1) + '{:d}'
    # Apply format string and print results
    return form_string.format(len(in_tuple), *in_tuple)

##################################TASK 4#######################################

tuple_four = ( 4, 30, 2017, 2, 27)
# Create format string using tuple indices, apply to tuple, and print
print('{3:02d} {4:d} {2:d} {0:02d} {1:d}'.format(*tuple_four))
