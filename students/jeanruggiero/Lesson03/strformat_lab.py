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
file_disp2 = "file_{name:03d} :  {size:.2f}, {use:.2e}, \
{key:.3G}".format(**file_info2)
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

##################################TASK 5#######################################
def article(string):
    """Return the proper article (a or an) for a given string"""
    # Check if the first letter of the string is a vowel and return article
    return 'an' if string[0].lower() in 'aeiouy' else 'a'

fruit_info = ['oranges', 1.3, 'lemons', 1.1]
# Create fstring with singular fruit and appropriate article
fruit_string = f"The weight of {article(fruit_info[0])} {fruit_info[0][0:-1]} \
is {fruit_info[1]} and the weight of {article(fruit_info[2])} \
{fruit_info[2][0:-1]} is {fruit_info[3]}"
print(fruit_string)

# Create fstring with names of fruits in upper case and weights increased by 20%
fruit_string2 = f"The weight of {article(fruit_info[0])} \
{fruit_info[0][0:-1].upper()} is {fruit_info[1]*1.2} and the weight of \
{article(fruit_info[2])} {fruit_info[2][0:-1].upper()} is {fruit_info[3]*1.2}"
print(fruit_string2)

##################################TASK 6#######################################
# Define a table of rows consisting of a name, age, and cost
rows = (('Jean',21,5000), ('Andrew',105,3.20), ('Cookie Monster',5,400.687690))

# Determine width needed for each column by calculating max length of data in
# each field
name_width = str(max(len(row[0]) for row in rows))
# Convert numbers to strings to determine their length in characters
age_width = str(max(len(str(row[1])) for row in rows))
# Convert the cost to an integer to remove decimal places (since there are an
# unknown number of them), then add 3 to the length to accomodate for a period
# and 2 decimal places
cost_width = str(max(len(str(int(row[2]))) for row in rows)+3)

# Build format string
row_format = '{:<' + name_width + 's}  {:<' + age_width + 'd}  ${:>' + \
cost_width + '.2f}'

# Print formatted rows
for row in rows:
    print(row_format.format(*row))

# Print a tuple of consecutive numbers in a column of width 5
nums = (1,2,3,4,5,6,7,8,9,10)
print(('{:5d}\n'*len(nums)).format(*nums))
